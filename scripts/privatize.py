#!/usr/bin/env python3
"""Rename the identifiers the cross-repo questions ask about, so a backend that is a famous public repository cannot be answered from memory.

    python privatize.py BACKEND_DIR            # the base ("private") backend
    python privatize.py BACKEND_DIR --drift    # then the planted refactors on top of it

Every rename is asserted to have applied. Only the backend changes; the storefront never mentions these names.
"""
import pathlib, re, subprocess, sys

root = pathlib.Path(sys.argv[1])
drift = "--drift" in sys.argv
extra = "--extra" in sys.argv
J = lambda *p: next(root.rglob(p[-1]))  # the one file with this name


def edit(name, pairs, regex=False):
    f = J(name)
    s = f.read_text(encoding="utf-8")
    for a, b in pairs:
        n = len(re.findall(a, s)) if regex else s.count(a)
        assert n, f"{name}: nothing matched {a!r}"
        s = re.sub(a, b, s) if regex else s.replace(a, b)
    f.write_text(s, encoding="utf-8")


def rename_class(old, new):
    files = subprocess.run(["grep", "-rlw", old, "--include=*.java", str(root)], capture_output=True, text=True).stdout.split()
    assert files, old
    for f in files:
        p = pathlib.Path(f)
        p.write_text(re.sub(rf"\b{old}\b", new, p.read_text(encoding="utf-8")), encoding="utf-8")
    src = next(root.rglob(f"{old}.java"))
    src.rename(src.with_name(f"{new}.java"))


if extra:
    # a second wave of renames for the harder change tasks: fields reached through inheritance (PersistableOrder extends Order, PersistablePayment extends PaymentEntity, ReadableOrderList extends ReadableList)
    def edit_path(rel, pairs):
        f = root / rel
        t = f.read_text(encoding="utf-8")
        for a, b in pairs:
            assert re.search(a, t), f"{rel}: nothing matched {a!r}"
            t = re.sub(a, b, t)
        f.write_text(t, encoding="utf-8")
    M = "sm-shop-model/src/main/java/com/salesmanager/shop/model/"
    edit_path(M + "order/v1/PersistableOrder.java", [(r"shippingQuote", "quoteId"), (r"ShippingQuote", "QuoteId")])
    edit_path(M + "order/v1/Order.java", [(r"customerAgreement", "termsAccepted"), (r"CustomerAgreement", "TermsAccepted"), (r"\bcomments\b", "orderNote"), (r"Comments", "OrderNote")])
    edit_path(M + "order/transaction/PersistablePayment.java", [(r"paymentToken", "cardToken"), (r"PaymentToken", "CardToken")])
    edit_path(M + "order/transaction/PaymentEntity.java", [(r"paymentModule", "processor"), (r"PaymentModule", "Processor")])
    edit_path(M + "entity/ReadableList.java", [(r"\btotalPages\b", "pageCount"), (r"TotalPages", "PageCount"), (r"\brecordsTotal\b", "totalRecords"), (r"RecordsTotal", "TotalRecords"), (r"\bnumber\b", "itemsOnPage"), (r"\bgetNumber\b", "getItemsOnPage"), (r"\bsetNumber\b", "setItemsOnPage")])
    print("ok extra")
elif not drift:
    # methods, renamed inside their own controller file before the classes are renamed
    edit("ShoppingCartApi.java", [(r"\baddToCart\(", "appendItem("), (r"\bmodifyCart\(", "replaceBasket("), (r"\bdeleteCartItem\(", "removeLine(")], regex=True)
    edit("AuthenticateCustomerApi.java", [(r"ResponseEntity<\?> authenticate\(", "ResponseEntity<?> openSession(")], regex=True)
    edit("SearchApi.java", [(r"List<SearchItem> search\(", "List<SearchItem> lookup(")], regex=True)
    edit("PublicConfigsApi.java", [(r"\bgetConfig\(", "readSettings(")], regex=True)
    edit("ProductReviewApi.java", [(r"\bgetAll\(", "listFeedback(")], regex=True)
    edit("OrderShippingApi.java", [(r"ReadableShippingSummary shipping\(", "ReadableShippingSummary quote(")], regex=True)
    # fields
    edit("PersistableShoppingCartItem.java", [(r"promoCode", "voucher"), (r"PromoCode", "Voucher")], regex=True)
    edit("SearchProductRequest.java", [(r"\bcount\b", "size"), (r"\bstart\b", "offset"), (r"getCount", "getSize"), (r"setCount", "setSize"), (r"getStart", "getOffset"), (r"setStart", "setOffset")], regex=True)
    edit("Configs.java", [(r"allowOnlinePurchase", "purchasingEnabled"), (r"AllowOnlinePurchase", "PurchasingEnabled")], regex=True)
    for a, b in [("ShoppingCartApi", "BasketEndpoint"), ("PersistableShoppingCartItem", "BasketLineInput"), ("AuthenticateCustomerApi", "SessionEndpoint"),
                 ("AuthenticationRequest", "SignInForm"), ("SearchApi", "CatalogLookup"), ("SearchProductRequest", "LookupQuery"),
                 ("PublicConfigsApi", "StoreSettingsEndpoint"), ("Configs", "StoreSettings"), ("ProductReviewApi", "FeedbackEndpoint"),
                 ("OrderShippingApi", "ShippingQuoteEndpoint"), ("AddressLocation", "GeoPoint"), ("ReadableShippingSummary", "QuoteSummary")]:
        rename_class(a, b)
else:
    edit("StoreSettingsEndpoint.java", [(r"\breadSettings\(", "readPublicSettings(")], regex=True)
    edit("BasketLineInput.java", [(r"voucher", "discountCode"), (r"Voucher", "DiscountCode")], regex=True)
    edit("BasketEndpoint.java", [('"/cart/{code}/product/{sku}"', '"/cart/{code}/product/{itemCode}"'), ('@PathVariable("sku") String sku', '@PathVariable("itemCode") String sku')])
    rename_class("SignInForm", "LoginPayload")
print("ok", "drift" if drift else "base")
