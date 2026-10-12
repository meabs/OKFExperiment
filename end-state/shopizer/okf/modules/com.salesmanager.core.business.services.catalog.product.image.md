---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.image"
description: "com.salesmanager.core.business.services.catalog.product.image: ProductImageServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java"
    sha256: "44f9e6d863a5255999855178959272eeb9c7ed6c00f52718e1641d698338010f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java"
    sha256: "2b31041efa7decb2fedcd5edf736c9936e421e4c079520100504d4d469a65a9c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.image

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java`

## Types
- `ProductImageService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:16`
- `ProductImageServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:32`

## Fields
- `ProductImageServiceImpl.productImageRepository: ProductImageRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:36`
- `ProductImageServiceImpl.productFileManager: ProductFileManager` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:45`
- `ProductImageServiceImpl.eventPublisher: ApplicationEventPublisher` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:48`

## Functions and methods
- `ProductImageService.addProductImage(Product, ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:27`
- `ProductImageService.getProductImage(ProductImage, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:36`
- `ProductImageService.getProductImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:45`
- `ProductImageService.getProductImage(Long, Long, MerchantStore) -> Optional<ProductImage>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:55`
- `ProductImageService.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:57`
- `ProductImageService.saveOrUpdate(ProductImage) -> ProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:59`
- `ProductImageService.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:71`
- `ProductImageService.addProductImages(Product, List<ProductImage>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:74`
- `ProductImageService.updateProductImage(Product, ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageService.java:77`
- `ProductImageServiceImpl.getById(Long) -> ProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:50`
- `ProductImageServiceImpl.addProductImages(Product, List<ProductImage>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:55`
- `ProductImageServiceImpl.addProductImage(Product, ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:78`
- `ProductImageServiceImpl.saveOrUpdate(ProductImage) -> ProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:111`
- `ProductImageServiceImpl.addProductImageDescription(ProductImage, ProductImageDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:118`
- `ProductImageServiceImpl.getProductImage(ProductImage, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:133`
- `ProductImageServiceImpl.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:153`
- `ProductImageServiceImpl.getProductImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:160`
- `ProductImageServiceImpl.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:165`
- `ProductImageServiceImpl.getProductImage(Long, Long, MerchantStore) -> Optional<ProductImage>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:185`
- `ProductImageServiceImpl.updateProductImage(Product, ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:198`

## Depends on
- [com.salesmanager.core.business.modules.cms.product.ProductFileManager](/modules/com.salesmanager.core.business.modules.cms.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:44`
- [com.salesmanager.core.business.repositories.catalog.product.image.ProductImageRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.image.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:36`

## Calls
- `ProductImageServiceImpl.addProductImage` calls [com.salesmanager.core.business.modules.cms.product.ProductImagePut](/modules/com.salesmanager.core.business.modules.cms.product.md) `ProductImagePut.addProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:87`
- `ProductImageServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.product.image.ProductImageRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.image.md) `ProductImageRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:52`
- `ProductImageServiceImpl.getProductImage` calls [com.salesmanager.core.business.repositories.catalog.product.image.ProductImageRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.image.md) `ProductImageRepository.finById` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:190`
- `ProductImageServiceImpl.removeProductImage` calls [com.salesmanager.core.business.modules.cms.product.ProductImageRemove](/modules/com.salesmanager.core.business.modules.cms.product.md) `ProductImageRemove.removeProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:169`
- `ProductImageServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.repositories.catalog.product.image.ProductImageRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.image.md) `ProductImageRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:114`
- `ProductImageServiceImpl.updateProductImage` calls [com.salesmanager.core.business.repositories.catalog.product.image.ProductImageRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.image.md) `ProductImageRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/image/ProductImageServiceImpl.java:203`
