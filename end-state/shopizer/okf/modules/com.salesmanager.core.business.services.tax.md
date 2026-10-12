---
type: Code Module
title: "com.salesmanager.core.business.services.tax"
description: "com.salesmanager.core.business.services.tax: TaxClassServiceImpl, TaxRateServiceImpl, TaxServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java"
    sha256: "d11fb50b6aec19104974791f142c06cd0080fe88c78dff13e0d985e4d98be385"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java"
    sha256: "960a6532e307aba93a7b68fcb38ee32d7c29ddaa43d1f7e9905e1ff37183a1ea"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java"
    sha256: "e72c750c1ee72229227e01b113835b6fda51be89779fee91e6730c3e451fed78"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java"
    sha256: "cd07c0223b2645b2d93c54de747bfe079fd7c290b3e6b9ab500f7c2f4e117c60"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxService.java"
    sha256: "d09b7cd92a7c9f09ba23c72da524a7edf077dc7b26769a1acb1b54b6ff630ed6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java"
    sha256: "ff26b8f4ce57353c41e370d19292f73a5ace4df5f74e2db0ff85a41cf54935e3"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.tax

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java`

## Types
- `TaxClassService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java:10`
- `TaxClassServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:16`
- `TaxRateService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:14`
- `TaxRateServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:19`
- `TaxService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxService.java:14`
- `TaxServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:37`

## Fields
- `TaxClassServiceImpl.taxClassRepository: TaxClassRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:20`
- `TaxRateServiceImpl.taxRateRepository: TaxRateRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:23`
- `TaxServiceImpl.TAX_CONFIGURATION: String` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:41`
- `TaxServiceImpl.DEFAULT_TAX_CLASS: String` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:42`
- `TaxServiceImpl.merchantConfigurationService: MerchantConfigurationService` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:45`
- `TaxServiceImpl.taxRateService: TaxRateService` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:48`
- `TaxServiceImpl.taxClassService: TaxClassService` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:51`

## Functions and methods
- `TaxClassService.listByStore(MerchantStore) -> List<TaxClass>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java:12`
- `TaxClassService.getByCode(String) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java:14`
- `TaxClassService.getByCode(String, MerchantStore) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java:16`
- `TaxClassService.exists(String, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java:19`
- `TaxClassService.saveOrUpdate(TaxClass) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassService.java:21`
- `TaxClassServiceImpl.listByStore(MerchantStore) -> List<TaxClass>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:29`
- `TaxClassServiceImpl.getByCode(String) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:34`
- `TaxClassServiceImpl.getByCode(String, MerchantStore) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:39`
- `TaxClassServiceImpl.delete(TaxClass) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:44`
- `TaxClassServiceImpl.getById(Long) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:52`
- `TaxClassServiceImpl.exists(String, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:57`
- `TaxClassServiceImpl.saveOrUpdate(TaxClass) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:66`
- `TaxRateService.listByStore(MerchantStore) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:16`
- `TaxRateService.listByCountryZoneAndTaxClass(Country, Zone, TaxClass, MerchantStore, Language) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:18`
- `TaxRateService.listByCountryStateProvinceAndTaxClass(Country, String, TaxClass, MerchantStore, Language) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:22`
- `TaxRateService.getByCode(String, MerchantStore) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:26`
- `TaxRateService.getById(Long, MerchantStore) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:29`
- `TaxRateService.listByStore(MerchantStore, Language) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:32`
- `TaxRateService.saveOrUpdate(TaxRate) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateService.java:35`
- `TaxRateServiceImpl.listByStore(MerchantStore) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:31`
- `TaxRateServiceImpl.listByStore(MerchantStore, Language) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:37`
- `TaxRateServiceImpl.getByCode(String, MerchantStore) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:44`
- `TaxRateServiceImpl.listByCountryZoneAndTaxClass(Country, Zone, TaxClass, MerchantStore, Language) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:50`
- `TaxRateServiceImpl.listByCountryStateProvinceAndTaxClass(Country, String, TaxClass, MerchantStore, Language) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:55`
- `TaxRateServiceImpl.delete(TaxRate) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:60`
- `TaxRateServiceImpl.saveOrUpdate(TaxRate) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:67`
- `TaxRateServiceImpl.getById(Long, MerchantStore) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:77`
- `TaxService.getTaxConfiguration(MerchantStore) -> TaxConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxService.java:22`
- `TaxService.saveTaxConfiguration(TaxConfiguration, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxService.java:31`
- `TaxService.calculateTax(OrderSummary, Customer, MerchantStore, Language) -> List<TaxItem>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxService.java:43`
- `TaxServiceImpl.getTaxConfiguration(MerchantStore) -> TaxConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:53`
- `TaxServiceImpl.saveTaxConfiguration(TaxConfiguration, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:74`
- `TaxServiceImpl.calculateTax(OrderSummary, Customer, MerchantStore, Language) -> List<TaxItem>` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:91`

## Depends on
- [com.salesmanager.core.business.repositories.tax.TaxClassRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:20`
- [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:23`
- [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:44`

## Calls
- `TaxClassServiceImpl.exists` calls [com.salesmanager.core.business.repositories.tax.TaxClassRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxClassRepository.findByStoreAndCode` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:62`
- `TaxClassServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.tax.TaxClassRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxClassRepository.findByCode`, `TaxClassRepository.findByStoreAndCode` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:36`
- `TaxClassServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.tax.TaxClassRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxClassRepository.findByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxClassServiceImpl.java:31`
- `TaxRateServiceImpl.delete` calls [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxRateRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:63`
- `TaxRateServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxRateRepository.findByStoreAndCode` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:47`
- `TaxRateServiceImpl.getById` calls [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxRateRepository.findByStoreAndId` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:79`
- `TaxRateServiceImpl.listByCountryStateProvinceAndTaxClass` calls [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxRateRepository.findByMerchantAndProvinceAndCountryAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:57`
- `TaxRateServiceImpl.listByCountryZoneAndTaxClass` calls [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxRateRepository.findByMerchantAndZoneAndCountryAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:52`
- `TaxRateServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.tax.TaxRateRepository](/modules/com.salesmanager.core.business.repositories.tax.md) `TaxRateRepository.findByStore`, `TaxRateRepository.findByStoreAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxRateServiceImpl.java:34`
- `TaxServiceImpl.calculateTax` calls [com.salesmanager.core.model.tax.TaxBasisCalculation](/modules/com.salesmanager.core.model.tax.md) `TaxBasisCalculation.name` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:119`
- `TaxServiceImpl.saveTaxConfiguration` calls [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `MerchantConfigurationService.saveOrUpdate` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:87`
- `TaxServiceImpl.saveTaxConfiguration` calls [com.salesmanager.core.model.tax.TaxConfiguration](/modules/com.salesmanager.core.model.tax.md) `TaxConfiguration.toJSONString` `sm-core/src/main/java/com/salesmanager/core/business/services/tax/TaxServiceImpl.java:85`
