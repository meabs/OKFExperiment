---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.content.gcp"
description: "com.salesmanager.core.business.modules.cms.content.gcp: GCPDownloadsManagerImpl, GCPStaticContentAssetsManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPDownloadsManagerImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPDownloadsManagerImpl.java"
    sha256: "f459a368bef88a7636f225ce8bdf8015815d1e5a28f48bb099be369ede380a29"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java"
    sha256: "b41c26edc6eb9ddcf4ba5a83804f4d6bff04f0e0e0ff7cbc76366a5895417bfd"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.content.gcp

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPDownloadsManagerImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java`

## Types
- `GCPDownloadsManagerImpl` (class) extends [com.salesmanager.core.business.modules.cms.content.gcp.GCPStaticContentAssetsManagerImpl](/modules/com.salesmanager.core.business.modules.cms.content.gcp.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPDownloadsManagerImpl.java:5`
- `GCPStaticContentAssetsManagerImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:50`

## Fields
- `GCPStaticContentAssetsManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:55`
- `GCPStaticContentAssetsManagerImpl.cmsManager: CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:59`

## Functions and methods
- `GCPStaticContentAssetsManagerImpl.getFile(String, Optional<String>, FileContentType, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:61`
- `GCPStaticContentAssetsManagerImpl.getFileNames(String, Optional<String>, FileContentType) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:80`
- `GCPStaticContentAssetsManagerImpl.getFiles(String, Optional<String>, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:111`
- `GCPStaticContentAssetsManagerImpl.addFile(String, Optional<String>, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:131`
- `GCPStaticContentAssetsManagerImpl.addFiles(String, Optional<String>, List<InputContentFile>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:155`
- `GCPStaticContentAssetsManagerImpl.removeFile(String, FileContentType, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:165`
- `GCPStaticContentAssetsManagerImpl.removeFiles(String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:180`
- `GCPStaticContentAssetsManagerImpl.getCmsManager() -> CMSManager` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:197`
- `GCPStaticContentAssetsManagerImpl.setCmsManager(CMSManager) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:201`
- `GCPStaticContentAssetsManagerImpl.addFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:206`
- `GCPStaticContentAssetsManagerImpl.removeFolder(String, String, Optional<String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:212`
- `GCPStaticContentAssetsManagerImpl.listFolders(String, Optional<String>) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:218`

## Depends on
- [com.salesmanager.core.business.modules.cms.impl.CMSManager](/modules/com.salesmanager.core.business.modules.cms.impl.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/content/gcp/GCPStaticContentAssetsManagerImpl.java:57`
