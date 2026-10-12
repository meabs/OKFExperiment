---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.category"
description: "com.salesmanager.shop.store.api.v1.category: CategoryApi; 10 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java"
    sha256: "cabc77735df8c91227d0da0b014a89e0c280b0449ec1157a430e61e3f1af839f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.category

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java`

## Types
- `CategoryApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:50`

## Fields
- `CategoryApi.DEFAULT_CATEGORY_DEPTH: int` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:57`
- `CategoryApi.categoryFacade: CategoryFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:60`
- `CategoryApi.userFacade: UserFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:63`

## Functions and methods
- `CategoryApi.get(Long, MerchantStore, Language) -> ReadableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:65`
- `CategoryApi.getByfriendlyUrl(String, MerchantStore, Language) -> ReadableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:79`
- `CategoryApi.exists(String, MerchantStore, Language) -> ResponseEntity<EntityExists>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:95`
- `CategoryApi.list(List<String>, String, MerchantStore, Language, Integer, Integer) -> ReadableCategoryList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:112`
- `CategoryApi.list(Long, MerchantStore, Language) -> ReadableCategoryList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:132`
- `CategoryApi.create(PersistableCategory, MerchantStore, Language) -> PersistableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:146`
- `CategoryApi.update(Long, PersistableCategory, MerchantStore) -> PersistableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:166`
- `CategoryApi.updateVisible(Long, PersistableCategory, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:184`
- `CategoryApi.move(Long, Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:202`
- `CategoryApi.delete(Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:222`

## HTTP routes
- `GET /api/v1/category` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:112`
- `GET /api/v1/category/product/{ProductId}` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:132`
- `GET /api/v1/category/{friendlyUrl}` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#getByfriendlyUrl` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:79`
- `GET /api/v1/category/{id}` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:65`
- `POST /api/v1/private/category` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:146`
- `GET /api/v1/private/category/unique` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:95`
- `DELETE /api/v1/private/category/{id}` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:222`
- `PUT /api/v1/private/category/{id}` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:166`
- `PUT /api/v1/private/category/{id}/move/{parent}` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#move` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:202`
- `PATCH /api/v1/private/category/{id}/visible` handled by `com.salesmanager.shop.store.api.v1.category.CategoryApi#updateVisible` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:184`

## Depends on
- [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:59`
- [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:62`

## Calls
- `CategoryApi.create` calls [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `CategoryFacade.saveCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:163`
- `CategoryApi.create` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:156`
- `CategoryApi.delete` calls [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `CategoryFacade.deleteCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:235`
- `CategoryApi.delete` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:227`
- `CategoryApi.exists` calls [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `CategoryFacade.existByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:102`
- `CategoryApi.list` calls [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `CategoryFacade.listByProduct` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:142`
- `CategoryApi.move` calls [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `CategoryFacade.move` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:218`
- `CategoryApi.move` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:210`
- `CategoryApi.update` calls [com.salesmanager.shop.store.controller.category.facade.CategoryFacade](/modules/com.salesmanager.shop.store.controller.category.facade.md) `CategoryFacade.saveCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:181`
- `CategoryApi.update` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:172`
- `CategoryApi.updateVisible` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/category/CategoryApi.java:191`
