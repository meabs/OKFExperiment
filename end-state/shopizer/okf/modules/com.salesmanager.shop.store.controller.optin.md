---
type: Code Module
title: "com.salesmanager.shop.store.controller.optin"
description: "com.salesmanager.shop.store.controller.optin: OptinFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacade.java"
    sha256: "56fdd83000006d11bf73920773c868430e46ca2c0f8fa44ae7d2de22f3921412"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java"
    sha256: "cc015a571f28b5652356eaea55078356e1299d736ec93093215174120c7ee25c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.optin

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java`

## Types
- `OptinFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacade.java:8`
- `OptinFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:16`

## Fields
- `OptinFacadeImpl.optinService: OptinService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:20`
- `OptinFacadeImpl.readableOptinConverter: ReadableOptinMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:23`
- `OptinFacadeImpl.persistableOptinConverter: PersistableOptinMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:25`

## Functions and methods
- `OptinFacade.create(PersistableOptin, MerchantStore, Language) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacade.java:10`
- `OptinFacadeImpl.create(PersistableOptin, MerchantStore, Language) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:27`
- `OptinFacadeImpl.createOptin(Optin) -> Optin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:35`

## Depends on
- [com.salesmanager.core.business.services.system.optin.OptinService](/modules/com.salesmanager.core.business.services.system.optin.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:19`
- [com.salesmanager.shop.mapper.optin.PersistableOptinMapper](/modules/com.salesmanager.shop.mapper.optin.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:24`
- [com.salesmanager.shop.mapper.optin.ReadableOptinMapper](/modules/com.salesmanager.shop.mapper.optin.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:22`

## Calls
- `OptinFacadeImpl.create` calls [com.salesmanager.shop.mapper.optin.PersistableOptinMapper](/modules/com.salesmanager.shop.mapper.optin.md) `PersistableOptinMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:30`
- `OptinFacadeImpl.create` calls [com.salesmanager.shop.mapper.optin.ReadableOptinMapper](/modules/com.salesmanager.shop.mapper.optin.md) `ReadableOptinMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:32`
- `OptinFacadeImpl.createOptin` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/optin/OptinFacadeImpl.java:37`
