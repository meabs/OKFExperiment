---
type: Code Module
title: "com.salesmanager.core.model.tax"
description: "com.salesmanager.core.model.tax: TaxConfiguration, TaxItem"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxBasisCalculation.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxBasisCalculation.java"
    sha256: "11d974e31fd97dfbfa9fb1f0cb2596e7cb27c5f830dcbafc6ba23e113b5ea2d9"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java"
    sha256: "86df22d739eddb8fad7838f554f8ad0b70919d5ec6b0712e32b9abd12eea5ab0"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java"
    sha256: "923e4bb4f018a4fd5410eafd397c79a4f51f3e9092b1709892dd38a2a7c74365"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.tax

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxBasisCalculation.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java`

## Types
- `TaxBasisCalculation` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxBasisCalculation.java:3`
- `TaxConfiguration` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:11`
- `TaxItem` (class) extends [com.salesmanager.core.model.order.OrderTotalItem](/modules/com.salesmanager.core.model.order.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:6`

## Fields
- `TaxConfiguration.taxBasisCalculation: TaxBasisCalculation` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:13`
- `TaxConfiguration.collectTaxIfDifferentProvinceOfStoreCountry: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:15`
- `TaxConfiguration.collectTaxIfDifferentCountryOfStoreCountry: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:16`
- `TaxItem.label: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:12`
- `TaxItem.taxRate: TaxRate` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:13`

## Functions and methods
- `TaxConfiguration.toJSONString() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:18`
- `TaxConfiguration.setTaxBasisCalculation(TaxBasisCalculation) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:27`
- `TaxConfiguration.getTaxBasisCalculation() -> TaxBasisCalculation` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:31`
- `TaxConfiguration.setCollectTaxIfDifferentProvinceOfStoreCountry(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:35`
- `TaxConfiguration.isCollectTaxIfDifferentProvinceOfStoreCountry() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:40`
- `TaxConfiguration.setCollectTaxIfDifferentCountryOfStoreCountry(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:44`
- `TaxConfiguration.isCollectTaxIfDifferentCountryOfStoreCountry() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxConfiguration.java:49`
- `TaxItem.setLabel(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:15`
- `TaxItem.getLabel() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:19`
- `TaxItem.setTaxRate(TaxRate) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:23`
- `TaxItem.getTaxRate() -> TaxRate` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:27`

## Depends on
- [com.salesmanager.core.model.tax.taxrate.TaxRate](/modules/com.salesmanager.core.model.tax.taxrate.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/TaxItem.java:13`
