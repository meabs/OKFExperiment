---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.store"
description: "com.salesmanager.shop.store.api.v1.store: MerchantStoreApi; 16 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java"
    sha256: "64826491ae7308c31e0497acea13b8f7b250e56f031fca8665a56d31177ec48b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.store

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java`

## Types
- `MerchantStoreApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:61`

## Fields
- `MerchantStoreApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:68`
- `MerchantStoreApi.MAPPING_FIELDS: Map<String, String>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:70`
- `MerchantStoreApi.storeFacade: StoreFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:74`
- `MerchantStoreApi.userFacade: UserFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:77`

## Functions and methods
- `MerchantStoreApi.store(String, String) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:79`
- `MerchantStoreApi.storeFull(String, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:88`
- `MerchantStoreApi.list(String, Language, Integer, Integer) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:104`
- `MerchantStoreApi.get(MerchantStore, Language, Integer, Integer, HttpServletRequest) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:124`
- `MerchantStoreApi.list(MerchantStore, Language, Integer, Integer, HttpServletRequest) -> List<ReadableMerchantStore>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:166`
- `MerchantStoreApi.supportedLanguages(MerchantStore, HttpServletRequest) -> List<Language>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:200`
- `MerchantStoreApi.create(PersistableMerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:210`
- `MerchantStoreApi.update(String, PersistableMerchantStore, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:227`
- `MerchantStoreApi.getUserFromRequest(HttpServletRequest) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:239`
- `MerchantStoreApi.validateUserPermission(String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:245`
- `MerchantStoreApi.getStoreMarketing(String, HttpServletRequest) -> ReadableBrand` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:252`
- `MerchantStoreApi.children(String, Language, Integer, Integer, HttpServletRequest) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:268`
- `MerchantStoreApi.saveStoreMarketing(String, PersistableBrand, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:283`
- `MerchantStoreApi.addLogo(String, MultipartFile, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:294`
- `MerchantStoreApi.createInputContentFile(MultipartFile) -> InputContentFile` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:313`
- `MerchantStoreApi.deleteStoreLogo(String, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:333`
- `MerchantStoreApi.exists(String) -> ResponseEntity<EntityExists>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:346`
- `MerchantStoreApi.delete(String, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:356`
- `MerchantStoreApi.createMerchantStoreCriteria(HttpServletRequest) -> MerchantStoreCriteria` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:366`

## HTTP routes
- `GET /api/v1/private/merchant/{code}/children` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#children` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:268`
- `GET /api/v1/private/merchant/{code}/stores` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:104`
- `POST /api/v1/private/store` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:210`
- `GET /api/v1/private/store/unique` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:346`
- `DELETE /api/v1/private/store/{code}` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:356`
- `GET /api/v1/private/store/{code}` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#storeFull` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:88`
- `PUT /api/v1/private/store/{code}` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:227`
- `GET /api/v1/private/store/{code}/marketing` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#getStoreMarketing` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:252`
- `POST /api/v1/private/store/{code}/marketing` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#saveStoreMarketing` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:283`
- `DELETE /api/v1/private/store/{code}/marketing/logo` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#deleteStoreLogo` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:333`
- `POST /api/v1/private/store/{code}/marketing/logo` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#addLogo` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:294`
- `GET /api/v1/private/stores` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:124`
- `GET /api/v1/private/stores/names` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:166`
- `GET /api/v1/store/languages` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#supportedLanguages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:200`
- `GET /api/v1/store/unique` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:346`
- `GET /api/v1/store/{code}` handled by `com.salesmanager.shop.store.api.v1.store.MerchantStoreApi#store` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:79`

## Depends on
- [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:73`
- [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:76`

## Calls
- `MerchantStoreApi.addLogo` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.addStoreLogo` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:310`
- `MerchantStoreApi.create` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:224`
- `MerchantStoreApi.create` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:216`
- `MerchantStoreApi.createMerchantStoreCriteria` calls [com.salesmanager.shop.utils.ServiceRequestCriteriaBuilderUtils](/modules/com.salesmanager.shop.utils.md) `ServiceRequestCriteriaBuilderUtils.buildRequestCriterias` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:368`
- `MerchantStoreApi.delete` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:362`
- `MerchantStoreApi.deleteStoreLogo` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.deleteLogo` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:343`
- `MerchantStoreApi.exists` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.existByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:350`
- `MerchantStoreApi.get` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.findAll` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:154`
- `MerchantStoreApi.get` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.userInRoles` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:135`
- `MerchantStoreApi.list` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.findAll` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:195`
- `MerchantStoreApi.list` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.userInRoles` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:111`
- `MerchantStoreApi.saveStoreMarketing` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.createBrand` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:291`
- `MerchantStoreApi.storeFull` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:95`
- `MerchantStoreApi.supportedLanguages` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.supportedLanguages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:207`
- `MerchantStoreApi.update` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:236`
- `MerchantStoreApi.validateUserPermission` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authorizedStore` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/store/MerchantStoreApi.java:247`

## Tests
- `com.salesmanager.test.shop.integration.store.MerchantStoreApiIntegrationTest`
