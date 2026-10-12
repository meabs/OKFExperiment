---
type: Code Module
title: "com.salesmanager.shop.store.controller.currency.facade"
description: "com.salesmanager.shop.store.controller.currency.facade: CurrencyFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacade.java"
    sha256: "b3e870ed9eaf3dcd7780410792413399ca8558a5cb4681cb63288836e00aed02"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java"
    sha256: "75f290213229582ce044c343c8b6ea42e5f06b6a46399b37ba056a534393bd92"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.currency.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java`

## Types
- `CurrencyFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacade.java:6`
- `CurrencyFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java:14`

## Fields
- `CurrencyFacadeImpl.currencyService: CurrencyService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java:18`

## Functions and methods
- `CurrencyFacade.getList() -> List<Currency>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacade.java:8`
- `CurrencyFacadeImpl.getList() -> List<Currency>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java:20`

## Depends on
- [com.salesmanager.core.business.services.reference.currency.CurrencyService](/modules/com.salesmanager.core.business.services.reference.currency.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java:17`

## Calls
- `CurrencyFacadeImpl.getList` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.list` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/currency/facade/CurrencyFacadeImpl.java:22`
