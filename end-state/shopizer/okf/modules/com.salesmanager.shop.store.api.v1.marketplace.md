---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.marketplace"
description: "com.salesmanager.shop.store.api.v1.marketplace: MarketPlaceApi; 3 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java"
    sha256: "dcbb9cc944d1eedf96f369fc0193e5f59bb47483c6e60b61075405a9def921c6"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.marketplace

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java`

## Types
- `MarketPlaceApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:34`

## Fields
- `MarketPlaceApi.marketPlaceFacade: MarketPlaceFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:39`
- `MarketPlaceApi.userFacade: UserFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:42`
- `MarketPlaceApi.storeFacade: StoreFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:45`
- `MarketPlaceApi.languageUtils: LanguageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:48`

## Functions and methods
- `MarketPlaceApi.marketPlace(String, String) -> ReadableMarketPlace` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:54`
- `MarketPlaceApi.signup(SignupStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:64`
- `MarketPlaceApi.storeSignupVerify(String, String, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:95`

## HTTP routes
- `GET /api/v1/private/marketplace/{store}` handled by `com.salesmanager.shop.store.api.v1.marketplace.MarketPlaceApi#marketPlace` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:54`
- `POST /api/v1/store/signup` handled by `com.salesmanager.shop.store.api.v1.marketplace.MarketPlaceApi#signup` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:64`
- `GET /api/v1/store/{store}/signup/{token}` handled by `com.salesmanager.shop.store.api.v1.marketplace.MarketPlaceApi#storeSignupVerify` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:95`

## Depends on
- [com.salesmanager.shop.store.controller.marketplace.facade.MarketPlaceFacade](/modules/com.salesmanager.shop.store.controller.marketplace.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:38`
- [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:44`
- [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:41`
- [com.salesmanager.shop.utils.LanguageUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:47`

## Calls
- `MarketPlaceApi.marketPlace` calls [com.salesmanager.shop.store.controller.marketplace.facade.MarketPlaceFacade](/modules/com.salesmanager.shop.store.controller.marketplace.facade.md) `MarketPlaceFacade.get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:60`
- `MarketPlaceApi.signup` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.existByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:82`
- `MarketPlaceApi.signup` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.findByUserName` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/marketplace/MarketPlaceApi.java:71`
