---
type: Code Module
title: "com.salesmanager.shop.mapper.order"
description: "com.salesmanager.shop.mapper.order: ReadableOrderProductMapper, ReadableOrderTotalMapper"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java"
    sha256: "10bc462e5dd72c3c36be3df184a9dd31e3a633318bf790934c7a7cef13a2d0cd"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java"
    sha256: "8cb749e670c701b677176695bdde2eb7eccda15109799d26d4a2b4b7910490cf"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.mapper.order

Source: `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java`

## Types
- `ReadableOrderProductMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:32`
- `ReadableOrderTotalMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:21`

## Fields
- `ReadableOrderProductMapper.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:36`
- `ReadableOrderProductMapper.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:39`
- `ReadableOrderProductMapper.readableProductMapper: ReadableProductMapper` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:42`
- `ReadableOrderProductMapper.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:46`
- `ReadableOrderTotalMapper.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:25`
- `ReadableOrderTotalMapper.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:28`

## Functions and methods
- `ReadableOrderProductMapper.convert(OrderProduct, MerchantStore, Language) -> ReadableOrderProduct` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:48`
- `ReadableOrderProductMapper.merge(OrderProduct, ReadableOrderProduct, MerchantStore, Language) -> ReadableOrderProduct` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:54`
- `ReadableOrderTotalMapper.convert(OrderTotal, MerchantStore, Language) -> ReadableOrderTotal` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:30`
- `ReadableOrderTotalMapper.merge(OrderTotal, ReadableOrderTotal, MerchantStore, Language) -> ReadableOrderTotal` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:36`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:35`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:24`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:38`
- [com.salesmanager.shop.mapper.catalog.product.ReadableProductMapper](/modules/com.salesmanager.shop.mapper.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:41`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:44`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderTotalMapper.java:27`

## Calls
- `ReadableOrderProductMapper.merge` calls [com.salesmanager.shop.mapper.catalog.product.ReadableProductMapper](/modules/com.salesmanager.shop.mapper.catalog.product.md) `ReadableProductMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/mapper/order/ReadableOrderProductMapper.java:113`
