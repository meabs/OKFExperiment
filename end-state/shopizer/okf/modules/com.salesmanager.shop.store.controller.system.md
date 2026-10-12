---
type: Code Module
title: "com.salesmanager.shop.store.controller.system"
description: "com.salesmanager.shop.store.controller.system: MerchantConfigurationFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacade.java"
    sha256: "daba5547ef48550f294e337fd87929cef8ecf5bffef46d0debb859730f983a3d"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java"
    sha256: "0e18f0b444610e65395df6fa807350c79320a5b74af901210b9a0f3b71f869ba"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.system

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java`

## Types
- `MerchantConfigurationFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacade.java:7`
- `MerchantConfigurationFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:28`

## Fields
- `MerchantConfigurationFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:31`
- `MerchantConfigurationFacadeImpl.merchantConfigurationService: MerchantConfigurationService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:35`
- `MerchantConfigurationFacadeImpl.displayShipping: String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:38`

## Functions and methods
- `MerchantConfigurationFacade.getMerchantConfig(MerchantStore, Language) -> Configs` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacade.java:9`
- `MerchantConfigurationFacadeImpl.getMerchantConfig(MerchantStore, Language) -> Configs` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:40`
- `MerchantConfigurationFacadeImpl.getMerchantConfig(MerchantStore) -> MerchantConfig` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:80`
- `MerchantConfigurationFacadeImpl.getConfigValue(String, MerchantStore) -> Optional<String>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:88`
- `MerchantConfigurationFacadeImpl.getMerchantConfiguration(String, MerchantStore) -> Optional<MerchantConfiguration>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:93`

## Depends on
- [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/system/MerchantConfigurationFacadeImpl.java:34`
