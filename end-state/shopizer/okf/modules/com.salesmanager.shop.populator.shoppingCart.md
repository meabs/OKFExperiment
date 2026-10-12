---
type: Code Module
title: "com.salesmanager.shop.populator.shoppingCart"
description: "com.salesmanager.shop.populator.shoppingCart: ShoppingCartDataPopulator, ShoppingCartModelPopulator"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java"
    sha256: "8ed73d579eaba32b84f9c01aa2fddb3b44f86e00a98bbe993ba3960e5cdf6a63"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java"
    sha256: "69426acfa7b515b557f960285e55d1f7ea60f8935e4d3034be07ebbd4958db76"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.populator.shoppingCart

Source: `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java`

## Types
- `ShoppingCartDataPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:43`
- `ShoppingCartModelPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:36`

## Fields
- `ShoppingCartDataPopulator.LOG: Logger` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:47`
- `ShoppingCartDataPopulator.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:49`
- `ShoppingCartDataPopulator.shoppingCartCalculationService: ShoppingCartCalculationService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:51`
- `ShoppingCartDataPopulator.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:53`
- `ShoppingCartModelPopulator.LOG: Logger` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:41`
- `ShoppingCartModelPopulator.shoppingCartService: ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:43`
- `ShoppingCartModelPopulator.customer: Customer` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:45`
- `ShoppingCartModelPopulator.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:57`
- `ShoppingCartModelPopulator.productAttributeService: ProductAttributeService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:70`

## Functions and methods
- `ShoppingCartDataPopulator.getimageUtils() -> ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:55`
- `ShoppingCartDataPopulator.setimageUtils(ImageFilePath) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:62`
- `ShoppingCartDataPopulator.createTarget() -> ShoppingCartData` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:68`
- `ShoppingCartDataPopulator.getOrderService() -> ShoppingCartCalculationService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:77`
- `ShoppingCartDataPopulator.getPricingService() -> PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:83`
- `ShoppingCartDataPopulator.populate(ShoppingCart, ShoppingCartData, MerchantStore, Language) -> ShoppingCartData` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:88`
- `ShoppingCartDataPopulator.setPricingService(PricingService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:218`
- `ShoppingCartDataPopulator.setShoppingCartCalculationService(ShoppingCartCalculationService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:227`
- `ShoppingCartModelPopulator.getShoppingCartService() -> ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:47`
- `ShoppingCartModelPopulator.setShoppingCartService(ShoppingCartService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:52`
- `ShoppingCartModelPopulator.getProductService() -> ProductService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:60`
- `ShoppingCartModelPopulator.setProductService(ProductService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:65`
- `ShoppingCartModelPopulator.getProductAttributeService() -> ProductAttributeService` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:73`
- `ShoppingCartModelPopulator.setProductAttributeService(ProductAttributeService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:78`
- `ShoppingCartModelPopulator.populate(ShoppingCartData, ShoppingCart, MerchantStore, Language) -> ShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:84`
- `ShoppingCartModelPopulator.createCartItem(com.salesmanager.core.model.shoppingcart.ShoppingCart, ShoppingCartItem, MerchantStore) -> com.salesmanager.core.model.shoppingcart.ShoppingCartItem` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:191`
- `ShoppingCartModelPopulator.createTarget() -> ShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:257`
- `ShoppingCartModelPopulator.getCustomer() -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:265`
- `ShoppingCartModelPopulator.setCustomer(Customer) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:270`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:49`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:57`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductAttributeService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:70`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartCalculationService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:51`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:43`
- [com.salesmanager.core.model.customer.Customer](/modules/com.salesmanager.core.model.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:45`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:53`

## Calls
- `ShoppingCartDataPopulator.populate` calls [com.salesmanager.core.business.services.shoppingcart.ShoppingCartCalculationService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `ShoppingCartCalculationService.calculate` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:186`
- `ShoppingCartDataPopulator.populate` calls [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `ImageFilePath.buildProductImageUtils` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartDataPopulator.java:132`
- `ShoppingCartModelPopulator.createCartItem` calls [com.salesmanager.core.model.shoppingcart.ShoppingCartItem](/modules/com.salesmanager.core.model.shoppingcart.md) `ShoppingCartItem.addAttributes` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:241`
- `ShoppingCartModelPopulator.populate` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create`, `SalesManagerEntityService.update` `sm-shop/src/main/java/com/salesmanager/shop/populator/shoppingCart/ShoppingCartModelPopulator.java:102`
