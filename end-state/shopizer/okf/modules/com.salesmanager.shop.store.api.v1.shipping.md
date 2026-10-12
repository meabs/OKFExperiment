---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.shipping"
description: "com.salesmanager.shop.store.api.v1.shipping: ShippingConfigurationApi, ShippingExpeditionApi; 13 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java"
    sha256: "405a51020aabddb34a6c8e5563016ebf84978037f8bb51c351ee1b8819be168c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java"
    sha256: "88d41ebd7b2ec0a6b6592239133eb527525cfba67659716c6ad9aafdc5afe0b9"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.shipping

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java`

## Types
- `ShippingConfigurationApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:48`
- `ShippingExpeditionApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:35`

## Fields
- `ShippingConfigurationApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:55`
- `ShippingConfigurationApi.authorizationUtils: AuthorizationUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:58`
- `ShippingConfigurationApi.shippingFacade: ShippingFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:61`
- `ShippingConfigurationApi.shippingService: ShippingService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:64`
- `ShippingExpeditionApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:41`
- `ShippingExpeditionApi.authorizationUtils: AuthorizationUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:44`
- `ShippingExpeditionApi.shippingFacade: ShippingFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:47`

## Functions and methods
- `ShippingConfigurationApi.shippingOrigin(MerchantStore, Language) -> ReadableAddress` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:66`
- `ShippingConfigurationApi.saveShippingOrigin(PersistableAddress, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:80`
- `ShippingConfigurationApi.listPackages(MerchantStore, Language) -> List<PackageDetails>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:94`
- `ShippingConfigurationApi.getPackage(String, MerchantStore, Language) -> PackageDetails` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:108`
- `ShippingConfigurationApi.createPackage(PackageDetails, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:123`
- `ShippingConfigurationApi.updatePackage(String, PackageDetails, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:138`
- `ShippingConfigurationApi.deletePackage(String, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:153`
- `ShippingConfigurationApi.shippingModules(MerchantStore, Language) -> List<IntegrationModuleSummaryEntity>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:174`
- `ShippingConfigurationApi.shippingModule(String, MerchantStore, Language) -> IntegrationConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:203`
- `ShippingConfigurationApi.configure(IntegrationModuleConfiguration, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:246`
- `ShippingConfigurationApi.integrationModule(IntegrationModule, Map<String, IntegrationConfiguration>) -> IntegrationModuleSummaryEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:290`
- `ShippingExpeditionApi.expedition(MerchantStore, Language) -> ExpeditionConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:49`
- `ShippingExpeditionApi.getCountry(MerchantStore, Language) -> List<ReadableCountry>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:65`
- `ShippingExpeditionApi.saveExpedition(ExpeditionConfiguration, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:74`

## HTTP routes
- `GET /api/v1/private/modules/shipping` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#shippingModules` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:174`
- `POST /api/v1/private/modules/shipping` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#configure` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:246`
- `GET /api/v1/private/modules/shipping/{code}` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#shippingModule` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:203`
- `GET /api/v1/private/shipping/expedition` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingExpeditionApi#expedition` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:49`
- `POST /api/v1/private/shipping/expedition` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingExpeditionApi#saveExpedition` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:74`
- `GET /api/v1/private/shipping/origin` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#shippingOrigin` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:66`
- `POST /api/v1/private/shipping/origin` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#saveShippingOrigin` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:80`
- `POST /api/v1/private/shipping/package` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#createPackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:123`
- `DELETE /api/v1/private/shipping/package/{code}` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#deletePackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:153`
- `GET /api/v1/private/shipping/package/{code}` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#getPackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:108`
- `PUT /api/v1/private/shipping/package/{code}` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#updatePackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:138`
- `GET /api/v1/private/shipping/packages` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingConfigurationApi#listPackages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:94`
- `GET /api/v1/shipping/country` handled by `com.salesmanager.shop.store.api.v1.shipping.ShippingExpeditionApi#getCountry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:65`

## Depends on
- [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:63`
- [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:60`
- [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:46`
- [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:57`
- [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:43`

## Calls
- `ShippingConfigurationApi.configure` calls [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `ShippingService.saveShippingQuoteModuleConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:281`
- `ShippingConfigurationApi.createPackage` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.createPackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:133`
- `ShippingConfigurationApi.createPackage` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:129`
- `ShippingConfigurationApi.deletePackage` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.deletePackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:163`
- `ShippingConfigurationApi.deletePackage` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:159`
- `ShippingConfigurationApi.getPackage` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:114`
- `ShippingConfigurationApi.listPackages` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.listPackages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:103`
- `ShippingConfigurationApi.listPackages` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:99`
- `ShippingConfigurationApi.saveShippingOrigin` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.saveShippingOrigin` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:89`
- `ShippingConfigurationApi.saveShippingOrigin` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:85`
- `ShippingConfigurationApi.shippingOrigin` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:72`
- `ShippingConfigurationApi.updatePackage` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.updatePackage` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:148`
- `ShippingConfigurationApi.updatePackage` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingConfigurationApi.java:144`
- `ShippingExpeditionApi.expedition` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:57`
- `ShippingExpeditionApi.getCountry` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.shipToCountry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:70`
- `ShippingExpeditionApi.saveExpedition` calls [com.salesmanager.shop.store.controller.shipping.facade.ShippingFacade](/modules/com.salesmanager.shop.store.controller.shipping.facade.md) `ShippingFacade.saveExpeditionConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:87`
- `ShippingExpeditionApi.saveExpedition` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shipping/ShippingExpeditionApi.java:83`
