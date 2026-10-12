---
type: Code Module
title: "com.salesmanager.shop.store.facade.content"
description: "com.salesmanager.shop.store.facade.content: ContentFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java"
    sha256: "b22604edf3f12341516598db7e66e90411f060ef7dd7f77265a1fd988de990d1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.content

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java`

## Types
- `ContentFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:54`

## Fields
- `ContentFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:57`
- `ContentFacadeImpl.FILE_CONTENT_DELIMETER: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:59`
- `ContentFacadeImpl.contentService: ContentService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:62`
- `ContentFacadeImpl.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:65`
- `ContentFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:69`
- `ContentFacadeImpl.fileUtils: FilePathUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:72`

## Functions and methods
- `ContentFacadeImpl.getContentFolder(String, MerchantStore) -> ContentFolder` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:74`
- `ContentFacadeImpl.convertToContentImage(String, MerchantStore) -> ContentImage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:97`
- `ContentFacadeImpl.absolutePath(MerchantStore, String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:105`
- `ContentFacadeImpl.delete(MerchantStore, String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:111`
- `ContentFacadeImpl.getContentPages(MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentPage>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:123`
- `ContentFacadeImpl.contentDescriptionToReadableContent(MerchantStore, Content, ContentDescription) -> ReadableContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:152`
- `ContentFacadeImpl.convertContentToReadableContentFull(MerchantStore, Language, Content) -> ReadableContentFull` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:174`
- `ContentFacadeImpl.convertContentToReadableContentEntity(MerchantStore, Language, Content) -> ReadableContentEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:198`
- `ContentFacadeImpl.convertContentPageToContent(MerchantStore, Content, PersistableContentPage) -> Content` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:218`
- `ContentFacadeImpl.convertContentBoxToContent(MerchantStore, Content, PersistableContentBox) -> Content` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:238`
- `ContentFacadeImpl.createContentDescriptionEntitys(MerchantStore, Content, Language) -> List<ContentDescriptionEntity>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:291`
- `ContentFacadeImpl.create(ContentDescription) -> ContentDescriptionEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:311`
- `ContentFacadeImpl.buildDescriptions(Content, List<com.salesmanager.shop.model.content.common.ContentDescription>) -> List<ContentDescription>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:349`
- `ContentFacadeImpl.setContentDescriptionToContentModel(Content, ContentDescription, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:396`
- `ContentFacadeImpl.getContentPage(String, MerchantStore, Language) -> ReadableContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:414`
- `ContentFacadeImpl.getContentBoxes(ContentType, String, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentBox>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:438`
- `ContentFacadeImpl.getContentBoxes(ContentType, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentBox>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:456`
- `ContentFacadeImpl.addContentFile(ContentFile, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:486`
- `ContentFacadeImpl.getFileContentType(String) -> FileContentType` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:510`
- `ContentFacadeImpl.convertContentToReadableContentBox(MerchantStore, Language, Content) -> ReadableContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:519`
- `ContentFacadeImpl.setDescription(Content, ReadableContentBox, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:545`
- `ContentFacadeImpl.convertContentToReadableContentPage(MerchantStore, Language, Content) -> ReadableContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:557`
- `ContentFacadeImpl.contentDescription(ContentDescription) -> com.salesmanager.shop.model.content.common.ContentDescription` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:585`
- `ContentFacadeImpl.convertContentToReadableLegacyContentBox(MerchantStore, Language, Content) -> ReadableContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:598`
- `ContentFacadeImpl.findAppropriateContentDescription(List<ContentDescription>, Language) -> Optional<ContentDescription>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:615`
- `ContentFacadeImpl.getContentBox(String, MerchantStore, Language) -> ReadableContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:621`
- `ContentFacadeImpl.fixContentDescription(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:686`
- `ContentFacadeImpl.saveContentPage(PersistableContentPage, MerchantStore, Language) -> Long` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:693`
- `ContentFacadeImpl.saveContentBox(PersistableContentBox, MerchantStore, Language) -> Long` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:716`
- `ContentFacadeImpl.addContentFiles(List<ContentFile>, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:740`
- `ContentFacadeImpl.delete(MerchantStore, Long) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:748`
- `ContentFacadeImpl.getContent(String, MerchantStore, Language) -> ReadableContentFull` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:769`
- `ContentFacadeImpl.getContents(Optional<String>, MerchantStore, Language) -> List<ReadableContentEntity>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:788`
- `ContentFacadeImpl.getContentPageByName(String, MerchantStore, Language) -> ReadableContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:810`
- `ContentFacadeImpl.renameFile(MerchantStore, FileContentType, String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:828`
- `ContentFacadeImpl.download(MerchantStore, FileContentType, String) -> OutputContentFile` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:839`
- `ContentFacadeImpl.updateContentPage(Long, PersistableContentPage, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:852`
- `ContentFacadeImpl.deleteContent(Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:878`
- `ContentFacadeImpl.updateContentBox(Long, PersistableContentBox, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:900`
- `ContentFacadeImpl.codeExist(String, String, MerchantStore) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:925`

## Depends on
- [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:61`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:64`
- [com.salesmanager.shop.utils.FilePathUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:71`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:67`

## Calls
- `ContentFacadeImpl.absolutePath` calls [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `ImageFilePath.buildStaticImageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:108`
- `ContentFacadeImpl.addContentFile` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.addContentFile` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:503`
- `ContentFacadeImpl.codeExist` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.exists` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:927`
- `ContentFacadeImpl.codeExist` calls [com.salesmanager.core.model.content.ContentType](/modules/com.salesmanager.core.model.content.md) `ContentType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:927`
- `ContentFacadeImpl.contentDescriptionToReadableContent` calls [com.salesmanager.shop.utils.FilePathUtils](/modules/com.salesmanager.shop.utils.md) `FilePathUtils.buildStaticFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:169`
- `ContentFacadeImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:762`
- `ContentFacadeImpl.delete` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.removeFile` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:117`
- `ContentFacadeImpl.delete` calls [com.salesmanager.core.model.content.FileContentType](/modules/com.salesmanager.core.model.content.md) `FileContentType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:116`
- `ContentFacadeImpl.deleteContent` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:892`
- `ContentFacadeImpl.getContentBoxes` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.listByType` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:466`
- `ContentFacadeImpl.getContentPages` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.listByType` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:133`
- `ContentFacadeImpl.getContents` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.listByType` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:800`
- `ContentFacadeImpl.renameFile` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.renameFile` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:832`
- `ContentFacadeImpl.saveContentBox` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:732`
- `ContentFacadeImpl.saveContentPage` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:709`
- `ContentFacadeImpl.updateContentBox` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:917`
- `ContentFacadeImpl.updateContentPage` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/content/ContentFacadeImpl.java:870`
