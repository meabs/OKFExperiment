---
type: Code Module
title: "com.salesmanager.core.business.services.system.optin"
description: "com.salesmanager.core.business.services.system.optin: OptinServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinService.java"
    sha256: "7f43024452afda7dddbc5abdef308bdf7771fdea030f1a90262cdb6194f3b8d0"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java"
    sha256: "f1780728f5ce38b3843017f3ad1626bfbd14c68bb79d4be29cb6288133751ff5"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.system.optin

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java`

## Types
- `OptinService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinService.java:14`
- `OptinServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:14`

## Fields
- `OptinServiceImpl.optinRepository: OptinRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:18`

## Functions and methods
- `OptinService.getOptinByMerchantAndType(MerchantStore, OptinType) -> Optin` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinService.java:17`
- `OptinService.getOptinByCode(MerchantStore, String) -> Optin` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinService.java:18`
- `OptinServiceImpl.getOptinByCode(MerchantStore, String) -> Optin` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:27`
- `OptinServiceImpl.getOptinByMerchantAndType(MerchantStore, OptinType) -> Optin` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:32`

## Depends on
- [com.salesmanager.core.business.repositories.system.OptinRepository](/modules/com.salesmanager.core.business.repositories.system.md) `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:18`

## Calls
- `OptinServiceImpl.getOptinByCode` calls [com.salesmanager.core.business.repositories.system.OptinRepository](/modules/com.salesmanager.core.business.repositories.system.md) `OptinRepository.findByMerchantAndCode` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:29`
- `OptinServiceImpl.getOptinByMerchantAndType` calls [com.salesmanager.core.business.repositories.system.OptinRepository](/modules/com.salesmanager.core.business.repositories.system.md) `OptinRepository.findByMerchantAndType` `sm-core/src/main/java/com/salesmanager/core/business/services/system/optin/OptinServiceImpl.java:34`
