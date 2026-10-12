---
type: Code Module
title: "com.salesmanager.shop.model.catalog.product.attribute.optionset"
description: "com.salesmanager.shop.model.catalog.product.attribute.optionset: PersistableProductOptionSet, ProductOptionSetEntity, ReadableProductOptionSet"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java"
    sha256: "dc6afaa08ed03d6c37641af86a593232a389f32891bef223cf8e48bd9b53fb79"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java"
    sha256: "d95670252615fb1b06cbc88909c781dce2c556ee3e7b56dc4b2d4aa5d5b22ef2"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java"
    sha256: "762c31adfffa8b97b8ab7866b9c400d4e64b422f345f89de300b3b208d60dc9c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog.product.attribute.optionset

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java`

## Types
- `PersistableProductOptionSet` (class) extends [com.salesmanager.shop.model.catalog.product.attribute.optionset.ProductOptionSetEntity](/modules/com.salesmanager.shop.model.catalog.product.attribute.optionset.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:5`
- `ProductOptionSetEntity` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:5`
- `ReadableProductOptionSet` (class) extends [com.salesmanager.shop.model.catalog.product.attribute.optionset.ProductOptionSetEntity](/modules/com.salesmanager.shop.model.catalog.product.attribute.optionset.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:9`

## Fields
- `PersistableProductOptionSet.optionValues: List<Long>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:12`
- `PersistableProductOptionSet.productTypes: List<Long>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:13`
- `PersistableProductOptionSet.option: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:14`
- `ProductOptionSetEntity.id: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:12`
- `ProductOptionSetEntity.code: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:13`
- `ProductOptionSetEntity.readOnly: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:14`
- `ReadableProductOptionSet.option: ReadableProductOption` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:16`
- `ReadableProductOptionSet.values: List<ReadableProductOptionValue>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:17`
- `ReadableProductOptionSet.productTypes: List<ReadableProductType>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:18`

## Functions and methods
- `PersistableProductOptionSet.getOptionValues() -> List<Long>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:16`
- `PersistableProductOptionSet.setOptionValues(List<Long>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:19`
- `PersistableProductOptionSet.getOption() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:22`
- `PersistableProductOptionSet.setOption(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:25`
- `PersistableProductOptionSet.getProductTypes() -> List<Long>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:28`
- `PersistableProductOptionSet.setProductTypes(List<Long>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/PersistableProductOptionSet.java:31`
- `ProductOptionSetEntity.getId() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:15`
- `ProductOptionSetEntity.setId(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:18`
- `ProductOptionSetEntity.getCode() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:21`
- `ProductOptionSetEntity.setCode(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:24`
- `ProductOptionSetEntity.isReadOnly() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:27`
- `ProductOptionSetEntity.setReadOnly(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ProductOptionSetEntity.java:30`
- `ReadableProductOptionSet.getOption() -> ReadableProductOption` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:20`
- `ReadableProductOptionSet.setOption(ReadableProductOption) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:23`
- `ReadableProductOptionSet.getValues() -> List<ReadableProductOptionValue>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:26`
- `ReadableProductOptionSet.setValues(List<ReadableProductOptionValue>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:29`
- `ReadableProductOptionSet.getProductTypes() -> List<ReadableProductType>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:32`
- `ReadableProductOptionSet.setProductTypes(List<ReadableProductType>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:35`

## Depends on
- [com.salesmanager.shop.model.catalog.product.attribute.ReadableProductOption](/modules/com.salesmanager.shop.model.catalog.product.attribute.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:16`
- [com.salesmanager.shop.model.catalog.product.attribute.ReadableProductOptionValue](/modules/com.salesmanager.shop.model.catalog.product.attribute.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:17`
- [com.salesmanager.shop.model.catalog.product.type.ReadableProductType](/modules/com.salesmanager.shop.model.catalog.product.type.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/attribute/optionset/ReadableProductOptionSet.java:18`
