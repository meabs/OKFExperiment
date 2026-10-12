import sys, pathlib
d = pathlib.Path(sys.argv[1]); a = d / "src/redux/actions/cartActions.js"; s = a.read_text()
assert "item.id + '?store='" in s
s = s.replace("constant.ACTION.PRODUCT + item.id + '?store='", "constant.ACTION.PRODUCT + item.sku + '?store='")
s = s.replace("userData, selectedProductOptions) => {\n  return async dispatch => {\n    dispatch(setLoader(true))\n    try {\n      let action;\n      let param;", "userData, selectedProductOptions, promoCode) => {\n  return async dispatch => {\n    dispatch(setLoader(true))\n    try {\n      let action;\n      let param;", 1)
s = s.replace("      console.log('Cart parameters ' + JSON.stringify(param));", "      if (promoCode) { param.voucher = promoCode }\n      console.log('Cart parameters ' + JSON.stringify(param));", 1)
a.write_text(s)
u = d / "src/util"; u.mkdir(parents=True, exist_ok=True)
(u / "checkoutRequest.mjs").write_text("""export function buildCheckoutRequest({ cartCode, shippingOptionId, currency, paymentToken, paymentModule, amount, agreedToTerms, comments }) {
  return { method: "POST", path: `cart/${cartCode}/checkout`, body: { quoteId: shippingOptionId, currency, termsAccepted: agreedToTerms, orderNote: comments,
    payment: { paymentType: "CREDITCARD", transactionType: "CAPTURE", processor: paymentModule, cardToken: paymentToken, amount } } };
}
""")
(u / "ordersApi.mjs").write_text("""export function normalizeOrderList(r) { return { orders: r.orders ?? [], pages: r.pageCount ?? 0, total: r.totalRecords ?? 0, onThisPage: r.itemsOnPage ?? 0 }; }
""")
