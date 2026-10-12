---
type: Code Module
title: "com.salesmanager.shop.model.catalog.product.variation"
description: "com.salesmanager.shop.model.catalog.product.variation: PersistableProductVariation, ProductVariationEntity, ReadableProductVariation"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java"
    sha256: "b9403edcb0ef37f429c55eee614d54e8ce5eb2cbb686e62cc6535d63f3cbc8ef"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java"
    sha256: "880e521b65ef9579c2c4e27b200f79bacf7769ca307f12c50a25a987f651908f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java"
    sha256: "3edd435a3461b13022b74e083908b85d6a03c17f78ceb19f1e9127bd4d44717b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog.product.variation

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java`

## Types
- `PersistableProductVariation` (class) extends [com.salesmanager.shop.model.catalog.product.variation.ProductVariationEntity](/modules/com.salesmanager.shop.model.catalog.product.variation.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:8`
- `ProductVariationEntity` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:5`
- `ReadableProductVariation` (class) extends [com.salesmanager.shop.model.catalog.product.variation.ProductVariationEntity](/modules/com.salesmanager.shop.model.catalog.product.variation.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:6`

## Fields
- `PersistableProductVariation.option: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:14`
- `PersistableProductVariation.optionValue: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:15`
- `ProductVariationEntity.code: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:11`
- `ProductVariationEntity.date: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:12`
- `ProductVariationEntity.sortOrder: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:20`
- `ProductVariationEntity.defaultValue: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:22`
- `ReadableProductVariation.option: ReadableProductOption` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:13`
- `ReadableProductVariation.optionValue: ReadableProductOptionValue` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:14`

## Functions and methods
- `PersistableProductVariation.getOption() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:16`
- `PersistableProductVariation.setOption(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:19`
- `PersistableProductVariation.getOptionValue() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:22`
- `PersistableProductVariation.setOptionValue(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/PersistableProductVariation.java:25`
- `ProductVariationEntity.getCode() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:13`
- `ProductVariationEntity.setCode(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:16`
- `ProductVariationEntity.getSortOrder() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:23`
- `ProductVariationEntity.setSortOrder(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:26`
- `ProductVariationEntity.isDefaultValue() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:29`
- `ProductVariationEntity.setDefaultValue(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:32`
- `ProductVariationEntity.getDate() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:35`
- `ProductVariationEntity.setDate(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ProductVariationEntity.java:38`
- `ReadableProductVariation.getOption() -> ReadableProductOption` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:15`
- `ReadableProductVariation.setOption(ReadableProductOption) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:18`
- `ReadableProductVariation.getOptionValue() -> ReadableProductOptionValue` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:21`
- `ReadableProductVariation.setOptionValue(ReadableProductOptionValue) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:24`

## Depends on
- [com.salesmanager.shop.model.catalog.product.attribute.ReadableProductOption](/modules/com.salesmanager.shop.model.catalog.product.attribute.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:13`
- [com.salesmanager.shop.model.catalog.product.attribute.ReadableProductOptionValue](/modules/com.salesmanager.shop.model.catalog.product.attribute.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/variation/ReadableProductVariation.java:14`
