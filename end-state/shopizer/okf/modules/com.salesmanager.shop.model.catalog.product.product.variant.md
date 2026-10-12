---
type: Code Module
title: "com.salesmanager.shop.model.catalog.product.product.variant"
description: "com.salesmanager.shop.model.catalog.product.product.variant: PersistableProductVariant, ProductVariant, ReadableProductVariant"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java"
    sha256: "1c658b97ec06e6ef0562f9e49c4ac0f990bd454ffa47b580c94651589cc17225"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java"
    sha256: "d8cb2d3cd3cf9009eda0d1cd709d463a1ba99b0fcb8ba62ba6d4503afcdec807"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java"
    sha256: "17791605b03910e83c4b5598769edcc2448653e5c582ba51579641e88ce18313"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog.product.product.variant

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java`

## Types
- `PersistableProductVariant` (class) extends [com.salesmanager.shop.model.catalog.product.product.variant.ProductVariant](/modules/com.salesmanager.shop.model.catalog.product.product.variant.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:5`
- `ProductVariant` (class) extends [com.salesmanager.shop.model.catalog.product.Product](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:5`
- `ReadableProductVariant` (class) extends [com.salesmanager.shop.model.catalog.product.product.variant.ProductVariant](/modules/com.salesmanager.shop.model.catalog.product.product.variant.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:10`

## Fields
- `PersistableProductVariant.variation: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:9`
- `PersistableProductVariant.variationValue: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:10`
- `PersistableProductVariant.variationCode: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:12`
- `PersistableProductVariant.variationValueCode: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:13`
- `PersistableProductVariant.inventory: PersistableProductInventory` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:15`
- `ProductVariant.store: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:8`
- `ProductVariant.productId: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:10`
- `ProductVariant.sku: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:11`
- `ProductVariant.available: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:13`
- `ProductVariant.dateAvailable: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:14`
- `ProductVariant.sortOrder: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:15`
- `ProductVariant.defaultSelection: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:17`
- `ReadableProductVariant.variation: ReadableProductVariation` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:14`
- `ReadableProductVariant.variationValue: ReadableProductVariation` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:15`
- `ReadableProductVariant.code: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:16`
- `ReadableProductVariant.images: List<ReadableImage>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:17`
- `ReadableProductVariant.inventory: List<ReadableInventory>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:18`

## Functions and methods
- `PersistableProductVariant.getVariation() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:17`
- `PersistableProductVariant.setVariation(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:21`
- `PersistableProductVariant.getVariationValue() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:25`
- `PersistableProductVariant.setVariationValue(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:29`
- `PersistableProductVariant.getVariationCode() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:33`
- `PersistableProductVariant.setVariationCode(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:37`
- `PersistableProductVariant.getVariationValueCode() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:41`
- `PersistableProductVariant.setVariationValueCode(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:45`
- `PersistableProductVariant.getInventory() -> PersistableProductInventory` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:49`
- `PersistableProductVariant.setInventory(PersistableProductInventory) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:53`
- `ProductVariant.getStore() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:19`
- `ProductVariant.setStore(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:22`
- `ProductVariant.isDefaultSelection() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:25`
- `ProductVariant.setDefaultSelection(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:28`
- `ProductVariant.getProductId() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:31`
- `ProductVariant.setProductId(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:34`
- `ProductVariant.getSku() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:37`
- `ProductVariant.setSku(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:40`
- `ProductVariant.isAvailable() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:43`
- `ProductVariant.setAvailable(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:46`
- `ProductVariant.getDateAvailable() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:49`
- `ProductVariant.setDateAvailable(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:52`
- `ProductVariant.getSortOrder() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:55`
- `ProductVariant.setSortOrder(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ProductVariant.java:58`
- `ReadableProductVariant.getVariation() -> ReadableProductVariation` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:20`
- `ReadableProductVariant.setVariation(ReadableProductVariation) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:23`
- `ReadableProductVariant.getVariationValue() -> ReadableProductVariation` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:26`
- `ReadableProductVariant.setVariationValue(ReadableProductVariation) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:29`
- `ReadableProductVariant.getImages() -> List<ReadableImage>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:32`
- `ReadableProductVariant.setImages(List<ReadableImage>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:35`
- `ReadableProductVariant.getCode() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:38`
- `ReadableProductVariant.setCode(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:41`
- `ReadableProductVariant.getInventory() -> List<ReadableInventory>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:44`
- `ReadableProductVariant.setInventory(List<ReadableInventory>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:47`

## Depends on
- [com.salesmanager.shop.model.catalog.product.ReadableImage](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:17`
- [com.salesmanager.shop.model.catalog.product.inventory.ReadableInventory](/modules/com.salesmanager.shop.model.catalog.product.inventory.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:18`
- [com.salesmanager.shop.model.catalog.product.product.PersistableProductInventory](/modules/com.salesmanager.shop.model.catalog.product.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/PersistableProductVariant.java:15`
- [com.salesmanager.shop.model.catalog.product.variation.ReadableProductVariation](/modules/com.salesmanager.shop.model.catalog.product.variation.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variant/ReadableProductVariant.java:14`
