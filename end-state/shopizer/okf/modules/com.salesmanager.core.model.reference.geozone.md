---
type: Code Module
title: "com.salesmanager.core.model.reference.geozone"
description: "com.salesmanager.core.model.reference.geozone: GeoZone, GeoZoneDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java"
    sha256: "238218b694eaf6fbb30973417db95376df369f15b91b01dc7f3b8899ab0804ec"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZoneDescription.java"
    sha256: "3b4f76fa59d2cddd549a9eb31b738997c53990810ecdb19bf69af7c9d4fc87f1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.reference.geozone

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZoneDescription.java`

## Types
- `GeoZone` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:21`
- `GeoZoneDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZoneDescription.java:14`

## Fields
- `GeoZone.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:31`
- `GeoZone.descriptions: List<GeoZoneDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:34`
- `GeoZone.countries: List<Country>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:38`
- `GeoZone.name: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:43`
- `GeoZone.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:46`
- `GeoZoneDescription.geoZone: GeoZone` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZoneDescription.java:30`

## Functions and methods
- `GeoZone.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:51`
- `GeoZone.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:56`
- `GeoZone.getName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:62`
- `GeoZone.setName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:66`
- `GeoZone.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:70`
- `GeoZone.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:74`
- `GeoZone.getCountries() -> List<Country>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:78`
- `GeoZone.setCountries(List<Country>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:82`
- `GeoZone.getDescriptions() -> List<GeoZoneDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:86`
- `GeoZone.setDescriptions(List<GeoZoneDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:90`
- `GeoZoneDescription.getGeoZone() -> GeoZone` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZoneDescription.java:35`
- `GeoZoneDescription.setGeoZone(GeoZone) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZoneDescription.java:39`

## Depends on
- [com.salesmanager.core.model.reference.country.Country](/modules/com.salesmanager.core.model.reference.country.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/geozone/GeoZone.java:36`
