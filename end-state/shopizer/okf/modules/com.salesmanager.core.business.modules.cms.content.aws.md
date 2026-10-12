---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.content.aws"
description: "com.salesmanager.core.business.modules.cms.content.aws: S3StaticContentAssetsManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java"
    sha256: "83731e0b06a98f03ff6604960b2e70ee20452e39f1b81fc99732412b139aa098"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.content.aws

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java`

## Types
- `S3StaticContentAssetsManagerImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:38`

## Fields
- `S3StaticContentAssetsManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:42`
- `S3StaticContentAssetsManagerImpl.fileManager: S3StaticContentAssetsManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:44`
- `S3StaticContentAssetsManagerImpl.cmsManager: CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:46`

## Functions and methods
- `S3StaticContentAssetsManagerImpl.getInstance() -> S3StaticContentAssetsManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:48`
- `S3StaticContentAssetsManagerImpl.getFile(String, Optional<String>, FileContentType, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:58`
- `S3StaticContentAssetsManagerImpl.getFileNames(String, Optional<String>, FileContentType) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:78`
- `S3StaticContentAssetsManagerImpl.getFiles(String, Optional<String>, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:115`
- `S3StaticContentAssetsManagerImpl.addFile(String, Optional<String>, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:154`
- `S3StaticContentAssetsManagerImpl.addFiles(String, Optional<String>, List<InputContentFile>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:182`
- `S3StaticContentAssetsManagerImpl.removeFile(String, FileContentType, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:195`
- `S3StaticContentAssetsManagerImpl.removeFiles(String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:215`
- `S3StaticContentAssetsManagerImpl.getBucket(String) -> Bucket` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:234`
- `S3StaticContentAssetsManagerImpl.createBucket(String) -> Bucket` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:251`
- `S3StaticContentAssetsManagerImpl.s3Client() -> AmazonS3` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:272`
- `S3StaticContentAssetsManagerImpl.regionName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:287`
- `S3StaticContentAssetsManagerImpl.getCmsManager() -> CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:295`
- `S3StaticContentAssetsManagerImpl.setCmsManager(CMSManager) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:299`
- `S3StaticContentAssetsManagerImpl.addFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:303`
- `S3StaticContentAssetsManagerImpl.removeFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:309`
- `S3StaticContentAssetsManagerImpl.listFolders(String, Optional<String>) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:316`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.CMSManager](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/aws/S3StaticContentAssetsManagerImpl.java:46`
