---
type: Code Module
title: "com.salesmanager.shop.store.controller.store.facade"
description: "com.salesmanager.shop.store.controller.store.facade: StoreFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java"
    sha256: "c17ff9a3ae326b241b8d2de0a71f50345c78998453da58038d9fe5a533803947"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java"
    sha256: "f26113c3221888ad1c7cff802f808f661004f9c536c72329ee02dd27a686c9f1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.store.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java`

## Types
- `StoreFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:23`
- `StoreFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:51`

## Fields
- `StoreFacadeImpl.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:55`
- `StoreFacadeImpl.merchantConfigurationService: MerchantConfigurationService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:58`
- `StoreFacadeImpl.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:61`
- `StoreFacadeImpl.contentService: ContentService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:64`
- `StoreFacadeImpl.persistableMerchantStorePopulator: PersistableMerchantStorePopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:67`
- `StoreFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:71`
- `StoreFacadeImpl.languageUtils: LanguageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:74`
- `StoreFacadeImpl.readableMerchantStorePopulator: ReadableMerchantStorePopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:77`
- `StoreFacadeImpl.LOG: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:79`

## Functions and methods
- `StoreFacade.getByCode(HttpServletRequest) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:32`
- `StoreFacade.get(String) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:34`
- `StoreFacade.getByCode(String) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:36`
- `StoreFacade.supportedLanguages(MerchantStore) -> List<Language>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:38`
- `StoreFacade.getByCode(String, String) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:40`
- `StoreFacade.getFullByCode(String, String) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:42`
- `StoreFacade.findAll(MerchantStoreCriteria, Language, int, int) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:44`
- `StoreFacade.getChildStores(Language, String, int, int) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:52`
- `StoreFacade.getByCode(String, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:54`
- `StoreFacade.getFullByCode(String, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:56`
- `StoreFacade.existByCode(String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:58`
- `StoreFacade.getByCriteria(MerchantStoreCriteria, Language) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:68`
- `StoreFacade.create(PersistableMerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:77`
- `StoreFacade.update(PersistableMerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:86`
- `StoreFacade.delete(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:93`
- `StoreFacade.getBrand(String) -> ReadableBrand` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:101`
- `StoreFacade.createBrand(String, PersistableBrand) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:109`
- `StoreFacade.deleteLogo(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:114`
- `StoreFacade.addStoreLogo(String, InputContentFile) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:122`
- `StoreFacade.getMerchantStoreNames(MerchantStoreCriteria) -> List<ReadableMerchantStore>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacade.java:129`
- `StoreFacadeImpl.getByCode(HttpServletRequest) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:81`
- `StoreFacadeImpl.get(String) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:90`
- `StoreFacadeImpl.getByCode(String, String) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:102`
- `StoreFacadeImpl.getFullByCode(String, String) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:108`
- `StoreFacadeImpl.getLanguage(String) -> Language` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:114`
- `StoreFacadeImpl.getByCode(String, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:118`
- `StoreFacadeImpl.getFullByCode(String, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:124`
- `StoreFacadeImpl.existByCode(String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:130`
- `StoreFacadeImpl.convertMerchantStoreToReadableMerchantStore(Language, MerchantStore) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:139`
- `StoreFacadeImpl.convertMerchantStoreToReadableMerchantStoreWithFullDetails(Language, MerchantStore) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:153`
- `StoreFacadeImpl.getMerchantStoreByCode(String) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:168`
- `StoreFacadeImpl.create(PersistableMerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:173`
- `StoreFacadeImpl.createMerchantStore(MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:190`
- `StoreFacadeImpl.convertPersistableMerchantStoreToMerchantStore(PersistableMerchantStore, Language) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:198`
- `StoreFacadeImpl.update(PersistableMerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:214`
- `StoreFacadeImpl.updateMerchantStore(MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:226`
- `StoreFacadeImpl.mergePersistableMerchantStoreToMerchantStore(PersistableMerchantStore, String, Language) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:235`
- `StoreFacadeImpl.getByCriteria(MerchantStoreCriteria, Language) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:250`
- `StoreFacadeImpl.getMerchantStoresByCriteria(MerchantStoreCriteria, Language) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:258`
- `StoreFacadeImpl.delete(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:282`
- `StoreFacadeImpl.getBrand(String) -> ReadableBrand` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:300`
- `StoreFacadeImpl.getMerchantConfigEntities(MerchantStore) -> List<MerchantConfigEntity>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:315`
- `StoreFacadeImpl.getMergeConfigurationsByStore(MerchantConfigurationType, MerchantStore) -> List<MerchantConfiguration>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:323`
- `StoreFacadeImpl.convertToMerchantConfigEntity(MerchantConfiguration) -> MerchantConfigEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:332`
- `StoreFacadeImpl.convertToMerchantConfiguration(MerchantConfigEntity, MerchantConfigurationType) -> MerchantConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:342`
- `StoreFacadeImpl.createReadableImage(String, String) -> ReadableImage` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:353`
- `StoreFacadeImpl.deleteLogo(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:360`
- `StoreFacadeImpl.getByCode(String) -> MerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:376`
- `StoreFacadeImpl.addStoreLogo(String, InputContentFile) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:381`
- `StoreFacadeImpl.addLogoToStore(String, InputContentFile) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:389`
- `StoreFacadeImpl.saveMerchantStore(MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:397`
- `StoreFacadeImpl.createBrand(String, PersistableBrand) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:406`
- `StoreFacadeImpl.getChildStores(Language, String, int, int) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:435`
- `StoreFacadeImpl.findAll(MerchantStoreCriteria, Language, int, int) -> ReadableMerchantStoreList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:480`
- `StoreFacadeImpl.convertStoreName(MerchantStore) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:521`
- `StoreFacadeImpl.getMerchantStoreNames(MerchantStoreCriteria) -> List<ReadableMerchantStore>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:529`
- `StoreFacadeImpl.supportedLanguages(MerchantStore) -> List<Language>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:560`

## Depends on
- [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:63`
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:54`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:60`
- [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:57`
- [com.salesmanager.shop.populator.store.PersistableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:66`
- [com.salesmanager.shop.populator.store.ReadableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:76`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:69`
- [com.salesmanager.shop.utils.LanguageUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:73`

## Calls
- `StoreFacadeImpl.addLogoToStore` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.addLogo` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:391`
- `StoreFacadeImpl.convertMerchantStoreToReadableMerchantStore` calls [com.salesmanager.shop.populator.store.ReadableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `ReadableMerchantStorePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:146`
- `StoreFacadeImpl.convertMerchantStoreToReadableMerchantStoreWithFullDetails` calls [com.salesmanager.shop.populator.store.ReadableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `ReadableMerchantStorePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:161`
- `StoreFacadeImpl.convertPersistableMerchantStoreToMerchantStore` calls [com.salesmanager.shop.populator.store.PersistableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `PersistableMerchantStorePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:207`
- `StoreFacadeImpl.create` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:185`
- `StoreFacadeImpl.createBrand` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:425`
- `StoreFacadeImpl.createBrand` calls [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `MerchantConfigurationService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:420`
- `StoreFacadeImpl.createMerchantStore` calls [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `MerchantStoreService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:192`
- `StoreFacadeImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:292`
- `StoreFacadeImpl.deleteLogo` calls [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `ContentService.removeFile` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:369`
- `StoreFacadeImpl.findAll` calls [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `MerchantStoreService.listAll`, `MerchantStoreService.listAllRetailers`, `MerchantStoreService.listByGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:498`
- `StoreFacadeImpl.getBrand` calls [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `ImageFilePath.buildStoreLogoFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:306`
- `StoreFacadeImpl.getChildStores` calls [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `MerchantStoreService.listChildren` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:450`
- `StoreFacadeImpl.getMerchantStoreNames` calls [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `MerchantStoreService.findAllStoreNames` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:542`
- `StoreFacadeImpl.getMergeConfigurationsByStore` calls [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `MerchantConfigurationService.listByType` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:326`
- `StoreFacadeImpl.mergePersistableMerchantStoreToMerchantStore` calls [com.salesmanager.shop.populator.store.PersistableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `PersistableMerchantStorePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:243`
- `StoreFacadeImpl.saveMerchantStore` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:399`
- `StoreFacadeImpl.update` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:220`
- `StoreFacadeImpl.updateMerchantStore` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/store/facade/StoreFacadeImpl.java:228`
