---
type: Code Module
title: "com.salesmanager.shop.populator.store"
description: "com.salesmanager.shop.populator.store: PersistableMerchantStorePopulator, ReadableMerchantStorePopulator, ReadableMerchantStorePopulatorWithDetails"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java"
    sha256: "9d8c408a5d5889ae0a97c217f2e962ef05763f1391888ead3f04e6ef70f96ade"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java"
    sha256: "079a47a39bde281648db290db2b1e8cc9f1641a4e23dd7950925f63138f85e76"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulatorWithDetails.java"
    sha256: "25b928a7b2491ae6b56c710eb3260647423ebccd7bfbf0141d05973f7cd07943"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.populator.store

Source: `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulatorWithDetails.java`

## Types
- `PersistableMerchantStorePopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:31`
- `ReadableMerchantStorePopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:41`
- `ReadableMerchantStorePopulatorWithDetails` (class) extends [com.salesmanager.shop.populator.store.ReadableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulatorWithDetails.java:16`

## Fields
- `PersistableMerchantStorePopulator.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:35`
- `PersistableMerchantStorePopulator.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:37`
- `PersistableMerchantStorePopulator.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:39`
- `PersistableMerchantStorePopulator.currencyService: CurrencyService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:41`
- `PersistableMerchantStorePopulator.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:43`
- `ReadableMerchantStorePopulator.logger: Log` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:45`
- `ReadableMerchantStorePopulator.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:48`
- `ReadableMerchantStorePopulator.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:50`
- `ReadableMerchantStorePopulator.filePath: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:53`
- `ReadableMerchantStorePopulator.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:55`
- `ReadableMerchantStorePopulatorWithDetails.logger: Log` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulatorWithDetails.java:19`

## Functions and methods
- `PersistableMerchantStorePopulator.populate(PersistableMerchantStore, MerchantStore, MerchantStore, Language) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:46`
- `PersistableMerchantStorePopulator.createTarget() -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:160`
- `PersistableMerchantStorePopulator.getZoneService() -> ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:166`
- `PersistableMerchantStorePopulator.setZoneService(ZoneService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:170`
- `PersistableMerchantStorePopulator.getCountryService() -> CountryService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:173`
- `PersistableMerchantStorePopulator.setCountryService(CountryService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:177`
- `PersistableMerchantStorePopulator.getLanguageService() -> LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:181`
- `PersistableMerchantStorePopulator.setLanguageService(LanguageService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:185`
- `PersistableMerchantStorePopulator.getCurrencyService() -> CurrencyService` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:189`
- `PersistableMerchantStorePopulator.setCurrencyService(CurrencyService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:193`
- `ReadableMerchantStorePopulator.populate(MerchantStore, ReadableMerchantStore, MerchantStore, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:59`
- `ReadableMerchantStorePopulator.createTarget() -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:180`
- `ReadableMerchantStorePopulatorWithDetails.populate(MerchantStore, ReadableMerchantStore, MerchantStore, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulatorWithDetails.java:21`
- `ReadableMerchantStorePopulatorWithDetails.createTarget() -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulatorWithDetails.java:35`

## Depends on
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:42`
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:34`
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:47`
- [com.salesmanager.core.business.services.reference.currency.CurrencyService](/modules/com.salesmanager.core.business.services.reference.currency.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:40`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:38`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:54`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/PersistableMerchantStorePopulator.java:36`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:49`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:51`

## Calls
- `ReadableMerchantStorePopulator.populate` calls [com.salesmanager.shop.model.references.MeasureUnit](/modules/com.salesmanager.shop.model.references.md) `MeasureUnit.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:107`
- `ReadableMerchantStorePopulator.populate` calls [com.salesmanager.shop.model.references.WeightUnit](/modules/com.salesmanager.shop.model.references.md) `WeightUnit.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:108`
- `ReadableMerchantStorePopulator.populate` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.formatDate` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:142`
- `ReadableMerchantStorePopulator.populate` calls [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `ImageFilePath.buildStoreLogoFilePath` `sm-shop/src/main/java/com/salesmanager/shop/populator/store/ReadableMerchantStorePopulator.java:129`
