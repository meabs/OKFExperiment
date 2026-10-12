---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.references"
description: "com.salesmanager.shop.store.api.v1.references: ReferencesApi; 5 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java"
    sha256: "788e5c336b0342eb5dec664495384c7af78e748ece5f5b0048c33927b91c1948"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.references

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java`

## Types
- `ReferencesApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:38`

## Fields
- `ReferencesApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:42`
- `ReferencesApi.storeFacade: StoreFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:45`
- `ReferencesApi.languageUtils: LanguageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:47`
- `ReferencesApi.languageFacade: LanguageFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:49`
- `ReferencesApi.countryFacade: CountryFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:51`
- `ReferencesApi.zoneFacade: ZoneFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:53`
- `ReferencesApi.currencyFacade: CurrencyFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:55`

## Functions and methods
- `ReferencesApi.getLanguages() -> List<Language>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:62`
- `ReferencesApi.getCountry(Language, HttpServletRequest) -> List<ReadableCountry>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:74`
- `ReferencesApi.getZones(String, Language, HttpServletRequest) -> List<ReadableZone>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:80`
- `ReferencesApi.getCurrency() -> List<Currency>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:92`
- `ReferencesApi.measures() -> SizeReferences` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:97`

## HTTP routes
- `GET /api/v1/country` handled by `com.salesmanager.shop.store.api.v1.references.ReferencesApi#getCountry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:74`
- `GET /api/v1/currency` handled by `com.salesmanager.shop.store.api.v1.references.ReferencesApi#getCurrency` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:92`
- `GET /api/v1/languages` handled by `com.salesmanager.shop.store.api.v1.references.ReferencesApi#getLanguages` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:62`
- `GET /api/v1/measures` handled by `com.salesmanager.shop.store.api.v1.references.ReferencesApi#measures` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:97`
- `GET /api/v1/zones` handled by `com.salesmanager.shop.store.api.v1.references.ReferencesApi#getZones` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:80`

## Depends on
- [com.salesmanager.shop.store.controller.country.facade.CountryFacade](/modules/com.salesmanager.shop.store.controller.country.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:51`
- [com.salesmanager.shop.store.controller.currency.facade.CurrencyFacade](/modules/com.salesmanager.shop.store.controller.currency.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:55`
- [com.salesmanager.shop.store.controller.language.facade.LanguageFacade](/modules/com.salesmanager.shop.store.controller.language.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:49`
- [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:45`
- [com.salesmanager.shop.store.controller.zone.facade.ZoneFacade](/modules/com.salesmanager.shop.store.controller.zone.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:53`
- [com.salesmanager.shop.utils.LanguageUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:47`

## Calls
- `ReferencesApi.measures` calls [com.salesmanager.shop.model.references.MeasureUnit](/modules/com.salesmanager.shop.model.references.md) `MeasureUnit.values` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:100`
- `ReferencesApi.measures` calls [com.salesmanager.shop.model.references.WeightUnit](/modules/com.salesmanager.shop.model.references.md) `WeightUnit.values` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/references/ReferencesApi.java:101`
