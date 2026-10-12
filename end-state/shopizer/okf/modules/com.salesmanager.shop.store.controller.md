---
type: Code Module
title: "com.salesmanager.shop.store.controller"
description: "com.salesmanager.shop.store.controller: AbstractController"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java"
    sha256: "1b717fb529c9b853138e21e6e4e2ef0c70dd1ef11fade2fe6eb2bd6b1419a2a3"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java"
    sha256: "3d79af7d93bae0377dc046acf0a1f8e9175e59f2117a9d8675405f0cd793dc2f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java`

## Types
- `AbstractController` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:16`
- `ControllerConstants` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:13`
- `Tiles` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:18`
- `ShoppingCart` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:19`
- `Category` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:23`
- `Product` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:27`
- `Items` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:31`
- `Customer` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:35`
- `Content` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:47`
- `Pages` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:52`
- `Merchant` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:57`
- `Checkout` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:61`
- `Search` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:66`
- `Error` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:70`
- `Views` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:79`
- `Controllers` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:81`
- `Registration` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/ControllerConstants.java:83`

## Functions and methods
- `AbstractController.getSessionAttribute(String, HttpServletRequest) -> T` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:25`
- `AbstractController.setSessionAttribute(String, Object, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:31`
- `AbstractController.removeAttribute(String, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:36`
- `AbstractController.getLanguage(HttpServletRequest) -> Language` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:40`
- `AbstractController.createPaginaionData(int, int) -> PaginationData` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:44`
- `AbstractController.calculatePaginaionData(PaginationData, int, int) -> PaginationData` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/AbstractController.java:51`
