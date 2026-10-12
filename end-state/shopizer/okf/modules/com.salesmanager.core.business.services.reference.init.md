---
type: Code Module
title: "com.salesmanager.core.business.services.reference.init"
description: "com.salesmanager.core.business.services.reference.init: InitializationDatabaseImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabase.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabase.java"
    sha256: "b2943b565278192ac69f68717bb3f057a4e2a806e278350ec551ea14632901ed"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java"
    sha256: "ffb50b5ee7d9cf5e83835181d97c102ddc5b7e17d98a1418b69ce44a240b210e"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.reference.init

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabase.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java`

## Types
- `InitializationDatabase` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabase.java:5`
- `InitializationDatabaseImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:49`

## Fields
- `InitializationDatabaseImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:52`
- `InitializationDatabaseImpl.zoneService: ZoneService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:56`
- `InitializationDatabaseImpl.languageService: LanguageService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:59`
- `InitializationDatabaseImpl.countryService: CountryService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:62`
- `InitializationDatabaseImpl.currencyService: CurrencyService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:65`
- `InitializationDatabaseImpl.merchantService: MerchantStoreService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:68`
- `InitializationDatabaseImpl.productTypeService: ProductTypeService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:71`
- `InitializationDatabaseImpl.taxClassService: TaxClassService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:74`
- `InitializationDatabaseImpl.zonesLoader: ZonesLoader` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:77`
- `InitializationDatabaseImpl.modulesLoader: IntegrationModulesLoader` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:80`
- `InitializationDatabaseImpl.manufacturerService: ManufacturerService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:83`
- `InitializationDatabaseImpl.moduleConfigurationService: ModuleConfigurationService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:86`
- `InitializationDatabaseImpl.optinService: OptinService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:89`
- `InitializationDatabaseImpl.groupService: GroupService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:92`
- `InitializationDatabaseImpl.permissionService: PermissionService` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:95`
- `InitializationDatabaseImpl.name: String` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:97`

## Functions and methods
- `InitializationDatabase.isEmpty() -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabase.java:7`
- `InitializationDatabase.populate(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabase.java:9`
- `InitializationDatabaseImpl.isEmpty() -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:99`
- `InitializationDatabaseImpl.populate(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:103`
- `InitializationDatabaseImpl.createSecurityGroups() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:119`
- `InitializationDatabaseImpl.createCurrencies() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:245`
- `InitializationDatabaseImpl.createCountries() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:271`
- `InitializationDatabaseImpl.createZones() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:291`
- `InitializationDatabaseImpl.addZonesToDb(Map<String,Zone>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:338`
- `InitializationDatabaseImpl.createLanguages() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:369`
- `InitializationDatabaseImpl.createMerchant() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:377`
- `InitializationDatabaseImpl.createModules() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:440`
- `InitializationDatabaseImpl.createSubReferences() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:457`

## Depends on
- [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:82`
- [com.salesmanager.core.business.services.catalog.product.type.ProductTypeService](/modules/com.salesmanager.core.business.services.catalog.product.type.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:70`
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:67`
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:61`
- [com.salesmanager.core.business.services.reference.currency.CurrencyService](/modules/com.salesmanager.core.business.services.reference.currency.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:64`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:58`
- [com.salesmanager.core.business.services.reference.loader.IntegrationModulesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:79`
- [com.salesmanager.core.business.services.reference.loader.ZonesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:76`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:55`
- [com.salesmanager.core.business.services.system.ModuleConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:85`
- [com.salesmanager.core.business.services.system.optin.OptinService](/modules/com.salesmanager.core.business.services.system.optin.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:88`
- [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:73`
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:91`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:94`

## Calls
- `InitializationDatabaseImpl.addZonesToDb` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:354`
- `InitializationDatabaseImpl.addZonesToDb` calls [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `ZoneService.addDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:358`
- `InitializationDatabaseImpl.createCountries` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create`, `SalesManagerEntityService.list` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:278`
- `InitializationDatabaseImpl.createCountries` calls [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `CountryService.addCountryDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:285`
- `InitializationDatabaseImpl.createCurrencies` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:262`
- `InitializationDatabaseImpl.createLanguages` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:373`
- `InitializationDatabaseImpl.createMerchant` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:409`
- `InitializationDatabaseImpl.createModules` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:446`
- `InitializationDatabaseImpl.createModules` calls [com.salesmanager.core.business.services.reference.loader.IntegrationModulesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `IntegrationModulesLoader.loadIntegrationModules` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:444`
- `InitializationDatabaseImpl.createSecurityGroups` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:125`
- `InitializationDatabaseImpl.createSecurityGroups` calls [com.salesmanager.core.business.utils.SecurityGroupsBuilder](/modules/com.salesmanager.core.business.utils.md) `SecurityGroupsBuilder.addGroup`, `SecurityGroupsBuilder.build` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:173`
- `InitializationDatabaseImpl.createSubReferences` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:464`
- `InitializationDatabaseImpl.createZones` calls [com.salesmanager.core.business.services.reference.loader.ZonesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `ZonesLoader.loadIndividualZones`, `ZonesLoader.loadZones` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:326`
- `InitializationDatabaseImpl.isEmpty` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.count` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/init/InitializationDatabaseImpl.java:100`
