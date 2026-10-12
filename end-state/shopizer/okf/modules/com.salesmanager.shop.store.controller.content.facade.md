---
type: Code Module
title: "com.salesmanager.shop.store.controller.content.facade"
description: "com.salesmanager.shop.store.controller.content.facade: getContentFolder, absolutePath, delete, delete"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java"
    sha256: "884ba72bbf70aa9c29f389bed17ffccef0f5aefe807a598e7864d8d1f7f96796"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.content.facade

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java`

## Types
- `ContentFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:29`

## Functions and methods
- `ContentFacade.getContentFolder(String, MerchantStore) -> ContentFolder` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:32`
- `ContentFacade.absolutePath(MerchantStore, String) -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:40`
- `ContentFacade.delete(MerchantStore, String, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:47`
- `ContentFacade.delete(MerchantStore, Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:54`
- `ContentFacade.getContentPages(MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentPage>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:65`
- `ContentFacade.getContentPage(String, MerchantStore, Language) -> ReadableContentPage` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:76`
- `ContentFacade.getContentPageByName(String, MerchantStore, Language) -> ReadableContentPage` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:86`
- `ContentFacade.getContentBox(String, MerchantStore, Language) -> ReadableContentBox` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:97`
- `ContentFacade.codeExist(String, String, MerchantStore) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:106`
- `ContentFacade.getContentBoxes(ContentType, String, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentBox>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:117`
- `ContentFacade.getContentBoxes(ContentType, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentBox>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:119`
- `ContentFacade.addContentFile(ContentFile, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:121`
- `ContentFacade.addContentFiles(List<ContentFile>, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:128`
- `ContentFacade.saveContentPage(PersistableContentPage, MerchantStore, Language) -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:136`
- `ContentFacade.updateContentPage(Long, PersistableContentPage, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:138`
- `ContentFacade.deleteContent(Long, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:140`
- `ContentFacade.saveContentBox(PersistableContentBox, MerchantStore, Language) -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:148`
- `ContentFacade.updateContentBox(Long, PersistableContentBox, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:150`
- `ContentFacade.getContent(String, MerchantStore, Language) -> ReadableContentFull` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:153`
- `ContentFacade.getContents(Optional<String>, MerchantStore, Language) -> List<ReadableContentEntity>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:163`
- `ContentFacade.renameFile(MerchantStore, FileContentType, String, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:172`
- `ContentFacade.download(MerchantStore, FileContentType, String) -> OutputContentFile` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/content/facade/ContentFacade.java:181`
