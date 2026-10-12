---
type: Code Module
title: "com.salesmanager.core.business.services.reference.country"
description: "com.salesmanager.core.business.services.reference.country: CountryServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java"
    sha256: "5ae1e4197955a409c6f8fab8b271bedafa24894587f02c4abb26ea5f8f083f86"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java"
    sha256: "2a1054fc20bad1bd8ad820f8e4aeba619e935ad5f3a983288ccccb7d10ffeae1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.reference.country

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java`

## Types
- `CountryService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:12`
- `CountryServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:24`

## Fields
- `CountryServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:28`
- `CountryServiceImpl.countryRepository: CountryRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:30`
- `CountryServiceImpl.cache: CacheUtils` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:33`

## Functions and methods
- `CountryService.getByCode(String) -> Country` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:14`
- `CountryService.addCountryDescription(Country, CountryDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:16`
- `CountryService.getCountries(Language) -> List<Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:18`
- `CountryService.getCountriesMap(Language) -> Map<String, Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:20`
- `CountryService.getCountries(List<String>, Language) -> List<Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:23`
- `CountryService.listCountryZones(Language) -> List<Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryService.java:33`
- `CountryServiceImpl.getByCode(String) -> Country` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:42`
- `CountryServiceImpl.addCountryDescription(Country, CountryDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:47`
- `CountryServiceImpl.getCountriesMap(Language) -> Map<String,Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:54`
- `CountryServiceImpl.getCountries(List<String>, Language) -> List<Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:70`
- `CountryServiceImpl.getCountries(Language) -> List<Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:85`
- `CountryServiceImpl.listCountryZones(Language) -> List<Country>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:117`

## Depends on
- [com.salesmanager.core.business.repositories.reference.country.CountryRepository](/modules/com.salesmanager.core.business.repositories.reference.country.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:30`
- [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:32`

## Calls
- `CountryServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.reference.country.CountryRepository](/modules/com.salesmanager.core.business.repositories.reference.country.md) `CountryRepository.findByIsoCode` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:44`
- `CountryServiceImpl.getCountries` calls [com.salesmanager.core.business.repositories.reference.country.CountryRepository](/modules/com.salesmanager.core.business.repositories.reference.country.md) `CountryRepository.listByLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:95`
- `CountryServiceImpl.getCountries` calls [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `CacheUtils.putInCache` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:105`
- `CountryServiceImpl.listCountryZones` calls [com.salesmanager.core.business.repositories.reference.country.CountryRepository](/modules/com.salesmanager.core.business.repositories.reference.country.md) `CountryRepository.listCountryZonesByLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/country/CountryServiceImpl.java:120`
