---
type: Code Module
title: "com.salesmanager.core.business.services.reference.zone"
description: "com.salesmanager.core.business.services.reference.zone: ZoneServiceImpl, ZoneTransient"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java"
    sha256: "e6a849c518f66045829b7aad0ddc9dae3f67566373a2af3f551e583433c0d4bf"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java"
    sha256: "881d02e86c02dc094226f8b90ac1679e9e71579d6629d28e0e67b658f2c879b8"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java"
    sha256: "81d3dfdfece8b277fb90b17ecbe52dfb02c31f27ff2638984c8ad7f947880b72"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.reference.zone

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java`

## Types
- `ZoneService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java:13`
- `ZoneServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:26`
- `ZoneTransient` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:3`

## Fields
- `ZoneServiceImpl.ZONE_CACHE_PREFIX: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:30`
- `ZoneServiceImpl.zoneRepository: ZoneRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:32`
- `ZoneServiceImpl.cache: CacheUtils` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:35`
- `ZoneServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:37`
- `ZoneTransient.zoneCode: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:5`
- `ZoneTransient.zoneName: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:6`
- `ZoneTransient.countryCode: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:7`

## Functions and methods
- `ZoneService.getByCode(String) -> Zone` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java:15`
- `ZoneService.addDescription(Zone, ZoneDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java:17`
- `ZoneService.getZones(Country, Language) -> List<Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java:19`
- `ZoneService.getZones(Language) -> Map<String, Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java:22`
- `ZoneService.getZones(String, Language) -> List<Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneService.java:24`
- `ZoneServiceImpl.getByCode(String) -> Zone` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:45`
- `ZoneServiceImpl.addDescription(Zone, ZoneDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:51`
- `ZoneServiceImpl.getZones(Country, Language) -> List<Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:66`
- `ZoneServiceImpl.getZones(String, Language) -> List<Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:108`
- `ZoneServiceImpl.getZones(Language) -> Map<String, Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:146`
- `ZoneTransient.getZoneCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:9`
- `ZoneTransient.setZoneCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:12`
- `ZoneTransient.getZoneName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:15`
- `ZoneTransient.setZoneName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:18`
- `ZoneTransient.getCountryCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:21`
- `ZoneTransient.setCountryCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneTransient.java:24`

## Depends on
- [com.salesmanager.core.business.repositories.reference.zone.ZoneRepository](/modules/com.salesmanager.core.business.repositories.reference.zone.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:32`
- [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:34`

## Calls
- `ZoneServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.reference.zone.ZoneRepository](/modules/com.salesmanager.core.business.repositories.reference.zone.md) `ZoneRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:48`
- `ZoneServiceImpl.getZones` calls [com.salesmanager.core.business.repositories.reference.zone.ZoneRepository](/modules/com.salesmanager.core.business.repositories.reference.zone.md) `ZoneRepository.listByLanguage`, `ZoneRepository.listByLanguageAndCountry` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:161`
- `ZoneServiceImpl.getZones` calls [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `CacheUtils.putInCache` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/zone/ZoneServiceImpl.java:97`
