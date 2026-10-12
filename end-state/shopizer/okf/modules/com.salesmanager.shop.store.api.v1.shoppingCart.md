---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.shoppingCart"
description: "com.salesmanager.shop.store.api.v1.shoppingCart: ShoppingCartApi; 9 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java"
    sha256: "ec61a920ad3dad84e2e622111937cfdab907eaf86dfffce8a84683c5d3da5af8"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.shoppingCart

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java`

## Types
- `ShoppingCartApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:51`

## Fields
- `ShoppingCartApi.shoppingCartFacade: ShoppingCartFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:59`
- `ShoppingCartApi.shoppingCartFacadev1: com.salesmanager.shop.store.controller.shoppingCart.facade.v1.ShoppingCartFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:62`
- `ShoppingCartApi.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:65`
- `ShoppingCartApi.customerFacadev1: CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:68`
- `ShoppingCartApi.customerFacade: com.salesmanager.shop.store.controller.customer.facade.CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:71`
- `ShoppingCartApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:73`

## Functions and methods
- `ShoppingCartApi.addToCart(PersistableShoppingCartItem, MerchantStore, Language) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:75`
- `ShoppingCartApi.modifyCart(String, PersistableShoppingCartItem, MerchantStore, Language, HttpServletResponse) -> ResponseEntity<ReadableShoppingCart>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:87`
- `ShoppingCartApi.modifyCart(String, String, MerchantStore, Language, HttpServletResponse) -> ResponseEntity<ReadableShoppingCart>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:118`
- `ShoppingCartApi.modifyCart(String, PersistableShoppingCartItem[], MerchantStore, Language) -> ResponseEntity<ReadableShoppingCart>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:149`
- `ShoppingCartApi.getByCode(String, MerchantStore, Language, HttpServletResponse) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:175`
- `ShoppingCartApi.addToCart(Long, PersistableShoppingCartItem, MerchantStore, Language, HttpServletResponse) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:204`
- `ShoppingCartApi.getByCustomer(Long, Optional<String>, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:218`
- `ShoppingCartApi.getByCustomer(Optional<String>, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:251`
- `ShoppingCartApi.deleteCartItem(String, String, MerchantStore, Language, boolean) -> ResponseEntity<ReadableShoppingCart>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:286`

## HTTP routes
- `GET /api/v1/auth/customer/cart` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#getByCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:251`
- `GET /api/v1/auth/customer/{id}/cart` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#getByCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:218`
- `POST /api/v1/cart` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#addToCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:75`
- `GET /api/v1/cart/{code}` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#getByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:175`
- `PUT /api/v1/cart/{code}` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#modifyCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:87`
- `POST /api/v1/cart/{code}/multi` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#modifyCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:149`
- `DELETE /api/v1/cart/{code}/product/{sku}` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#deleteCartItem` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:286`
- `POST /api/v1/cart/{code}/promo/{promo}` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#modifyCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:118`
- `POST /api/v1/customers/{id}/cart` handled by `com.salesmanager.shop.store.api.v1.shoppingCart.ShoppingCartApi#addToCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:204`

## Depends on
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:64`
- [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:67`
- [com.salesmanager.shop.store.controller.customer.facade.v1.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.v1.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:67`
- [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:58`
- [com.salesmanager.shop.store.controller.shoppingCart.facade.v1.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.v1.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:58`

## Calls
- `ShoppingCartApi.addToCart` calls [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `ShoppingCartFacade.addToCart` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:84`
- `ShoppingCartApi.deleteCartItem` calls [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `ShoppingCartFacade.removeShoppingCartItem` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:296`
- `ShoppingCartApi.getByCustomer` calls [com.salesmanager.shop.store.controller.customer.facade.v1.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.v1.md) `CustomerFacade.authorize` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:239`
- `ShoppingCartApi.getByCustomer` calls [com.salesmanager.shop.store.controller.shoppingCart.facade.v1.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.v1.md) `ShoppingCartFacade.get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:241`
- `ShoppingCartApi.modifyCart` calls [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `ShoppingCartFacade.modifyCart`, `ShoppingCartFacade.modifyCartMulti` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/shoppingCart/ShoppingCartApi.java:99`
