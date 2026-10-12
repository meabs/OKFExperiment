---
type: Code Module
title: "com.salesmanager.shop.store.facade.tax"
description: "com.salesmanager.shop.store.facade.tax: TaxFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java"
    sha256: "118dcd01dd8b2a6473e9c1c73e693c9c145ec4eaa1703554e4610aec44267b42"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.tax

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java`

## Types
- `TaxFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:35`

## Fields
- `TaxFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:38`
- `TaxFacadeImpl.taxClassService: TaxClassService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:42`
- `TaxFacadeImpl.taxRateService: TaxRateService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:45`
- `TaxFacadeImpl.persistableTaxClassMapper: PersistableTaxClassMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:48`
- `TaxFacadeImpl.readableTaxClassMapper: ReadableTaxClassMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:51`
- `TaxFacadeImpl.persistableTaxRateMapper: PersistableTaxRateMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:54`
- `TaxFacadeImpl.readableTaxRateMapper: ReadableTaxRateMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:57`

## Functions and methods
- `TaxFacadeImpl.createTaxClass(PersistableTaxClass, MerchantStore, Language) -> Entity` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:59`
- `TaxFacadeImpl.deleteTaxClass(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:85`
- `TaxFacadeImpl.taxClasses(MerchantStore, Language) -> ReadableEntityList<ReadableTaxClass>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:108`
- `TaxFacadeImpl.convertToReadableTaxClass(TaxClass, MerchantStore, Language) -> ReadableTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:131`
- `TaxFacadeImpl.updateTaxClass(Long, PersistableTaxClass, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:135`
- `TaxFacadeImpl.taxClass(String, MerchantStore, Language) -> ReadableTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:158`
- `TaxFacadeImpl.existsTaxClass(String, MerchantStore, Language) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:183`
- `TaxFacadeImpl.taxRateByCode(String, MerchantStore, Language) -> TaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:196`
- `TaxFacadeImpl.taxRateById(Long, MerchantStore, Language) -> TaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:221`
- `TaxFacadeImpl.deleteTaxRate(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:241`
- `TaxFacadeImpl.taxRate(Long, MerchantStore, Language) -> ReadableTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:253`
- `TaxFacadeImpl.createTaxRate(PersistableTaxRate, MerchantStore, Language) -> Entity` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:260`
- `TaxFacadeImpl.updateTaxRate(Long, PersistableTaxRate, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:293`
- `TaxFacadeImpl.existsTaxRate(String, MerchantStore, Language) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:316`
- `TaxFacadeImpl.taxRates(MerchantStore, Language) -> ReadableEntityList<ReadableTaxRate>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:330`

## Depends on
- [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:41`
- [com.salesmanager.core.business.services.tax.TaxRateService](/modules/com.salesmanager.core.business.services.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:44`
- [com.salesmanager.shop.mapper.tax.PersistableTaxClassMapper](/modules/com.salesmanager.shop.mapper.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:47`
- [com.salesmanager.shop.mapper.tax.PersistableTaxRateMapper](/modules/com.salesmanager.shop.mapper.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:53`
- [com.salesmanager.shop.mapper.tax.ReadableTaxClassMapper](/modules/com.salesmanager.shop.mapper.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:50`
- [com.salesmanager.shop.mapper.tax.ReadableTaxRateMapper](/modules/com.salesmanager.shop.mapper.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:56`

## Calls
- `TaxFacadeImpl.convertToReadableTaxClass` calls [com.salesmanager.shop.mapper.tax.ReadableTaxClassMapper](/modules/com.salesmanager.shop.mapper.tax.md) `ReadableTaxClassMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:132`
- `TaxFacadeImpl.createTaxClass` calls [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `TaxClassService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:73`
- `TaxFacadeImpl.createTaxClass` calls [com.salesmanager.shop.mapper.tax.PersistableTaxClassMapper](/modules/com.salesmanager.shop.mapper.tax.md) `PersistableTaxClassMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:72`
- `TaxFacadeImpl.createTaxRate` calls [com.salesmanager.core.business.services.tax.TaxRateService](/modules/com.salesmanager.core.business.services.tax.md) `TaxRateService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:280`
- `TaxFacadeImpl.createTaxRate` calls [com.salesmanager.shop.mapper.tax.PersistableTaxRateMapper](/modules/com.salesmanager.shop.mapper.tax.md) `PersistableTaxRateMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:278`
- `TaxFacadeImpl.deleteTaxClass` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:99`
- `TaxFacadeImpl.deleteTaxRate` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:245`
- `TaxFacadeImpl.existsTaxClass` calls [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `TaxClassService.exists` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:186`
- `TaxFacadeImpl.taxClass` calls [com.salesmanager.shop.mapper.tax.ReadableTaxClassMapper](/modules/com.salesmanager.shop.mapper.tax.md) `ReadableTaxClassMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:175`
- `TaxFacadeImpl.taxClasses` calls [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `TaxClassService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:113`
- `TaxFacadeImpl.taxRate` calls [com.salesmanager.shop.mapper.tax.ReadableTaxRateMapper](/modules/com.salesmanager.shop.mapper.tax.md) `ReadableTaxRateMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:257`
- `TaxFacadeImpl.taxRates` calls [com.salesmanager.core.business.services.tax.TaxRateService](/modules/com.salesmanager.core.business.services.tax.md) `TaxRateService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:337`
- `TaxFacadeImpl.taxRates` calls [com.salesmanager.shop.mapper.tax.ReadableTaxRateMapper](/modules/com.salesmanager.shop.mapper.tax.md) `ReadableTaxRateMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:338`
- `TaxFacadeImpl.updateTaxClass` calls [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `TaxClassService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:150`
- `TaxFacadeImpl.updateTaxClass` calls [com.salesmanager.shop.mapper.tax.PersistableTaxClassMapper](/modules/com.salesmanager.shop.mapper.tax.md) `PersistableTaxClassMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:149`
- `TaxFacadeImpl.updateTaxRate` calls [com.salesmanager.core.business.services.tax.TaxRateService](/modules/com.salesmanager.core.business.services.tax.md) `TaxRateService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:306`
- `TaxFacadeImpl.updateTaxRate` calls [com.salesmanager.shop.mapper.tax.PersistableTaxRateMapper](/modules/com.salesmanager.shop.mapper.tax.md) `PersistableTaxRateMapper.merge` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/tax/TaxFacadeImpl.java:303`
