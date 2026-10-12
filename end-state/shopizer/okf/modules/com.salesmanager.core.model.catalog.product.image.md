---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.image"
description: "com.salesmanager.core.model.catalog.product.image: ProductImage, ProductImageDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java"
    sha256: "b1a565f07a3e7242a16fe28b9d9949fc1c6950dc055df6a16cdc9fc5555a7496"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java"
    sha256: "c98ed255cdec38a6bf3892dfee7967e2cc953f99e9653611765548f97052ad55"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.image

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java`

## Types
- `ProductImage` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:24`
- `ProductImageDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:14`

## Fields
- `ProductImage.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:33`
- `ProductImage.descriptions: List<ProductImageDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:36`
- `ProductImage.productImage: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:40`
- `ProductImage.defaultImage: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:43`
- `ProductImage.imageType: int` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:49`
- `ProductImage.productImageUrl: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:55`
- `ProductImage.imageCrop: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:59`
- `ProductImage.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:63`
- `ProductImage.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:66`
- `ProductImage.image: InputStream` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:70`
- `ProductImageDescription.productImage: ProductImage` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:28`
- `ProductImageDescription.altTag: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:31`

## Functions and methods
- `ProductImage.getProductImage() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:77`
- `ProductImage.setProductImage(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:81`
- `ProductImage.isDefaultImage() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:85`
- `ProductImage.setDefaultImage(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:89`
- `ProductImage.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:93`
- `ProductImage.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:97`
- `ProductImage.getImageType() -> int` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:101`
- `ProductImage.setImageType(int) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:105`
- `ProductImage.isImageCrop() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:109`
- `ProductImage.setImageCrop(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:113`
- `ProductImage.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:117`
- `ProductImage.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:122`
- `ProductImage.getProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:127`
- `ProductImage.setProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:131`
- `ProductImage.setDescriptions(List<ProductImageDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:135`
- `ProductImage.getDescriptions() -> List<ProductImageDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:139`
- `ProductImage.getImage() -> InputStream` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:143`
- `ProductImage.setImage(InputStream) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:147`
- `ProductImage.getProductImageUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:151`
- `ProductImage.setProductImageUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:155`
- `ProductImageDescription.getProductImage() -> ProductImage` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:33`
- `ProductImageDescription.setProductImage(ProductImage) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:37`
- `ProductImageDescription.getAltTag() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:41`
- `ProductImageDescription.setAltTag(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImageDescription.java:45`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/image/ProductImage.java:61`
