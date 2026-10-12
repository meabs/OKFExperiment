---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.file"
description: "com.salesmanager.core.business.services.catalog.product.file: DigitalProductServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java"
    sha256: "b1b48dc900e7ce270aebeda2b333ce71a913aaedde19fdb941055126f27db047"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java"
    sha256: "81e4cfc4437936d6ed7d39bc22cafb750ffc6bec1111b217997a19bd6ab93354"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.file

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java`

## Types
- `DigitalProductService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java:11`
- `DigitalProductServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:19`

## Fields
- `DigitalProductServiceImpl.digitalProductRepository: DigitalProductRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:24`
- `DigitalProductServiceImpl.productDownloadsFileManager: StaticContentFileManager` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:27`
- `DigitalProductServiceImpl.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:30`

## Functions and methods
- `DigitalProductService.saveOrUpdate(DigitalProduct) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java:13`
- `DigitalProductService.addProductFile(Product, DigitalProduct, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java:15`
- `DigitalProductService.getByProduct(MerchantStore, Product) -> DigitalProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductService.java:20`
- `DigitalProductServiceImpl.addProductFile(Product, DigitalProduct, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:38`
- `DigitalProductServiceImpl.getByProduct(MerchantStore, Product) -> DigitalProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:75`
- `DigitalProductServiceImpl.delete(DigitalProduct) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:80`
- `DigitalProductServiceImpl.saveOrUpdate(DigitalProduct) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:97`

## Depends on
- [com.salesmanager.core.business.modules.cms.content.StaticContentFileManager](/modules/com.salesmanager.core.business.modules.cms.content.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:26`
- [com.salesmanager.core.business.repositories.catalog.product.file.DigitalProductRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.file.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:24`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:29`

## Calls
- `DigitalProductServiceImpl.addProductFile` calls [com.salesmanager.core.business.modules.cms.content.FilePut](/modules/com.salesmanager.core.business.modules.cms.content.md) `FilePut.addFile` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:55`
- `DigitalProductServiceImpl.addProductFile` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:58`
- `DigitalProductServiceImpl.delete` calls [com.salesmanager.core.business.modules.cms.content.FileRemove](/modules/com.salesmanager.core.business.modules.cms.content.md) `FileRemove.removeFile` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:91`
- `DigitalProductServiceImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:93`
- `DigitalProductServiceImpl.getByProduct` calls [com.salesmanager.core.business.repositories.catalog.product.file.DigitalProductRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.file.md) `DigitalProductRepository.findByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:77`
- `DigitalProductServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/file/DigitalProductServiceImpl.java:109`
