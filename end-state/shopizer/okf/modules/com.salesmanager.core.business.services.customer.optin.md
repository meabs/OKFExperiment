---
type: Code Module
title: "com.salesmanager.core.business.services.customer.optin"
description: "com.salesmanager.core.business.services.customer.optin: CustomerOptinServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java"
    sha256: "4f707954c3b6e544d9431402487ebbd846d95622747bc003f0b1511f9553a8e6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java"
    sha256: "5c30c3c69cc511b499f651c5600c1d1d859cbb8a64a8ce54e02d53dbb5b512a2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.customer.optin

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java`

## Types
- `CustomerOptinService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java:14`
- `CustomerOptinServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:17`

## Fields
- `CustomerOptinServiceImpl.customerOptinRepository: CustomerOptinRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:21`

## Functions and methods
- `CustomerOptinService.optinCumtomer(CustomerOptin) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java:22`
- `CustomerOptinService.optoutCumtomer(CustomerOptin) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java:30`
- `CustomerOptinService.findByEmailAddress(MerchantStore, String, String) -> CustomerOptin` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinService.java:40`
- `CustomerOptinServiceImpl.optinCumtomer(CustomerOptin) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:30`
- `CustomerOptinServiceImpl.optoutCumtomer(CustomerOptin) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:39`
- `CustomerOptinServiceImpl.findByEmailAddress(MerchantStore, String, String) -> CustomerOptin` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:47`

## Depends on
- [com.salesmanager.core.business.repositories.customer.optin.CustomerOptinRepository](/modules/com.salesmanager.core.business.repositories.customer.optin.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:21`

## Calls
- `CustomerOptinServiceImpl.findByEmailAddress` calls [com.salesmanager.core.business.repositories.customer.optin.CustomerOptinRepository](/modules/com.salesmanager.core.business.repositories.customer.optin.md) `CustomerOptinRepository.findByMerchantAndCodeAndEmail` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:49`
- `CustomerOptinServiceImpl.optinCumtomer` calls [com.salesmanager.core.business.repositories.customer.optin.CustomerOptinRepository](/modules/com.salesmanager.core.business.repositories.customer.optin.md) `CustomerOptinRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:34`
- `CustomerOptinServiceImpl.optoutCumtomer` calls [com.salesmanager.core.business.repositories.customer.optin.CustomerOptinRepository](/modules/com.salesmanager.core.business.repositories.customer.optin.md) `CustomerOptinRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/optin/CustomerOptinServiceImpl.java:43`
