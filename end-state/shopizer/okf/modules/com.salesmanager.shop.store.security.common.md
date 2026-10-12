---
type: Code Module
title: "com.salesmanager.shop.store.security.common"
description: "com.salesmanager.shop.store.security.common: CustomAuthenticationException, CustomAuthenticationManager"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationException.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationException.java"
    sha256: "e39353f56756aaf607070d2677e66873942a363a15be93c06d0459a5c908cfdb"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java"
    sha256: "8207a92a556bea9d1c2249c2eeccde2c8d3ef5cc2c88fe828697725dc66dbf35"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.security.common

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationException.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java`

## Types
- `CustomAuthenticationException` (class) extends `org.springframework.security.core.AuthenticationException` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationException.java:5`
- `CustomAuthenticationManager` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:19`

## Fields
- `CustomAuthenticationManager.logger: Log` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:21`
- `CustomAuthenticationManager.tokenHeader: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:24`

## Functions and methods
- `CustomAuthenticationManager.getTokenHeader() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:27`
- `CustomAuthenticationManager.setTokenHeader(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:31`
- `CustomAuthenticationManager.authenticateRequest(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:35`
- `CustomAuthenticationManager.success(HttpServletRequest, HttpServletResponse, Authentication) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:62`
- `CustomAuthenticationManager.unsuccess(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:74`
- `CustomAuthenticationManager.attemptAuthentication(HttpServletRequest, HttpServletResponse) -> Authentication` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:87`
- `CustomAuthenticationManager.successfullAuthentication(HttpServletRequest, HttpServletResponse, Authentication) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:89`
- `CustomAuthenticationManager.unSuccessfullAuthentication(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/common/CustomAuthenticationManager.java:91`
