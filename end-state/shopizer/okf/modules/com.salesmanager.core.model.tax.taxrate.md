---
type: Code Module
title: "com.salesmanager.core.model.tax.taxrate"
description: "com.salesmanager.core.model.tax.taxrate: TaxRate, TaxRateDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java"
    sha256: "6c6ccb138a6c40e666ea64ddde4d10e8dfc65e212df490dd2479df21f27c0869"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRateDescription.java"
    sha256: "7e891108e6d5fa43b0532174ecd54f15d7a62b44b0f8710285e419a05f52e346"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.tax.taxrate

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRateDescription.java`

## Types
- `TaxRate` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:52`
- `TaxRateDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRateDescription.java:29`

## Fields
- `TaxRate.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:68`
- `TaxRate.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:71`
- `TaxRate.taxPriority: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:74`
- `TaxRate.taxRate: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:77`
- `TaxRate.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:81`
- `TaxRate.piggyback: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:85`
- `TaxRate.taxClass: TaxClass` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:89`
- `TaxRate.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:95`
- `TaxRate.descriptions: List<TaxRateDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:99`
- `TaxRate.country: Country` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:103`
- `TaxRate.zone: Zone` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:107`
- `TaxRate.stateProvince: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:110`
- `TaxRate.parent: TaxRate` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:114`
- `TaxRate.taxRates: List<TaxRate>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:117`
- `TaxRate.rateText: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:120`
- `TaxRateDescription.taxRate: TaxRate` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRateDescription.java:45`

## Functions and methods
- `TaxRate.getRateText() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:123`
- `TaxRate.setRateText(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:127`
- `TaxRate.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:134`
- `TaxRate.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:138`
- `TaxRate.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:142`
- `TaxRate.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:147`
- `TaxRate.getTaxPriority() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:152`
- `TaxRate.setTaxPriority(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:156`
- `TaxRate.getTaxRate() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:160`
- `TaxRate.setTaxRate(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:164`
- `TaxRate.isPiggyback() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:168`
- `TaxRate.setPiggyback(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:172`
- `TaxRate.getTaxClass() -> TaxClass` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:176`
- `TaxRate.setTaxClass(TaxClass) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:180`
- `TaxRate.getDescriptions() -> List<TaxRateDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:186`
- `TaxRate.setDescriptions(List<TaxRateDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:190`
- `TaxRate.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:196`
- `TaxRate.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:200`
- `TaxRate.setCountry(Country) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:204`
- `TaxRate.getCountry() -> Country` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:208`
- `TaxRate.setZone(Zone) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:212`
- `TaxRate.getZone() -> Zone` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:216`
- `TaxRate.setTaxRates(List<TaxRate>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:221`
- `TaxRate.getTaxRates() -> List<TaxRate>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:225`
- `TaxRate.setParent(TaxRate) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:229`
- `TaxRate.getParent() -> TaxRate` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:233`
- `TaxRate.setStateProvince(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:237`
- `TaxRate.getStateProvince() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:241`
- `TaxRate.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:245`
- `TaxRate.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:249`
- `TaxRateDescription.getTaxRate() -> TaxRate` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRateDescription.java:50`
- `TaxRateDescription.setTaxRate(TaxRate) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRateDescription.java:54`

## Depends on
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:70`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:93`
- [com.salesmanager.core.model.reference.country.Country](/modules/com.salesmanager.core.model.reference.country.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:101`
- [com.salesmanager.core.model.reference.zone.Zone](/modules/com.salesmanager.core.model.reference.zone.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:105`
- [com.salesmanager.core.model.tax.taxclass.TaxClass](/modules/com.salesmanager.core.model.tax.taxclass.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxrate/TaxRate.java:87`

## Tests
- `com.salesmanager.test.shop.integration.tax.TaxRateIntegrationTest`
