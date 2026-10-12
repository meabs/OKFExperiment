---
type: Code Module
title: "com.salesmanager.shop.init.data"
description: "com.salesmanager.shop.init.data: InitializationLoader"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/init/data/InitData.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/init/data/InitData.java"
    sha256: "3c86abfeed9f51af40325ff0b307bb2c6831f5e981726dcd08bf51cf6aac3731"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java"
    sha256: "7c85c89be0341f1c0c889abf180b2f944ccafe631db5ffefc957a17f28b3c40f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.init.data

Source: `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitData.java`, `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java`

## Types
- `InitData` (interface) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitData.java:5`
- `InitializationLoader` (class) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:28`

## Fields
- `InitializationLoader.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:31`
- `InitializationLoader.initDefaultData: boolean` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:34`
- `InitializationLoader.merchantConfigurationService: MerchantConfigurationService` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:38`
- `InitializationLoader.initializationDatabase: InitializationDatabase` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:41`
- `InitializationLoader.systemConfigurationService: SystemConfigurationService` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:47`
- `InitializationLoader.userDetailsService: WebUserServices` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:50`
- `InitializationLoader.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:53`
- `InitializationLoader.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:56`
- `InitializationLoader.configuration: CoreConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:59`
- `InitializationLoader.merchantService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:62`

## Functions and methods
- `InitData.initInitialData() -> void` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitData.java:7`
- `InitializationLoader.init() -> void` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:65`

## Depends on
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:61`
- [com.salesmanager.core.business.services.reference.init.InitializationDatabase](/modules/com.salesmanager.core.business.services.reference.init.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:40`
- [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:37`
- [com.salesmanager.core.business.services.system.SystemConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:46`
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:55`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:52`
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:58`
- [com.salesmanager.shop.admin.security.WebUserServices](/modules/com.salesmanager.shop.admin.security.md) `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:49`

## Calls
- `InitializationLoader.init` calls [com.salesmanager.core.business.services.reference.init.InitializationDatabase](/modules/com.salesmanager.core.business.services.reference.init.md) `InitializationDatabase.populate` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:82`
- `InitializationLoader.init` calls [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `MerchantConfigurationService.saveMerchantConfig` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:91`
- `InitializationLoader.init` calls [com.salesmanager.shop.admin.security.WebUserServices](/modules/com.salesmanager.shop.admin.security.md) `WebUserServices.createDefaultAdmin` `sm-shop/src/main/java/com/salesmanager/shop/init/data/InitializationLoader.java:86`
