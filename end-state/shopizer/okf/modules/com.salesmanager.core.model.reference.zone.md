---
type: Code Module
title: "com.salesmanager.core.model.reference.zone"
description: "com.salesmanager.core.model.reference.zone: Zone, ZoneDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java"
    sha256: "b5a29427c4d57d4c05302cd415774ea0d9aa39b6678d36f008528e3e9bc5afdc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java"
    sha256: "484f4f6c1c2573e91b1b3f5a942a84f3220e9b7d9d5c45c949724c3ec9a2312c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.reference.zone

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java`

## Types
- `Zone` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:24`
- `ZoneDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java:15`

## Fields
- `Zone.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:34`
- `Zone.descriptions: List<ZoneDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:38`
- `Zone.country: Country` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:43`
- `Zone.name: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:46`
- `Zone.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:51`
- `ZoneDescription.zone: Zone` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java:31`

## Functions and methods
- `Zone.getCountry() -> Country` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:61`
- `Zone.setCountry(Country) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:65`
- `Zone.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:71`
- `Zone.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:75`
- `Zone.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:79`
- `Zone.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:84`
- `Zone.getDescriptions() -> List<ZoneDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:89`
- `Zone.setDescriptons(List<ZoneDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:93`
- `Zone.getName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:97`
- `Zone.setName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:101`
- `ZoneDescription.getZone() -> Zone` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java:42`
- `ZoneDescription.setZone(Zone) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java:46`

## Depends on
- [com.salesmanager.core.model.reference.country.Country](/modules/com.salesmanager.core.model.reference.country.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/Zone.java:40`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/zone/ZoneDescription.java:36`
