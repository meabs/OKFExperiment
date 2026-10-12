---
type: Code Module
title: "com.salesmanager.shop.store.controller.marketplace.facade"
description: "com.salesmanager.shop.store.controller.marketplace.facade: MarketPlaceFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacade.java"
    sha256: "75ddf561e95832f1f785da476556491292f8bec22e50da57cfcedb47347bd96b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java"
    sha256: "6ccd908bb191ccd361fa1b213a06ba7d230333e614f73599580dec1328264f4c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.marketplace.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java`

## Types
- `MarketPlaceFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacade.java:14`
- `MarketPlaceFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:24`

## Fields
- `MarketPlaceFacadeImpl.storeFacade: StoreFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:28`
- `MarketPlaceFacadeImpl.optinService: OptinService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:31`

## Functions and methods
- `MarketPlaceFacade.get(String, Language) -> ReadableMarketPlace` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacade.java:24`
- `MarketPlaceFacade.findByMerchantAndType(MerchantStore, OptinType) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacade.java:33`
- `MarketPlaceFacadeImpl.get(String, Language) -> ReadableMarketPlace` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:33`
- `MarketPlaceFacadeImpl.createReadableMarketPlace(ReadableMerchantStore) -> ReadableMarketPlace` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:39`
- `MarketPlaceFacadeImpl.findByMerchantAndType(MerchantStore, OptinType) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:46`
- `MarketPlaceFacadeImpl.getOptinByMerchantAndType(MerchantStore, OptinType) -> Optin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:52`
- `MarketPlaceFacadeImpl.convertOptinToReadableOptin(MerchantStore, Optin) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:62`

## Depends on
- [com.salesmanager.core.business.services.system.optin.OptinService](/modules/com.salesmanager.core.business.services.system.optin.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:30`
- [com.salesmanager.shop.store.controller.store.facade.StoreFacade](/modules/com.salesmanager.shop.store.controller.store.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:27`

## Calls
- `MarketPlaceFacadeImpl.convertOptinToReadableOptin` calls [com.salesmanager.shop.populator.system.ReadableOptinPopulator](/modules/com.salesmanager.shop.populator.system.md) `ReadableOptinPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/marketplace/facade/MarketPlaceFacadeImpl.java:65`
