---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.product.local"
description: "com.salesmanager.core.business.modules.cms.product.local: CmsImageFileManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java"
    sha256: "89ebaf2cec323abe9a2685946fc5300aab19b9b99d68db6bf100338e8b237889"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.product.local

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java`

## Types
- `CmsImageFileManagerImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:33`

## Fields
- `CmsImageFileManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:41`
- `CmsImageFileManagerImpl.fileManager: CmsImageFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:43`
- `CmsImageFileManagerImpl.ROOT_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:45`
- `CmsImageFileManagerImpl.SMALL: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:47`
- `CmsImageFileManagerImpl.LARGE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:48`
- `CmsImageFileManagerImpl.ROOT_CONTAINER: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:50`
- `CmsImageFileManagerImpl.rootName: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:52`
- `CmsImageFileManagerImpl.cacheManager: LocalCacheManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:54`

## Functions and methods
- `CmsImageFileManagerImpl.init() -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:56`
- `CmsImageFileManagerImpl.getInstance() -> CmsImageFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:64`
- `CmsImageFileManagerImpl.addProductImage(ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:82`
- `CmsImageFileManagerImpl.getProductImage(ProductImage) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:135`
- `CmsImageFileManagerImpl.getImages(MerchantStore, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:144`
- `CmsImageFileManagerImpl.getImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:153`
- `CmsImageFileManagerImpl.removeImages(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:163`
- `CmsImageFileManagerImpl.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:185`
- `CmsImageFileManagerImpl.removeProductImages(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:224`
- `CmsImageFileManagerImpl.getImages(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:247`
- `CmsImageFileManagerImpl.getProductImage(String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:256`
- `CmsImageFileManagerImpl.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:263`
- `CmsImageFileManagerImpl.getProductImage(String, String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:269`
- `CmsImageFileManagerImpl.buildRootPath() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:277`
- `CmsImageFileManagerImpl.createDirectoryIfNorExist(Path) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:284`
- `CmsImageFileManagerImpl.setRootName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:291`
- `CmsImageFileManagerImpl.getRootName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:295`
- `CmsImageFileManagerImpl.getCacheManager() -> LocalCacheManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:299`
- `CmsImageFileManagerImpl.setCacheManager(LocalCacheManagerImpl) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:303`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.LocalCacheManagerImpl](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:54`

## Calls
- `CmsImageFileManagerImpl.getProductImage` calls [com.salesmanager.core.model.catalog.product.file.ProductImageSize](/modules/com.salesmanager.core.model.catalog.product.file.md) `ProductImageSize.name` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/local/CmsImageFileManagerImpl.java:266`
