---
type: Code Module
title: "com.salesmanager.core.model.shoppingcart"
description: "com.salesmanager.core.model.shoppingcart: ShoppingCart, ShoppingCartAttributeItem, ShoppingCartItem"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java"
    sha256: "88f30aa644b28a274a2b04d317d061876feb52f9e5aaffceaa7183910ab7306c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java"
    sha256: "af891c3d90ca7a1547b284f271e7d2eae84d0ba29f807556edcf3eb993e1d875"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java"
    sha256: "6f22e946974c799cac1d068d7e6e0ff780c2709da5c7582bde755cf352e0c2b6"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.shoppingcart

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java`

## Types
- `ShoppingCart` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:43`
- `ShoppingCartAttributeItem` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:24`
- `ShoppingCartItem` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:34`

## Fields
- `ShoppingCart.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:52`
- `ShoppingCart.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:58`
- `ShoppingCart.shoppingCartCode: String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:66`
- `ShoppingCart.lineItems: Set<ShoppingCartItem>` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:69`
- `ShoppingCart.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:73`
- `ShoppingCart.customerId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:76`
- `ShoppingCart.orderId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:79`
- `ShoppingCart.ipAddress: String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:82`
- `ShoppingCart.promoCode: String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:85`
- `ShoppingCart.promoAdded: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:89`
- `ShoppingCart.obsolete: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:92`
- `ShoppingCartAttributeItem.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:36`
- `ShoppingCartAttributeItem.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:39`
- `ShoppingCartAttributeItem.productAttributeId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:44`
- `ShoppingCartAttributeItem.productAttribute: ProductAttribute` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:48`
- `ShoppingCartAttributeItem.shoppingCartItem: ShoppingCartItem` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:54`
- `ShoppingCartItem.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:46`
- `ShoppingCartItem.shoppingCart: ShoppingCart` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:51`
- `ShoppingCartItem.quantity: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:54`
- `ShoppingCartItem.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:57`
- `ShoppingCartItem.productId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:61`
- `ShoppingCartItem.sku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:65`
- `ShoppingCartItem.productVirtual: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:69`
- `ShoppingCartItem.attributes: Set<ShoppingCartAttributeItem>` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:72`
- `ShoppingCartItem.variant: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:75`
- `ShoppingCartItem.itemPrice: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:79`
- `ShoppingCartItem.subTotal: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:83`
- `ShoppingCartItem.finalPrice: FinalPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:87`
- `ShoppingCartItem.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:91`
- `ShoppingCartItem.obsolete: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:95`

## Functions and methods
- `ShoppingCart.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:94`
- `ShoppingCart.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:99`
- `ShoppingCart.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:104`
- `ShoppingCart.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:109`
- `ShoppingCart.isObsolete() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:115`
- `ShoppingCart.setObsolete(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:119`
- `ShoppingCart.getLineItems() -> Set<ShoppingCartItem>` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:123`
- `ShoppingCart.setLineItems(Set<ShoppingCartItem>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:127`
- `ShoppingCart.getShoppingCartCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:131`
- `ShoppingCart.setShoppingCartCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:136`
- `ShoppingCart.setCustomerId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:141`
- `ShoppingCart.getCustomerId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:145`
- `ShoppingCart.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:149`
- `ShoppingCart.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:153`
- `ShoppingCart.getIpAddress() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:157`
- `ShoppingCart.setIpAddress(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:161`
- `ShoppingCart.getPromoCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:166`
- `ShoppingCart.setPromoCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:170`
- `ShoppingCart.getPromoAdded() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:174`
- `ShoppingCart.setPromoAdded(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:178`
- `ShoppingCart.getOrderId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:182`
- `ShoppingCart.setOrderId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:186`
- `ShoppingCartAttributeItem.getShoppingCartItem() -> ShoppingCartItem` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:72`
- `ShoppingCartAttributeItem.setShoppingCartItem(ShoppingCartItem) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:76`
- `ShoppingCartAttributeItem.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:80`
- `ShoppingCartAttributeItem.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:85`
- `ShoppingCartAttributeItem.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:91`
- `ShoppingCartAttributeItem.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:96`
- `ShoppingCartAttributeItem.setProductAttributeId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:103`
- `ShoppingCartAttributeItem.getProductAttributeId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:107`
- `ShoppingCartAttributeItem.setProductAttribute(ProductAttribute) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:111`
- `ShoppingCartAttributeItem.getProductAttribute() -> ProductAttribute` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:115`
- `ShoppingCartItem.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:118`
- `ShoppingCartItem.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:123`
- `ShoppingCartItem.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:129`
- `ShoppingCartItem.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:134`
- `ShoppingCartItem.setAttributes(Set<ShoppingCartAttributeItem>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:140`
- `ShoppingCartItem.getAttributes() -> Set<ShoppingCartAttributeItem>` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:144`
- `ShoppingCartItem.setItemPrice(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:148`
- `ShoppingCartItem.getItemPrice() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:152`
- `ShoppingCartItem.setQuantity(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:156`
- `ShoppingCartItem.getQuantity() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:160`
- `ShoppingCartItem.getShoppingCart() -> ShoppingCart` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:164`
- `ShoppingCartItem.setShoppingCart(ShoppingCart) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:168`
- `ShoppingCartItem.setProductId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:172`
- `ShoppingCartItem.getProductId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:176`
- `ShoppingCartItem.setProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:180`
- `ShoppingCartItem.getProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:184`
- `ShoppingCartItem.addAttributes(ShoppingCartAttributeItem) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:188`
- `ShoppingCartItem.removeAttributes(ShoppingCartAttributeItem) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:193`
- `ShoppingCartItem.removeAllAttributes() -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:198`
- `ShoppingCartItem.setSubTotal(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:202`
- `ShoppingCartItem.getSubTotal() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:206`
- `ShoppingCartItem.setFinalPrice(FinalPrice) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:210`
- `ShoppingCartItem.getFinalPrice() -> FinalPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:214`
- `ShoppingCartItem.isObsolete() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:218`
- `ShoppingCartItem.setObsolete(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:222`
- `ShoppingCartItem.isProductVirtual() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:227`
- `ShoppingCartItem.setProductVirtual(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:231`
- `ShoppingCartItem.getSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:235`
- `ShoppingCartItem.setSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:239`
- `ShoppingCartItem.getVariant() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:243`
- `ShoppingCartItem.setVariant(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:247`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:89`
- [com.salesmanager.core.model.catalog.product.attribute.ProductAttribute](/modules/com.salesmanager.core.model.catalog.product.attribute.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:46`
- [com.salesmanager.core.model.catalog.product.price.FinalPrice](/modules/com.salesmanager.core.model.catalog.product.price.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:85`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:51`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartAttributeItem.java:38`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCartItem.java:56`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/shoppingcart/ShoppingCart.java:71`

## Tests
- `com.salesmanager.test.shoppingcart.ShoppingCartTest`
