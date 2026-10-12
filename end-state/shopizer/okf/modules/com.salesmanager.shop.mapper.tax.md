---
type: Code Module
title: "com.salesmanager.shop.mapper.tax"
description: "com.salesmanager.shop.mapper.tax: PersistableTaxClassMapper, PersistableTaxRateMapper, ReadableTaxClassMapper, ReadableTaxRateMapper"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxClassMapper.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxClassMapper.java"
    sha256: "b206fb0b08f85d4cc8e5c70928ad10d67bd597e0aca5bd54b9a056fbf5ce934c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java"
    sha256: "a9d283734fdaf73ad541ed9dbf8f6fed6839d11fd162b7712d4a3facb0665bf7"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxClassMapper.java"
    sha256: "00b362693a3210d73035c99b450ef10931f31e140b9863c01120cb867b521182"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java"
    sha256: "ea8da243910c2003849497175d7762d456d717f2d3b67feb73f37a02346019b4"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.mapper.tax

Source: `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxClassMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxClassMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java`

## Types
- `PersistableTaxClassMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxClassMapper.java:12`
- `PersistableTaxRateMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:21`
- `ReadableTaxClassMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxClassMapper.java:11`
- `ReadableTaxRateMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java:17`

## Fields
- `PersistableTaxRateMapper.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:26`
- `PersistableTaxRateMapper.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:29`
- `PersistableTaxRateMapper.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:32`
- `PersistableTaxRateMapper.taxClassService: TaxClassService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:35`

## Functions and methods
- `PersistableTaxClassMapper.convert(PersistableTaxClass, MerchantStore, Language) -> TaxClass` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxClassMapper.java:15`
- `PersistableTaxClassMapper.merge(PersistableTaxClass, TaxClass, MerchantStore, Language) -> TaxClass` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxClassMapper.java:26`
- `PersistableTaxRateMapper.convert(PersistableTaxRate, MerchantStore, Language) -> TaxRate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:37`
- `PersistableTaxRateMapper.merge(PersistableTaxRate, TaxRate, MerchantStore, Language) -> TaxRate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:43`
- `PersistableTaxRateMapper.taxRate(com.salesmanager.core.model.tax.taxrate.TaxRate, PersistableTaxRate) -> com.salesmanager.core.model.tax.taxrate.TaxRate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:71`
- `PersistableTaxRateMapper.description(TaxRateDescription) -> com.salesmanager.core.model.tax.taxrate.TaxRateDescription` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:100`
- `ReadableTaxClassMapper.convert(TaxClass, MerchantStore, Language) -> ReadableTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxClassMapper.java:14`
- `ReadableTaxClassMapper.merge(TaxClass, ReadableTaxClass, MerchantStore, Language) -> ReadableTaxClass` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxClassMapper.java:24`
- `ReadableTaxRateMapper.convert(TaxRate, MerchantStore, Language) -> ReadableTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java:20`
- `ReadableTaxRateMapper.merge(TaxRate, ReadableTaxRate, MerchantStore, Language) -> ReadableTaxRate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java:27`
- `ReadableTaxRateMapper.convertDescription(List<TaxRateDescription>, Language) -> Optional<ReadableTaxRateDescription>` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java:45`
- `ReadableTaxRateMapper.convertDescription(TaxRateDescription) -> ReadableTaxRateDescription` `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/ReadableTaxRateMapper.java:59`

## Depends on
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:25`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:31`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:28`
- [com.salesmanager.core.business.services.tax.TaxClassService](/modules/com.salesmanager.core.business.services.tax.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/tax/PersistableTaxRateMapper.java:34`
