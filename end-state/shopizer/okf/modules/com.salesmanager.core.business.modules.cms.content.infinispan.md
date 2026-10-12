---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.content.infinispan"
description: "com.salesmanager.core.business.modules.cms.content.infinispan: CmsStaticContentFileManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java"
    sha256: "8470be8101ee7a1e59f5c45b818887d179cb61c25b7da75fb213eabb40fe60d2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.content.infinispan

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java`

## Types
- `CmsStaticContentFileManagerImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:39`

## Fields
- `CmsStaticContentFileManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:47`
- `CmsStaticContentFileManagerImpl.fileManager: CmsStaticContentFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:48`
- `CmsStaticContentFileManagerImpl.ROOT_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:49`
- `CmsStaticContentFileManagerImpl.rootName: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:51`
- `CmsStaticContentFileManagerImpl.cacheManager: CacheManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:53`

## Functions and methods
- `CmsStaticContentFileManagerImpl.stopFileManager() -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:55`
- `CmsStaticContentFileManagerImpl.init() -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:65`
- `CmsStaticContentFileManagerImpl.getInstance() -> CmsStaticContentFileManagerImpl` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:73`
- `CmsStaticContentFileManagerImpl.addFile(String, Optional<String>, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:108`
- `CmsStaticContentFileManagerImpl.addFiles(String, Optional<String>, List<InputContentFile>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:156`
- `CmsStaticContentFileManagerImpl.getFile(String, Optional<String>, FileContentType, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:197`
- `CmsStaticContentFileManagerImpl.getFiles(String, Optional<String>, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:236`
- `CmsStaticContentFileManagerImpl.removeFile(String, FileContentType, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:280`
- `CmsStaticContentFileManagerImpl.removeFiles(String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:305`
- `CmsStaticContentFileManagerImpl.getNode(String) -> Node<String, Object>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:328`
- `CmsStaticContentFileManagerImpl.getNodePath(String, FileContentType) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:349`
- `CmsStaticContentFileManagerImpl.getFolder(String, String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:365`
- `CmsStaticContentFileManagerImpl.getCacheManager() -> CacheManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:377`
- `CmsStaticContentFileManagerImpl.setCacheManager(CacheManager) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:381`
- `CmsStaticContentFileManagerImpl.getFileNames(String, Optional<String>, FileContentType) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:393`
- `CmsStaticContentFileManagerImpl.setRootName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:419`
- `CmsStaticContentFileManagerImpl.getRootName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:423`
- `CmsStaticContentFileManagerImpl.addFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:427`
- `CmsStaticContentFileManagerImpl.removeFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:460`
- `CmsStaticContentFileManagerImpl.listFolders(String, Optional<String>) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:466`
- `CmsStaticContentFileManagerImpl.getCmsManager() -> CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:472`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.CacheManager](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:53`

## Calls
- `CmsStaticContentFileManagerImpl.getNodePath` calls [com.salesmanager.core.model.content.FileContentType](/modules/com.salesmanager.core.model.content.md) `FileContentType.name` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/infinispan/CmsStaticContentFileManagerImpl.java:352`
