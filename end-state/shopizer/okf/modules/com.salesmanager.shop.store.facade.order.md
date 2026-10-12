---
type: Code Module
title: "com.salesmanager.shop.store.facade.order"
description: "com.salesmanager.shop.store.facade.order: OrderFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java"
    sha256: "be4afa90fc2ccb22a9dc41c7da49c352e54b1f4131890d78459834a5234631c5"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.order

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java`

## Types
- `OrderFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:34`

## Fields
- `OrderFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:37`
- `OrderFacadeImpl.readableCustomerMapper: ReadableCustomerMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:41`
- `OrderFacadeImpl.readableOrderTotalMapper: ReadableOrderTotalMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:44`
- `OrderFacadeImpl.readableOrderProductMapper: ReadableOrderProductMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:47`
- `OrderFacadeImpl.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:50`
- `OrderFacadeImpl.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:53`

## Functions and methods
- `OrderFacadeImpl.orderConfirmation(Order, Customer, MerchantStore, Language) -> ReadableOrderConfirmation` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:55`
- `OrderFacadeImpl.convertOrderTotal(OrderTotal, MerchantStore, Language) -> ReadableOrderTotal` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:119`
- `OrderFacadeImpl.convertOrderProduct(OrderProduct, MerchantStore, Language) -> ReadableOrderProduct` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:124`

## Depends on
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:52`
- [com.salesmanager.shop.mapper.customer.ReadableCustomerMapper](/modules/com.salesmanager.shop.mapper.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:40`
- [com.salesmanager.shop.mapper.order.ReadableOrderProductMapper](/modules/com.salesmanager.shop.mapper.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:46`
- [com.salesmanager.shop.mapper.order.ReadableOrderTotalMapper](/modules/com.salesmanager.shop.mapper.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:43`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:49`

## Calls
- `OrderFacadeImpl.convertOrderProduct` calls [com.salesmanager.shop.mapper.order.ReadableOrderProductMapper](/modules/com.salesmanager.shop.mapper.order.md) `ReadableOrderProductMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:126`
- `OrderFacadeImpl.convertOrderTotal` calls [com.salesmanager.shop.mapper.order.ReadableOrderTotalMapper](/modules/com.salesmanager.shop.mapper.order.md) `ReadableOrderTotalMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:121`
- `OrderFacadeImpl.orderConfirmation` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.toLocale` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:98`
- `OrderFacadeImpl.orderConfirmation` calls [com.salesmanager.shop.mapper.customer.ReadableCustomerMapper](/modules/com.salesmanager.shop.mapper.customer.md) `ReadableCustomerMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/order/OrderFacadeImpl.java:64`
