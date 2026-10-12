---
type: Code Module
title: "com.salesmanager.shop.model.catalog.product.product.variantGroup"
description: "com.salesmanager.shop.model.catalog.product.product.variantGroup: PersistableProductVariantGroup, ProductVariantGroup, ReadableProductVariantGroup"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java"
    sha256: "14b48c537106228414038c24419f6beba02d0f3e2f7c917e035a9117136b2498"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ProductVariantGroup.java"
    sha256: "8482a9611d1fda6405782ce27c837ce6490ccfbf41a8a7d6251adb35aad9097d"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java"
    sha256: "6bbb16675742739cbc4e9206370f0eb7e792f9a57fd43021dc2fc41c91a8a5c6"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog.product.product.variantGroup

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ProductVariantGroup.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java`

## Types
- `PersistableProductVariantGroup` (class) extends [com.salesmanager.shop.model.catalog.product.product.variantGroup.ProductVariantGroup](/modules/com.salesmanager.shop.model.catalog.product.product.variantGroup.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java:5`
- `ProductVariantGroup` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ProductVariantGroup.java:4`
- `ReadableProductVariantGroup` (class) extends [com.salesmanager.shop.model.catalog.product.product.variantGroup.ProductVariantGroup](/modules/com.salesmanager.shop.model.catalog.product.product.variantGroup.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:9`

## Fields
- `PersistableProductVariantGroup.productVariants: List<Long>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java:9`
- `ReadableProductVariantGroup.images: List<ReadableImage>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:13`
- `ReadableProductVariantGroup.productVariants: List<ReadableProductVariant>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:15`

## Functions and methods
- `PersistableProductVariantGroup.getproductVariants() -> List<Long>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java:11`
- `PersistableProductVariantGroup.setproductVariants(List<Long>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/PersistableProductVariantGroup.java:15`
- `ReadableProductVariantGroup.getproductVariants() -> List<ReadableProductVariant>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:16`
- `ReadableProductVariantGroup.setproductVariants(List<ReadableProductVariant>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:19`
- `ReadableProductVariantGroup.getImages() -> List<ReadableImage>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:22`
- `ReadableProductVariantGroup.setImages(List<ReadableImage>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:25`

## Depends on
- [com.salesmanager.shop.model.catalog.product.ReadableImage](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:13`
- [com.salesmanager.shop.model.catalog.product.product.variant.ReadableProductVariant](/modules/com.salesmanager.shop.model.catalog.product.product.variant.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/variantGroup/ReadableProductVariantGroup.java:15`
