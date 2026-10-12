---
type: Code Module
title: "com.salesmanager.shop.mapper.cart"
description: "com.salesmanager.shop.mapper.cart: ReadableShoppingCartMapper"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java"
    sha256: "7efebf622a060c5b2cc75655edc8ceb5b3a60e411471e35ed1b383858338004b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.mapper.cart

Source: `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java`

## Types
- `ReadableShoppingCartMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:56`

## Fields
- `ReadableShoppingCartMapper.LOG: Logger` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:59`
- `ReadableShoppingCartMapper.shoppingCartCalculationService: ShoppingCartCalculationService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:62`
- `ReadableShoppingCartMapper.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:65`
- `ReadableShoppingCartMapper.productAttributeService: ProductAttributeService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:68`
- `ReadableShoppingCartMapper.productVariantService: ProductVariantService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:71`
- `ReadableShoppingCartMapper.readableMinimalProductMapper: ReadableMinimalProductMapper` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:74`
- `ReadableShoppingCartMapper.readableProductVariationMapper: ReadableProductVariationMapper` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:77`
- `ReadableShoppingCartMapper.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:81`

## Functions and methods
- `ReadableShoppingCartMapper.convert(ShoppingCart, MerchantStore, Language) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:83`
- `ReadableShoppingCartMapper.image(ProductVariantImage, MerchantStore, Language) -> ReadableImage` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:89`
- `ReadableShoppingCartMapper.merge(ShoppingCart, ReadableShoppingCart, MerchantStore, Language) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:98`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:64`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductAttributeService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:67`
- [com.salesmanager.core.business.services.catalog.product.variant.ProductVariantService](/modules/com.salesmanager.core.business.services.catalog.product.variant.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:70`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartCalculationService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:61`
- [com.salesmanager.shop.mapper.catalog.ReadableMinimalProductMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:73`
- [com.salesmanager.shop.mapper.catalog.ReadableProductVariationMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:76`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:79`

## Calls
- `ReadableShoppingCartMapper.image` calls [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `ImageFilePath.buildCustomTypeImageUtils` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:94`
- `ReadableShoppingCartMapper.merge` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculatePriceQuantity` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:167`
- `ReadableShoppingCartMapper.merge` calls [com.salesmanager.core.business.services.shoppingcart.ShoppingCartCalculationService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `ShoppingCartCalculationService.calculate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:259`
- `ReadableShoppingCartMapper.merge` calls [com.salesmanager.shop.mapper.catalog.ReadableMinimalProductMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableMinimalProductMapper.merge` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:134`
- `ReadableShoppingCartMapper.merge` calls [com.salesmanager.shop.mapper.catalog.ReadableProductVariationMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableProductVariationMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/mapper/cart/ReadableShoppingCartMapper.java:142`
