---
type: Code Module
title: "com.salesmanager.core.model.reference.country"
description: "com.salesmanager.core.model.reference.country: Country, CountryDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java"
    sha256: "70f4597285db57c7ea0de3a5cc954d91ba02793dc331a2f45898d7417cfa53fb"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java"
    sha256: "e3073c5fd85dc1e6a380081b3b045a78f4db064f58affcc00ad31678700eab7a"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.reference.country

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java`

## Types
- `Country` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:27`
- `CountryDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java:16`

## Fields
- `Country.id: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:38`
- `Country.descriptions: Set<CountryDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:42`
- `Country.zones: Set<Zone>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:46`
- `Country.geoZone: GeoZone` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:50`
- `Country.supported: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:53`
- `Country.isoCode: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:56`
- `Country.name: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:59`
- `CountryDescription.country: Country` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java:32`

## Functions and methods
- `Country.getName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:61`
- `Country.setName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:65`
- `Country.getSupported() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:76`
- `Country.setSupported(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:80`
- `Country.getIsoCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:84`
- `Country.setIsoCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:88`
- `Country.getId() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:93`
- `Country.setId(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:98`
- `Country.getZones() -> Set<Zone>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:104`
- `Country.setZones(Set<Zone>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:108`
- `Country.getGeoZone() -> GeoZone` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:113`
- `Country.setGeoZone(GeoZone) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:117`
- `Country.getDescriptions() -> Set<CountryDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:122`
- `Country.setDescriptions(Set<CountryDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:126`
- `CountryDescription.getCountry() -> Country` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java:42`
- `CountryDescription.setCountry(Country) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java:46`

## Depends on
- [com.salesmanager.core.model.reference.geozone.GeoZone](/modules/com.salesmanager.core.model.reference.geozone.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:48`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/CountryDescription.java:37`
- [com.salesmanager.core.model.reference.zone.Zone](/modules/com.salesmanager.core.model.reference.zone.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/country/Country.java:44`
