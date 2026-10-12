---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.content.local"
description: "com.salesmanager.core.business.modules.cms.content.local: CmsStaticContentFileManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java"
    sha256: "44e58489052cb3c2847b2edbb816e35c45712532e293e062b66fda47bc064dcc"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.content.local

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java`

## Types
- `CmsStaticContentFileManagerImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:37`

## Fields
- `CmsStaticContentFileManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:43`
- `CmsStaticContentFileManagerImpl.fileManager: CmsStaticContentFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:44`
- `CmsStaticContentFileManagerImpl.ROOT_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:45`
- `CmsStaticContentFileManagerImpl.ROOT_CONTAINER: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:47`
- `CmsStaticContentFileManagerImpl.rootName: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:49`
- `CmsStaticContentFileManagerImpl.cacheManager: LocalCacheManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:51`

## Functions and methods
- `CmsStaticContentFileManagerImpl.init() -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:53`
- `CmsStaticContentFileManagerImpl.getInstance() -> CmsStaticContentFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:61`
- `CmsStaticContentFileManagerImpl.addFile(String, Optional<String>, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:96`
- `CmsStaticContentFileManagerImpl.addFiles(String, Optional<String>, List<InputContentFile>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:179`
- `CmsStaticContentFileManagerImpl.getFile(String, Optional<String>, FileContentType, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:250`
- `CmsStaticContentFileManagerImpl.getFiles(String, Optional<String>, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:258`
- `CmsStaticContentFileManagerImpl.removeFile(String, FileContentType, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:266`
- `CmsStaticContentFileManagerImpl.removeFiles(String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:290`
- `CmsStaticContentFileManagerImpl.getFileNames(String, Optional<String>, FileContentType) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:319`
- `CmsStaticContentFileManagerImpl.setRootName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:370`
- `CmsStaticContentFileManagerImpl.getRootName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:374`
- `CmsStaticContentFileManagerImpl.buildRootPath() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:378`
- `CmsStaticContentFileManagerImpl.createDirectoryIfNorExist(Path) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:384`
- `CmsStaticContentFileManagerImpl.getCacheManager() -> LocalCacheManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:391`
- `CmsStaticContentFileManagerImpl.setCacheManager(LocalCacheManagerImpl) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:395`
- `CmsStaticContentFileManagerImpl.addFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:399`
- `CmsStaticContentFileManagerImpl.buildMerchantPath(String) -> Path` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:427`
- `CmsStaticContentFileManagerImpl.removeFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:444`
- `CmsStaticContentFileManagerImpl.listFolders(String, Optional<String>) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:473`
- `CmsStaticContentFileManagerImpl.getCmsManager() -> CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:479`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.LocalCacheManagerImpl](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:51`

## Calls
- `CmsStaticContentFileManagerImpl.getFileNames` calls [com.salesmanager.core.model.content.FileContentType](/modules/com.salesmanager.core.model.content.md) `FileContentType.name` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/local/CmsStaticContentFileManagerImpl.java:341`
