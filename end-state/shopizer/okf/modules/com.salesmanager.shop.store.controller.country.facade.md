---
type: Code Module
title: "com.salesmanager.shop.store.controller.country.facade"
description: "com.salesmanager.shop.store.controller.country.facade: CountryFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacade.java"
    sha256: "a18c3b4d7814d7dccaf5dd45f3818547d147df8f2cc9e9f1f46783fe0c35649e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java"
    sha256: "7fe9c5714fcfa856ccc23803f5223190b99c9bb63d4bc9305101ea0b755fe4b5"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.country.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java`

## Types
- `CountryFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacade.java:9`
- `CountryFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:18`

## Fields
- `CountryFacadeImpl.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:22`

## Functions and methods
- `CountryFacade.getListCountryZones(Language, MerchantStore) -> List<ReadableCountry>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacade.java:10`
- `CountryFacadeImpl.getListCountryZones(Language, MerchantStore) -> List<ReadableCountry>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:24`
- `CountryFacadeImpl.convertToReadableCountry(Country, Language, MerchantStore) -> ReadableCountry` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:32`
- `CountryFacadeImpl.getListOfCountryZones(Language) -> List<Country>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:41`

## Depends on
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:21`

## Calls
- `CountryFacadeImpl.convertToReadableCountry` calls [com.salesmanager.shop.populator.references.ReadableCountryPopulator](/modules/com.salesmanager.shop.populator.references.md) `ReadableCountryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:35`
- `CountryFacadeImpl.getListOfCountryZones` calls [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `CountryService.listCountryZones` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/country/facade/CountryFacadeImpl.java:43`
