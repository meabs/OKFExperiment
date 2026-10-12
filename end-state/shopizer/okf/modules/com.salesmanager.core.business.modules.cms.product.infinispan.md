---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.product.infinispan"
description: "com.salesmanager.core.business.modules.cms.product.infinispan: CmsImageFileManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java"
    sha256: "8cb84753eebc272aec312f65a9b98a65de13620ae62ae71f5dc7f1369278b5f4"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.product.infinispan

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java`

## Types
- `CmsImageFileManagerImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:39`

## Fields
- `CmsImageFileManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:46`
- `CmsImageFileManagerImpl.fileManager: CmsImageFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:48`
- `CmsImageFileManagerImpl.ROOT_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:50`
- `CmsImageFileManagerImpl.SMALL: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:52`
- `CmsImageFileManagerImpl.LARGE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:53`
- `CmsImageFileManagerImpl.rootName: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:55`
- `CmsImageFileManagerImpl.cacheManager: CacheManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:57`

## Functions and methods
- `CmsImageFileManagerImpl.stopFileManager() -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:63`
- `CmsImageFileManagerImpl.init() -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:73`
- `CmsImageFileManagerImpl.getInstance() -> CmsImageFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:81`
- `CmsImageFileManagerImpl.addProductImage(ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:101`
- `CmsImageFileManagerImpl.getProductImage(ProductImage) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:148`
- `CmsImageFileManagerImpl.getImages(MerchantStore, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:157`
- `CmsImageFileManagerImpl.getImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:164`
- `CmsImageFileManagerImpl.removeImages(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:224`
- `CmsImageFileManagerImpl.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:250`
- `CmsImageFileManagerImpl.removeProductImages(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:279`
- `CmsImageFileManagerImpl.getImages(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:309`
- `CmsImageFileManagerImpl.getProductImage(String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:368`
- `CmsImageFileManagerImpl.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:375`
- `CmsImageFileManagerImpl.getProductImage(String, String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:381`
- `CmsImageFileManagerImpl.getNode(String) -> Node<String, Object>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:437`
- `CmsImageFileManagerImpl.getCacheManager() -> CacheManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:458`
- `CmsImageFileManagerImpl.setCacheManager(CacheManager) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:462`
- `CmsImageFileManagerImpl.setRootName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:466`
- `CmsImageFileManagerImpl.getRootName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:470`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.CacheManager](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:57`

## Calls
- `CmsImageFileManagerImpl.getProductImage` calls [com.salesmanager.core.model.catalog.product.file.ProductImageSize](/modules/com.salesmanager.core.model.catalog.product.file.md) `ProductImageSize.name` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/infinispan/CmsImageFileManagerImpl.java:378`
