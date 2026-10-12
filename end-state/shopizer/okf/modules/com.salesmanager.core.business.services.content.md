---
type: Code Module
title: "com.salesmanager.core.business.services.content"
description: "com.salesmanager.core.business.services.content: ContentServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java"
    sha256: "34ba9fb8e4c56d02f0819bc5dca01cc06b2646dbb7c7b5ccb0f6a805151157cf"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java"
    sha256: "236979b88bff924508c69456e9d51edfaaef8d47378e68c9931644ad5782825a"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.content

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java`

## Types
- `ContentService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:31`
- `ContentServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:37`

## Fields
- `ContentServiceImpl.LOG: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:40`
- `ContentServiceImpl.contentRepository: ContentRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:42`
- `ContentServiceImpl.pageContentRepository: PageContentRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:45`
- `ContentServiceImpl.contentFileManager: StaticContentFileManager` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:49`

## Functions and methods
- `ContentService.listByType(ContentType, MerchantStore, Language) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:35`
- `ContentService.listByType(List<ContentType>, MerchantStore, Language) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:38`
- `ContentService.getByCode(String, MerchantStore) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:41`
- `ContentService.saveOrUpdate(Content) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:44`
- `ContentService.exists(String, ContentType, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:47`
- `ContentService.getByCode(String, MerchantStore, Language) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:49`
- `ContentService.getById(Long, MerchantStore, Language) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:52`
- `ContentService.getById(Long, MerchantStore) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:55`
- `ContentService.addContentFile(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:66`
- `ContentService.addContentFiles(String, List<InputContentFile>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:78`
- `ContentService.removeFile(String, FileContentType, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:89`
- `ContentService.removeFile(String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:97`
- `ContentService.removeFiles(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:106`
- `ContentService.renameFile(String, FileContentType, Optional<String>, String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:115`
- `ContentService.getContentFile(String, FileContentType, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:127`
- `ContentService.getContentFiles(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:138`
- `ContentService.getContentFilesNames(String, FileContentType) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:142`
- `ContentService.addLogo(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:151`
- `ContentService.addOptionImage(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:160`
- `ContentService.listByType(List<ContentType>, MerchantStore) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:165`
- `ContentService.listByType(ContentType, MerchantStore, int, int) -> Page<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:168`
- `ContentService.listByType(ContentType, MerchantStore, Language, int, int) -> Page<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:171`
- `ContentService.listNameByType(List<ContentType>, MerchantStore, Language) -> List<ContentDescription>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:174`
- `ContentService.getByLanguage(Long, Language) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:177`
- `ContentService.getBySeUrl(MerchantStore, String) -> ContentDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:179`
- `ContentService.getByCodeLike(ContentType, String, MerchantStore, Language) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:190`
- `ContentService.addFolder(MerchantStore, Optional<String>, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:192`
- `ContentService.listFolders(MerchantStore, Optional<String>) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:194`
- `ContentService.removeFolder(MerchantStore, Optional<String>, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentService.java:196`
- `ContentServiceImpl.listByType(ContentType, MerchantStore, Language) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:58`
- `ContentServiceImpl.delete(Content) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:65`
- `ContentServiceImpl.getByLanguage(Long, Language) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:73`
- `ContentServiceImpl.listByType(List<ContentType>, MerchantStore, Language) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:78`
- `ContentServiceImpl.listNameByType(List<ContentType>, MerchantStore, Language) -> List<ContentDescription>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:91`
- `ContentServiceImpl.listByType(List<ContentType>, MerchantStore) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:98`
- `ContentServiceImpl.getByCode(String, MerchantStore) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:104`
- `ContentServiceImpl.getById(Long) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:111`
- `ContentServiceImpl.saveOrUpdate(Content) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:116`
- `ContentServiceImpl.getByCode(String, MerchantStore, Language) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:128`
- `ContentServiceImpl.addContentFile(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:146`
- `ContentServiceImpl.addLogo(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:171`
- `ContentServiceImpl.addOptionImage(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:182`
- `ContentServiceImpl.addImage(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:192`
- `ContentServiceImpl.addFile(String, InputContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:218`
- `ContentServiceImpl.addContentFiles(String, List<InputContentFile>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:258`
- `ContentServiceImpl.removeFile(String, FileContentType, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:296`
- `ContentServiceImpl.removeFile(String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:310`
- `ContentServiceImpl.removeFiles(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:334`
- `ContentServiceImpl.getContentFile(String, FileContentType, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:358`
- `ContentServiceImpl.getContentFiles(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:383`
- `ContentServiceImpl.getContentFilesNames(String, FileContentType) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:402`
- `ContentServiceImpl.getBySeUrl(MerchantStore, String) -> ContentDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:422`
- `ContentServiceImpl.getByCodeLike(ContentType, String, MerchantStore, Language) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:427`
- `ContentServiceImpl.getById(Long, MerchantStore, Language) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:432`
- `ContentServiceImpl.getById(Long, MerchantStore) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:446`
- `ContentServiceImpl.addFolder(MerchantStore, Optional<String>, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:459`
- `ContentServiceImpl.listFolders(MerchantStore, Optional<String>) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:474`
- `ContentServiceImpl.removeFolder(MerchantStore, Optional<String>, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:481`
- `ContentServiceImpl.isValidLinuxDirectory(String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:490`
- `ContentServiceImpl.renameFile(String, FileContentType, Optional<String>, String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:495`
- `ContentServiceImpl.listByType(ContentType, MerchantStore, int, int) -> Page<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:522`
- `ContentServiceImpl.listByType(ContentType, MerchantStore, Language, int, int) -> Page<Content>` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:529`
- `ContentServiceImpl.exists(String, ContentType, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:536`

## Depends on
- [com.salesmanager.core.business.modules.cms.content.StaticContentFileManager](/modules/com.salesmanager.core.business.modules.cms.content.md) `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:48`
- [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:42`
- [com.salesmanager.core.business.repositories.content.PageContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:44`

## Calls
- `ContentServiceImpl.addContentFiles` calls [com.salesmanager.core.business.modules.cms.content.FilePut](/modules/com.salesmanager.core.business.modules.cms.content.md) `FilePut.addFiles` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:270`
- `ContentServiceImpl.addFile` calls [com.salesmanager.core.business.modules.cms.content.FilePut](/modules/com.salesmanager.core.business.modules.cms.content.md) `FilePut.addFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:228`
- `ContentServiceImpl.addFolder` calls [com.salesmanager.core.business.modules.cms.content.FolderPut](/modules/com.salesmanager.core.business.modules.cms.content.md) `FolderPut.addFolder` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:469`
- `ContentServiceImpl.addImage` calls [com.salesmanager.core.business.modules.cms.content.FilePut](/modules/com.salesmanager.core.business.modules.cms.content.md) `FilePut.addFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:199`
- `ContentServiceImpl.exists` calls [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepository.findByCodeAndType` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:538`
- `ContentServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:107`
- `ContentServiceImpl.getByCodeLike` calls [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepository.findByCodeLike` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:429`
- `ContentServiceImpl.getById` calls [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:113`
- `ContentServiceImpl.getByLanguage` calls [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepository.findByIdAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:75`
- `ContentServiceImpl.listByType` calls [com.salesmanager.core.business.repositories.content.ContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepository.findByType`, `ContentRepository.findByTypes` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:62`
- `ContentServiceImpl.listByType` calls [com.salesmanager.core.business.repositories.content.PageContentRepository](/modules/com.salesmanager.core.business.repositories.content.md) `PageContentRepository.findByContentType` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:526`
- `ContentServiceImpl.listFolders` calls [com.salesmanager.core.business.modules.cms.content.FolderList](/modules/com.salesmanager.core.business.modules.cms.content.md) `FolderList.listFolders` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:478`
- `ContentServiceImpl.listNameByType` calls [com.salesmanager.core.business.repositories.content.ContentRepositoryCustom](/modules/com.salesmanager.core.business.repositories.content.md) `ContentRepositoryCustom.listNameByType` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:95`
- `ContentServiceImpl.removeFile` calls [com.salesmanager.core.business.modules.cms.content.FileRemove](/modules/com.salesmanager.core.business.modules.cms.content.md) `FileRemove.removeFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:306`
- `ContentServiceImpl.removeFile` calls [com.salesmanager.core.model.content.FileContentType](/modules/com.salesmanager.core.model.content.md) `FileContentType.valueOf` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:322`
- `ContentServiceImpl.removeFiles` calls [com.salesmanager.core.business.modules.cms.content.FileRemove](/modules/com.salesmanager.core.business.modules.cms.content.md) `FileRemove.removeFiles` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:341`
- `ContentServiceImpl.removeFolder` calls [com.salesmanager.core.business.modules.cms.content.FolderRemove](/modules/com.salesmanager.core.business.modules.cms.content.md) `FolderRemove.removeFolder` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:486`
- `ContentServiceImpl.renameFile` calls [com.salesmanager.core.business.modules.cms.content.FilePut](/modules/com.salesmanager.core.business.modules.cms.content.md) `FilePut.addFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:518`
- `ContentServiceImpl.renameFile` calls [com.salesmanager.core.business.modules.cms.content.FileRemove](/modules/com.salesmanager.core.business.modules.cms.content.md) `FileRemove.removeFile` `sm-core/src/main/java/com/salesmanager/core/business/services/content/ContentServiceImpl.java:509`
