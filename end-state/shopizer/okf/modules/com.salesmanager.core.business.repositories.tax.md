---
type: Code Module
title: "com.salesmanager.core.business.repositories.tax"
description: "com.salesmanager.core.business.repositories.tax: findByStore, findByCode, findByStoreAndCode, findByStore"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java"
    sha256: "4d3d2ae6a72729ce988e00336e94e61dd287b50b5897ad10b605a8c9bdc3a619"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java"
    sha256: "ecc9fa2edfdec978a61af99efee25fb80a636c6f3f81a8bab42100dc82c7eb43"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.tax

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java`

## Types
- `TaxClassRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java:10`
- `TaxRateRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:10`

## Functions and methods
- `TaxClassRepository.findByStore(Integer) -> List<TaxClass>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java:12`
- `TaxClassRepository.findByCode(String) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java:15`
- `TaxClassRepository.findByStoreAndCode(Integer, String) -> TaxClass` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxClassRepository.java:18`
- `TaxRateRepository.findByStore(Integer) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:12`
- `TaxRateRepository.findByStoreAndLanguage(Integer, Integer) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:15`
- `TaxRateRepository.findByStoreAndCode(Integer, String) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:18`
- `TaxRateRepository.findByStoreAndId(Integer, Long) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:21`
- `TaxRateRepository.findOne(Long) -> TaxRate` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:24`
- `TaxRateRepository.findByMerchantAndZoneAndCountryAndLanguage(Integer, Long, Integer, Integer) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:27`
- `TaxRateRepository.findByMerchantAndProvinceAndCountryAndLanguage(Integer, String, Integer, Integer) -> List<TaxRate>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/tax/TaxRateRepository.java:30`
