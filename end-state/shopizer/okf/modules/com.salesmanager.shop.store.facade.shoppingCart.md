---
type: Code Module
title: "com.salesmanager.shop.store.facade.shoppingCart"
description: "com.salesmanager.shop.store.facade.shoppingCart: ShoppingCartFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java"
    sha256: "e24f43a2abc7672768456eef79941ec700e119dce7446cc27efc7d829a0d6082"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.shoppingCart

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java`

## Types
- `ShoppingCartFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:20`

## Fields
- `ShoppingCartFacadeImpl.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:24`
- `ShoppingCartFacadeImpl.shoppingCartService: ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:27`
- `ShoppingCartFacadeImpl.customerFacade: com.salesmanager.shop.store.controller.customer.facade.CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:30`
- `ShoppingCartFacadeImpl.shoppingCartFacade: com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:33`

## Functions and methods
- `ShoppingCartFacadeImpl.get(Optional<String>, Long, MerchantStore, Language) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:36`

## Depends on
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:23`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:26`
- [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:29`
- [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:32`

## Calls
- `ShoppingCartFacadeImpl.get` calls [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `CustomerFacade.mergeCart` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:54`
- `ShoppingCartFacadeImpl.get` calls [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `ShoppingCartFacade.readableCart` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/shoppingCart/ShoppingCartFacadeImpl.java:61`
