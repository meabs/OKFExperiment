---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.product.aws"
description: "com.salesmanager.core.business.modules.cms.product.aws: S3ProductContentFileManager"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java"
    sha256: "3089023a3bdf1028df567f9c2c272dd013651b18bded0daa869a01a312eedd12"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.product.aws

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java`

## Types
- `S3ProductContentFileManager` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:39`

## Fields
- `S3ProductContentFileManager.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:49`
- `S3ProductContentFileManager.fileManager: S3ProductContentFileManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:53`
- `S3ProductContentFileManager.DEFAULT_BUCKET_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:55`
- `S3ProductContentFileManager.DEFAULT_REGION_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:56`
- `S3ProductContentFileManager.ROOT_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:57`
- `S3ProductContentFileManager.UNIX_SEPARATOR: char` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:59`
- `S3ProductContentFileManager.WINDOWS_SEPARATOR: char` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:60`
- `S3ProductContentFileManager.SMALL: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:63`
- `S3ProductContentFileManager.LARGE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:64`
- `S3ProductContentFileManager.cmsManager: CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:66`

## Functions and methods
- `S3ProductContentFileManager.getInstance() -> S3ProductContentFileManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:68`
- `S3ProductContentFileManager.getImages(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:78`
- `S3ProductContentFileManager.removeImages(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:118`
- `S3ProductContentFileManager.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:136`
- `S3ProductContentFileManager.removeProductImages(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:155`
- `S3ProductContentFileManager.getProductImage(String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:173`
- `S3ProductContentFileManager.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:180`
- `S3ProductContentFileManager.getProductImage(ProductImage) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:187`
- `S3ProductContentFileManager.getImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:193`
- `S3ProductContentFileManager.addProductImage(ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:198`
- `S3ProductContentFileManager.getBucket(String) -> Bucket` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:235`
- `S3ProductContentFileManager.createBucket(String) -> Bucket` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:252`
- `S3ProductContentFileManager.s3Client() -> AmazonS3` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:273`
- `S3ProductContentFileManager.bucketName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:281`
- `S3ProductContentFileManager.regionName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:289`
- `S3ProductContentFileManager.nodePath(String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:297`
- `S3ProductContentFileManager.nodePath(String, String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:302`
- `S3ProductContentFileManager.nodePath(String, String, ImageContentFile) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:315`
- `S3ProductContentFileManager.getName(String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:334`
- `S3ProductContentFileManager.indexOfLastSeparator(String) -> int` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:342`
- `S3ProductContentFileManager.getCmsManager() -> CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:353`
- `S3ProductContentFileManager.setCmsManager(CMSManager) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:357`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.CMSManager](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/aws/S3ProductContentFileManager.java:66`
