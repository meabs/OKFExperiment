---
type: Code Module
title: "com.salesmanager.shop.store.controller.shipping.facade"
description: "com.salesmanager.shop.store.controller.shipping.facade: ShippingFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java"
    sha256: "a7ecd0d27d68e03aa0de75783f408f5f81ded120ef7e361dc4474cb698d9e076"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingModuleConfigurationFacade.java"
    sha256: "b7966bbc8797f02e330d109370be762715639e952adc59f4754100c2c02eb47c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java"
    sha256: "322b0b79b75fccc110f9782a698b3cf43bcf243b74ec6174fb1bdd30011c6a7c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.shipping.facade

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingModuleConfigurationFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java`

## Types
- `ShippingFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:13`
- `ShippingModuleConfigurationFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingModuleConfigurationFacade.java:3`
- `ShippingFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:40`

## Fields
- `ShippingFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:43`
- `ShippingFacadeImpl.shippingOriginService: ShippingOriginService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:46`
- `ShippingFacadeImpl.shippingService: ShippingService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:49`
- `ShippingFacadeImpl.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:52`
- `ShippingFacadeImpl.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:55`

## Functions and methods
- `ShippingFacade.getExpeditionConfiguration(MerchantStore, Language) -> ExpeditionConfiguration` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:15`
- `ShippingFacade.saveExpeditionConfiguration(ExpeditionConfiguration, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:16`
- `ShippingFacade.getShippingOrigin(MerchantStore) -> ReadableAddress` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:19`
- `ShippingFacade.saveShippingOrigin(PersistableAddress, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:20`
- `ShippingFacade.createPackage(PackageDetails, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:23`
- `ShippingFacade.getPackage(String, MerchantStore) -> PackageDetails` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:25`
- `ShippingFacade.shipToCountry(MerchantStore, Language) -> List<ReadableCountry>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:33`
- `ShippingFacade.listPackages(MerchantStore) -> List<PackageDetails>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:35`
- `ShippingFacade.updatePackage(String, PackageDetails, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:37`
- `ShippingFacade.deletePackage(String, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacade.java:39`
- `ShippingFacadeImpl.getExpeditionConfiguration(MerchantStore, Language) -> ExpeditionConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:60`
- `ShippingFacadeImpl.saveExpeditionConfiguration(ExpeditionConfiguration, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:89`
- `ShippingFacadeImpl.saveShippingConfiguration(ShippingConfiguration, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:110`
- `ShippingFacadeImpl.getShippingOrigin(MerchantStore) -> ReadableAddress` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:119`
- `ShippingFacadeImpl.saveShippingOrigin(PersistableAddress, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:146`
- `ShippingFacadeImpl.getDbConfig(MerchantStore) -> ShippingConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:179`
- `ShippingFacadeImpl.createPackage(PackageDetails, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:197`
- `ShippingFacadeImpl.packageExists(ShippingConfiguration, PackageDetails) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:216`
- `ShippingFacadeImpl.packageDetails(ShippingConfiguration, String) -> com.salesmanager.core.model.shipping.Package` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:233`
- `ShippingFacadeImpl.getPackage(String, MerchantStore) -> PackageDetails` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:249`
- `ShippingFacadeImpl.listPackages(MerchantStore) -> List<PackageDetails>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:265`
- `ShippingFacadeImpl.updatePackage(String, PackageDetails, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:274`
- `ShippingFacadeImpl.deletePackage(String, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:300`
- `ShippingFacadeImpl.toPackageDetails(com.salesmanager.core.model.shipping.Package) -> PackageDetails` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:320`
- `ShippingFacadeImpl.toPackage(PackageDetails) -> com.salesmanager.core.model.shipping.Package` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:334`
- `ShippingFacadeImpl.shipToCountry(MerchantStore, Language) -> List<ReadableCountry>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:348`
- `ShippingFacadeImpl.convert(Country, MerchantStore, Language) -> ReadableCountry` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:382`

## Depends on
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:51`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:54`
- [com.salesmanager.core.business.services.shipping.ShippingOriginService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:45`
- [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:48`

## Calls
- `ShippingFacadeImpl.convert` calls [com.salesmanager.shop.populator.references.ReadableCountryPopulator](/modules/com.salesmanager.shop.populator.references.md) `ReadableCountryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:384`
- `ShippingFacadeImpl.saveShippingConfiguration` calls [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `ShippingService.saveShippingConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:112`
- `ShippingFacadeImpl.saveShippingOrigin` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:169`
- `ShippingFacadeImpl.toPackage` calls [com.salesmanager.core.model.shipping.ShippingPackageType](/modules/com.salesmanager.core.model.shipping.md) `ShippingPackageType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/shipping/facade/ShippingFacadeImpl.java:344`
