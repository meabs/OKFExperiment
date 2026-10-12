---
type: Code Module
title: "com.salesmanager.shop.store.controller.zone.facade"
description: "com.salesmanager.shop.store.controller.zone.facade: ZoneFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacade.java"
    sha256: "300889c0cdbfbe5b169777f722e03ae0bf2b41063332bc87d64b7c1264b96974"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java"
    sha256: "8c24ddfb84c308bb5f4a764a82ea25d9fdd3765b619a4a6bfa66d1b00a0a9474"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.zone.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java`

## Types
- `ZoneFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacade.java:9`
- `ZoneFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:22`

## Fields
- `ZoneFacadeImpl.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:26`

## Functions and methods
- `ZoneFacade.getZones(String, Language, MerchantStore) -> List<ReadableZone>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacade.java:11`
- `ZoneFacadeImpl.getZones(String, Language, MerchantStore) -> List<ReadableZone>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:28`
- `ZoneFacadeImpl.convertToReadableZone(Zone, Language, MerchantStore) -> ReadableZone` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:40`
- `ZoneFacadeImpl.getListZones(String, Language) -> List<Zone>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:49`

## Depends on
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:25`

## Calls
- `ZoneFacadeImpl.convertToReadableZone` calls [com.salesmanager.shop.populator.references.ReadableZonePopulator](/modules/com.salesmanager.shop.populator.references.md) `ReadableZonePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/zone/facade/ZoneFacadeImpl.java:43`
