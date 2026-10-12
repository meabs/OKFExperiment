---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.content"
description: "com.salesmanager.shop.store.api.v1.content: ContentAdministrationApi, FileStatus, ImageFile, ContentApi; 32 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java"
    sha256: "bd8deef1da3ce96a55dc59f7c6e6ef500d1f569235a2e4ea0ddf9c8135bba701"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java"
    sha256: "b750164c5ef3ab94bb12b82f61296cfa9dd8ea75d538527dc2f2a35b742a485f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.content

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java`

## Types
- `ContentAdministrationApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:53`
- `FileStatus` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:270`
- `ImageFile` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:301`
- `ContentApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:57`

## Fields
- `ContentAdministrationApi.DEFAULT_PATH: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:59`
- `ContentAdministrationApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:61`
- `ContentAdministrationApi.contentFacade: ContentFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:64`
- `ContentAdministrationApi.fileNameUtils: FileNameUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:67`
- `ContentAdministrationApi.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:72`
- `FileStatus.success: boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:276`
- `FileStatus.error: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:277`
- `FileStatus.preventRetry: boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:278`
- `ImageFile.url: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:355`
- `ImageFile.name: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:356`
- `ImageFile.size: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:357`
- `ImageFile.dir: boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:358`
- `ImageFile.path: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:359`
- `ImageFile.id: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:360`
- `ContentApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:64`
- `ContentApi.DEFAULT_PATH: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:66`
- `ContentApi.BOX: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:68`
- `ContentApi.PAGE: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:69`
- `ContentApi.contentFacade: ContentFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:72`
- `ContentApi.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:76`

## Functions and methods
- `ContentAdministrationApi.list(String, MerchantStore, Language) -> List<ImageFile>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:83`
- `ContentAdministrationApi.folder(String, MerchantStore, Language) -> ContentFolder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:105`
- `ContentAdministrationApi.upload(MultipartFile, String, String, Long, String, Integer, Integer, MerchantStore, Language) -> FileStatus` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:123`
- `ContentAdministrationApi.download(String, MerchantStore, Language) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:164`
- `ContentAdministrationApi.rename(String, String, MerchantStore, Language) -> FileStatus` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:186`
- `ContentAdministrationApi.remove(String, MerchantStore, Language) -> FileStatus` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:213`
- `ContentAdministrationApi.convertToImageFile(MerchantStore, Content) -> ImageFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:240`
- `ContentAdministrationApi.convertToFolder(String) -> ImageFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:251`
- `ContentAdministrationApi.decodeContentPath(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:261`
- `FileStatus.isSuccess() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:279`
- `FileStatus.setSuccess(boolean) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:282`
- `FileStatus.getError() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:285`
- `FileStatus.setError(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:288`
- `FileStatus.isPreventRetry() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:291`
- `FileStatus.setPreventRetry(boolean) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:294`
- `ImageFile.getUrl() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:303`
- `ImageFile.setUrl(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:307`
- `ImageFile.getName() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:311`
- `ImageFile.setName(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:315`
- `ImageFile.getSize() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:319`
- `ImageFile.setSize(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:323`
- `ImageFile.isDir() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:327`
- `ImageFile.setDir(boolean) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:331`
- `ImageFile.getPath() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:335`
- `ImageFile.setPath(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:339`
- `ImageFile.getId() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:343`
- `ImageFile.setId(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:347`
- `ContentApi.pages(MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentPage>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:86`
- `ContentApi.pagesSummary(MerchantStore, Language) -> List<ReadableContentBox>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:99`
- `ContentApi.boxes(MerchantStore, Language, int, int) -> ReadableEntityList<ReadableContentBox>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:118`
- `ContentApi.page(String, MerchantStore, Language) -> ReadableContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:139`
- `ContentApi.pageByName(String, MerchantStore, Language) -> ReadableContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:157`
- `ContentApi.createBox(PersistableContentBox, MerchantStore, Language) -> Entity` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:176`
- `ContentApi.boxExists(String, MerchantStore, Language) -> EntityExists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:193`
- `ContentApi.pageExists(String, MerchantStore, Language) -> EntityExists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:209`
- `ContentApi.createPage(PersistableContentPage, MerchantStore, Language) -> Entity` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:231`
- `ContentApi.deletePage(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:255`
- `ContentApi.deleteBox(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:276`
- `ContentApi.updatePage(PersistableContentPage, Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:291`
- `ContentApi.updateBox(PersistableContentBox, Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:306`
- `ContentApi.content(String, MerchantStore, Language) -> ReadableContentFull` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:321`
- `ContentApi.contents(MerchantStore, Language) -> List<ReadableContentEntity>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:333`
- `ContentApi.manageBoxByCode(String, MerchantStore, Language) -> ReadableContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:346`
- `ContentApi.getBoxByCode(String, MerchantStore, Language) -> ReadableContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:355`
- `ContentApi.addFolder(String, String, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:375`
- `ContentApi.images(MerchantStore, Language, String, HttpServletRequest, HttpServletResponse) -> ContentFolder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:392`
- `ContentApi.upload(MultipartFile, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:412`
- `ContentApi.uploadMultipleFiles(MultipartFile[], MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:432`
- `ContentApi.updatePage(Long, PersistableContentEntity, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:457`
- `ContentApi.deleteContent(Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:477`
- `ContentApi.deleteFile(ContentName, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:510`

## HTTP routes
- `GET /api/v1/content/boxes` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#boxes` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:118`
- `GET /api/v1/content/boxes/{code}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#getBoxByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:355`
- `DELETE /api/v1/content/folder` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#addFolder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:375`
- `GET /api/v1/content/images` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#images` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:392`
- `GET /api/v1/content/images/download` handled by `com.salesmanager.shop.store.api.v1.content.ContentAdministrationApi#download` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:164`
- `GET /api/v1/content/pages` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#pages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:86`
- `GET /api/v1/content/pages/name/{name}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#pageByName` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:157`
- `GET /api/v1/content/pages/{code}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#page` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:139`
- `GET /api/v1/content/summary` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#pagesSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:99`
- `DELETE /api/v1/private/content` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#deleteFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:510`
- `GET /api/v1/private/content/any/{code}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#content` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:321`
- `POST /api/v1/private/content/box` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#createBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:176`
- `GET /api/v1/private/content/box/{code}/exists` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#boxExists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:193`
- `DELETE /api/v1/private/content/box/{id}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#deleteBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:276`
- `PUT /api/v1/private/content/box/{id}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#updateBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:306`
- `GET /api/v1/private/content/boxes` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#boxes` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:118`
- `GET /api/v1/private/content/boxes/{code}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#manageBoxByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:346`
- `GET /api/v1/private/content/folder` handled by `com.salesmanager.shop.store.api.v1.content.ContentAdministrationApi#folder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:105`
- `POST /api/v1/private/content/images/add` handled by `com.salesmanager.shop.store.api.v1.content.ContentAdministrationApi#upload` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:123`
- `DELETE /api/v1/private/content/images/remove` handled by `com.salesmanager.shop.store.api.v1.content.ContentAdministrationApi#remove` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:213`
- `POST /api/v1/private/content/images/rename` handled by `com.salesmanager.shop.store.api.v1.content.ContentAdministrationApi#rename` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:186`
- `GET /api/v1/private/content/list` handled by `com.salesmanager.shop.store.api.v1.content.ContentAdministrationApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:83`
- `POST /api/v1/private/content/page` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#createPage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:231`
- `GET /api/v1/private/content/page/{code}/exists` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#pageExists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:209`
- `DELETE /api/v1/private/content/page/{id}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#deletePage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:255`
- `PUT /api/v1/private/content/page/{id}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#updatePage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:291`
- `GET /api/v1/private/content/pages` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#pages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:86`
- `DELETE /api/v1/private/content/{id}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#deleteContent` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:477`
- `PUT /api/v1/private/content/{id}` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#updatePage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:457`
- `GET /api/v1/private/contents/any` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#contents` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:333`
- `POST /api/v1/private/file` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#upload` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:412`
- `POST /api/v1/private/files` handled by `com.salesmanager.shop.store.api.v1.content.ContentApi#uploadMultipleFiles` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:432`

## Depends on
- [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:63`
- [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:71`
- [com.salesmanager.shop.utils.FileNameUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:66`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:70`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:74`

## Calls
- `ContentAdministrationApi.convertToImageFile` calls [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `ImageFilePath.buildStaticImageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:243`
- `ContentAdministrationApi.remove` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:226`
- `ContentAdministrationApi.rename` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.renameFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:200`
- `ContentAdministrationApi.upload` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.addContentFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:151`
- `ContentAdministrationApi.upload` calls [com.salesmanager.shop.utils.FileNameUtils](/modules/com.salesmanager.shop.utils.md) `FileNameUtils.validFileName` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentAdministrationApi.java:139`
- `ContentApi.boxExists` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.codeExist` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:204`
- `ContentApi.createBox` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.saveContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:187`
- `ContentApi.createPage` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.saveContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:242`
- `ContentApi.deleteBox` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:287`
- `ContentApi.deleteContent` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:482`
- `ContentApi.deleteFile` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:516`
- `ContentApi.deletePage` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:266`
- `ContentApi.pageExists` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.codeExist` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:220`
- `ContentApi.updateBox` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.updateContentBox` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:318`
- `ContentApi.updatePage` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.updateContentPage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:303`
- `ContentApi.upload` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.addContentFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:428`
- `ContentApi.uploadMultipleFiles` calls [com.salesmanager.shop.store.controller.content.facade.ContentFacade](/modules/com.salesmanager.shop.store.controller.content.facade.md) `ContentFacade.addContentFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/content/ContentApi.java:448`
