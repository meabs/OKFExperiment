---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.configurations"
description: "com.salesmanager.shop.store.api.v1.configurations: CacheApi, ConfigurationsApi; 4 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java"
    sha256: "a245b494faa7a8fc7e0732fa329b9a901c1b4894d346742c141a0626d0e9e4bc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java"
    sha256: "69a9021ce6e246462e2a26a3583652cf7dcbb525c25a2b44a527c696543b827a"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.configurations

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java`

## Types
- `CacheApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:24`
- `ConfigurationsApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:22`

## Fields
- `CacheApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:28`
- `CacheApi.storeFacade: StoreFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:31`
- `CacheApi.cache: CacheUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:34`

## Functions and methods
- `CacheApi.clearCache(String, String) -> ResponseEntity<String>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:36`
- `ConfigurationsApi.create(MerchantStore, Language) -> Void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:31`
- `ConfigurationsApi.listPaymentConfigurations(MerchantStore, Language) -> List<ReadableConfiguration>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:51`
- `ConfigurationsApi.listShippingConfigurations(MerchantStore, Language) -> List<ReadableConfiguration>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:73`

## HTTP routes
- `DELETE /api/v1/auth/cache/store/{storeId}/clear` handled by `com.salesmanager.shop.store.api.v1.configurations.CacheApi#clearCache` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:36`
- `GET /api/v1/private/configurations/payment` handled by `com.salesmanager.shop.store.api.v1.configurations.ConfigurationsApi#listPaymentConfigurations` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:51`
- `POST /api/v1/private/configurations/payment` handled by `com.salesmanager.shop.store.api.v1.configurations.ConfigurationsApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:31`
- `GET /api/v1/private/configurations/shipping` handled by `com.salesmanager.shop.store.api.v1.configurations.ConfigurationsApi#listShippingConfigurations` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/ConfigurationsApi.java:73`

## Depends on
- [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:33`
- [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:30`

## Calls
- `CacheApi.clearCache` calls [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `CacheUtils.removeAllFromCache`, `CacheUtils.removeFromCache` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:48`
- `CacheApi.clearCache` calls [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `StoreFacade.get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/configurations/CacheApi.java:41`
