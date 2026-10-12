---
type: Code Module
title: "com.salesmanager.core.model.system.optin"
description: "com.salesmanager.core.model.system.optin: CustomerOptin, Optin"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java"
    sha256: "38b7d82a600b93b9d67e08949f048557560c786ca428ef030575a517f83186ca"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java"
    sha256: "60b48ad8dc635d4f71ce1eb00c14f1f6a8d331f8c12cbe25ede2c4a7f57f50e6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/OptinType.java"
    sha256: "f1318fb326aeab45fc1a2cd1df6a4763d5f3ad4507a0383b3d224107b61868b6"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.system.optin

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/OptinType.java`

## Types
- `CustomerOptin` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:34`
- `Optin` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:33`
- `OptinType` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/OptinType.java:3`

## Fields
- `CustomerOptin.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:51`
- `CustomerOptin.optinDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:55`
- `CustomerOptin.optin: Optin` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:60`
- `CustomerOptin.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:64`
- `CustomerOptin.firstName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:67`
- `CustomerOptin.lastName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:70`
- `CustomerOptin.email: String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:73`
- `CustomerOptin.value: String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:77`
- `Optin.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:50`
- `Optin.startDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:54`
- `Optin.endDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:58`
- `Optin.optinType: OptinType` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:62`
- `Optin.merchant: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:66`
- `Optin.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:69`
- `Optin.description: String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:72`

## Functions and methods
- `CustomerOptin.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:79`
- `CustomerOptin.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:84`
- `CustomerOptin.getOptinDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:89`
- `CustomerOptin.setOptinDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:93`
- `CustomerOptin.getOptin() -> Optin` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:97`
- `CustomerOptin.setOptin(Optin) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:101`
- `CustomerOptin.getFirstName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:105`
- `CustomerOptin.setFirstName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:109`
- `CustomerOptin.getLastName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:113`
- `CustomerOptin.setLastName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:117`
- `CustomerOptin.getEmail() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:121`
- `CustomerOptin.setEmail(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:125`
- `CustomerOptin.getValue() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:129`
- `CustomerOptin.setValue(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:133`
- `CustomerOptin.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:137`
- `CustomerOptin.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:141`
- `Optin.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:75`
- `Optin.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:80`
- `Optin.getStartDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:85`
- `Optin.setStartDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:89`
- `Optin.getEndDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:93`
- `Optin.setEndDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:97`
- `Optin.getMerchant() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:101`
- `Optin.setMerchant(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:105`
- `Optin.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:109`
- `Optin.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:113`
- `Optin.getDescription() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:117`
- `Optin.setDescription(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:121`
- `Optin.getOptinType() -> OptinType` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:125`
- `Optin.setOptinType(OptinType) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:129`

## Depends on
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/CustomerOptin.java:62`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/system/optin/Optin.java:64`
