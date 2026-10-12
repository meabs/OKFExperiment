---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.product.gcp"
description: "com.salesmanager.core.business.modules.cms.product.gcp: GCPProductContentFileManager"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java"
    sha256: "25f3963158fd3e8f86adf55ae334f76e0f567de6708a2664bd692682af695baa"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.product.gcp

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java`

## Types
- `GCPProductContentFileManager` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:44`

## Fields
- `GCPProductContentFileManager.gcpAssetsManager: CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:48`
- `GCPProductContentFileManager.DEFAULT_BUCKET_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:50`
- `GCPProductContentFileManager.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:52`
- `GCPProductContentFileManager.SMALL: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:56`
- `GCPProductContentFileManager.LARGE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:57`

## Functions and methods
- `GCPProductContentFileManager.getProductImage(String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:65`
- `GCPProductContentFileManager.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:75`
- `GCPProductContentFileManager.getProductImage(ProductImage) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:117`
- `GCPProductContentFileManager.getImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:124`
- `GCPProductContentFileManager.getImages(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:133`
- `GCPProductContentFileManager.addProductImage(ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:178`
- `GCPProductContentFileManager.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:209`
- `GCPProductContentFileManager.removeProductImages(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:232`
- `GCPProductContentFileManager.removeImages(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:253`
- `GCPProductContentFileManager.bucketName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:271`
- `GCPProductContentFileManager.bucketExists(Storage, String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:279`
- `GCPProductContentFileManager.createBucket(Storage, String) -> Bucket` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:287`
- `GCPProductContentFileManager.filePath(String, String, FileContentType) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:291`
- `GCPProductContentFileManager.filePath(String, String, String, String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:308`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.CMSManager](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:47`

## Calls
- `GCPProductContentFileManager.filePath` calls [com.salesmanager.core.model.content.FileContentType](/modules/com.salesmanager.core.model.content.md) `FileContentType.name` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:298`
- `GCPProductContentFileManager.getProductImage` calls [com.salesmanager.core.model.catalog.product.file.ProductImageSize](/modules/com.salesmanager.core.model.catalog.product.file.md) `ProductImageSize.name` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/gcp/GCPProductContentFileManager.java:88`
