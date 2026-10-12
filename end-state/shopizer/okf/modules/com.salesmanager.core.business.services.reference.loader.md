---
type: Code Module
title: "com.salesmanager.core.business.services.reference.loader"
description: "com.salesmanager.core.business.services.reference.loader: ConfigurationModulesLoader, IntegrationModulesLoader, ZonesLoader"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java"
    sha256: "62591a166c6c10863d1ec77d092363a8f3db01e89a9cb7894d113273f8a4519f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/IntegrationModulesLoader.java"
    sha256: "93cc3c7d1023a58dbda48ab23d5e6c220c77ba87cf905f0c161728c851995002"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java"
    sha256: "c88f7d2769dc86f1e74f94a2a308b324a90d395ac445176452a9f9c096e94295"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.reference.loader

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/IntegrationModulesLoader.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java`

## Types
- `ConfigurationModulesLoader` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java:19`
- `IntegrationModulesLoader` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/IntegrationModulesLoader.java:18`
- `ZonesLoader` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:38`

## Fields
- `ConfigurationModulesLoader.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java:22`
- `IntegrationModulesLoader.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/IntegrationModulesLoader.java:22`
- `ZonesLoader.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:41`
- `ZonesLoader.languageService: LanguageService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:44`
- `ZonesLoader.countryService: CountryService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:47`
- `ZonesLoader.resourceResolver: ResourcePatternResolver` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:50`
- `ZonesLoader.PATH: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:52`
- `ZonesLoader.ALL_REGIONS: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:54`

## Functions and methods
- `ConfigurationModulesLoader.toJSONString(Map<String,IntegrationConfiguration>) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java:26`
- `ConfigurationModulesLoader.loadIntegrationConfigurations(String) -> Map<String,IntegrationConfiguration>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java:50`
- `IntegrationModulesLoader.loadIntegrationModules(String) -> List<IntegrationModule>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/IntegrationModulesLoader.java:25`
- `IntegrationModulesLoader.loadModule(Map) -> IntegrationModule` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/IntegrationModulesLoader.java:60`
- `ZonesLoader.loadIndividualZones() -> List<Map<String, Zone>>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:57`
- `ZonesLoader.loadFileContent(String) -> InputStream` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:139`
- `ZonesLoader.loadZones(String) -> Map<String, Zone>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:143`
- `ZonesLoader.mapZone(Language, Map<String, List<ZoneDescription>>, Map<String, Country>, Map<String, Zone>, Map<String, String>, Map<String, String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:239`
- `ZonesLoader.geZoneFiles(String) -> List<Resource>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:281`

## Depends on
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:46`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:43`

## Calls
- `ConfigurationModulesLoader.toJSONString` calls [com.salesmanager.core.model.system.IntegrationConfiguration](/modules/com.salesmanager.core.model.system.md) `IntegrationConfiguration.toJSONString` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ConfigurationModulesLoader.java:36`
- `ZonesLoader.loadIndividualZones` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.list` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:64`
- `ZonesLoader.loadZones` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.list` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/loader/ZonesLoader.java:145`
