---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.tax"
description: "com.salesmanager.shop.store.api.v1.tax: TaxClassApi, TaxRatesApi; 12 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java"
    sha256: "31c9125c6ccf9a73a05b93e01cb15827d847ee089bef4cf62244d37398ae01e7"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java"
    sha256: "e28bb95d2d26eb50456f83eca3ea08d18502e26b74efaede9485b6cb0067b45d"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.tax

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java`

## Types
- `TaxClassApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:45`
- `TaxRatesApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:45`

## Fields
- `TaxClassApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:51`
- `TaxClassApi.taxFacade: TaxFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:54`
- `TaxRatesApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:51`
- `TaxRatesApi.taxFacade: TaxFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:54`

## Functions and methods
- `TaxClassApi.create(MerchantStore, Language, PersistableTaxClass) -> Entity` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:57`
- `TaxClassApi.exists(String, MerchantStore, Language) -> ResponseEntity<EntityExists>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:67`
- `TaxClassApi.update(MerchantStore, Long, Language, PersistableTaxClass) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:80`
- `TaxClassApi.list(int, int, MerchantStore, Language) -> ReadableEntityList<ReadableTaxClass>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:91`
- `TaxClassApi.get(MerchantStore, String, Language) -> ReadableTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:103`
- `TaxClassApi.delete(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:112`
- `TaxRatesApi.create(MerchantStore, Language, PersistableTaxRate) -> Entity` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:57`
- `TaxRatesApi.exists(String, MerchantStore, Language) -> ResponseEntity<EntityExists>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:67`
- `TaxRatesApi.update(MerchantStore, Long, Language, PersistableTaxRate) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:80`
- `TaxRatesApi.list(int, int, MerchantStore, Language) -> ReadableEntityList<ReadableTaxRate>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:91`
- `TaxRatesApi.get(MerchantStore, Long, Language) -> ReadableTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:103`
- `TaxRatesApi.delete(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:112`

## HTTP routes
- `GET /api/v1/private/tax/class` handled by `com.salesmanager.shop.store.api.v1.tax.TaxClassApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:91`
- `POST /api/v1/private/tax/class` handled by `com.salesmanager.shop.store.api.v1.tax.TaxClassApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:57`
- `GET /api/v1/private/tax/class/unique` handled by `com.salesmanager.shop.store.api.v1.tax.TaxClassApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:67`
- `GET /api/v1/private/tax/class/{code}` handled by `com.salesmanager.shop.store.api.v1.tax.TaxClassApi#get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:103`
- `DELETE /api/v1/private/tax/class/{id}` handled by `com.salesmanager.shop.store.api.v1.tax.TaxClassApi#delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:112`
- `PUT /api/v1/private/tax/class/{id}` handled by `com.salesmanager.shop.store.api.v1.tax.TaxClassApi#update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:80`
- `POST /api/v1/private/tax/rate` handled by `com.salesmanager.shop.store.api.v1.tax.TaxRatesApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:57`
- `GET /api/v1/private/tax/rate/unique` handled by `com.salesmanager.shop.store.api.v1.tax.TaxRatesApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:67`
- `DELETE /api/v1/private/tax/rate/{id}` handled by `com.salesmanager.shop.store.api.v1.tax.TaxRatesApi#delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:112`
- `GET /api/v1/private/tax/rate/{id}` handled by `com.salesmanager.shop.store.api.v1.tax.TaxRatesApi#get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:103`
- `PUT /api/v1/private/tax/rate/{id}` handled by `com.salesmanager.shop.store.api.v1.tax.TaxRatesApi#update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:80`
- `GET /api/v1/private/tax/rates` handled by `com.salesmanager.shop.store.api.v1.tax.TaxRatesApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:91`

## Depends on
- [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:53`

## Calls
- `TaxClassApi.create` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.createTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:63`
- `TaxClassApi.delete` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.deleteTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:118`
- `TaxClassApi.exists` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.existsTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:74`
- `TaxClassApi.get` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.taxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:108`
- `TaxClassApi.list` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.taxClasses` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:99`
- `TaxClassApi.update` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.updateTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxClassApi.java:87`
- `TaxRatesApi.create` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.createTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:63`
- `TaxRatesApi.delete` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.deleteTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:118`
- `TaxRatesApi.exists` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.existsTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:74`
- `TaxRatesApi.get` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.taxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:108`
- `TaxRatesApi.list` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.taxRates` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:99`
- `TaxRatesApi.update` calls [com.salesmanager.shop.store.controller.tax.facade.TaxFacade](/modules/com.salesmanager.shop.store.controller.tax.facade.md) `TaxFacade.updateTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/tax/TaxRatesApi.java:87`
