---
type: Code Module
title: "com.salesmanager.shop.store.security.customer"
description: "com.salesmanager.shop.store.security.customer: JWTCustomerAuthenticationManager, JWTCustomerAuthenticationProvider, JWTCustomerServicesImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java"
    sha256: "19b0653828590fd80239f5ce8828cdeb9c72d17d13004320b3eb60c6c8887f3d"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java"
    sha256: "3737adcb22864112f25b5aef6cf86f016842ffb27325de7428cdbdd0098567de"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java"
    sha256: "4bead2e5e72ab8968f47a44a6b732c8b338d649742aee072b7614404dbe1dfd2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.security.customer

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java`

## Types
- `JWTCustomerAuthenticationManager` (class) extends [com.salesmanager.shop.store.security.common.CustomAuthenticationManager](/modules/com.salesmanager.shop.store.security.common.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:24`
- `JWTCustomerAuthenticationProvider` (class) extends `org.springframework.security.authentication.dao.DaoAuthenticationProvider` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:19`
- `JWTCustomerServicesImpl` (class) extends [com.salesmanager.shop.store.security.AbstractCustomerServices](/modules/com.salesmanager.shop.store.security.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java:21`

## Fields
- `JWTCustomerAuthenticationManager.logger: Log` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:27`
- `JWTCustomerAuthenticationManager.jwtTokenUtil: JWTTokenUtil` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:30`
- `JWTCustomerAuthenticationManager.jwtCustomerDetailsService: UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:33`
- `JWTCustomerAuthenticationProvider.jwtCustomerDetailsService: UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:22`
- `JWTCustomerAuthenticationProvider.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:25`

## Functions and methods
- `JWTCustomerAuthenticationManager.attemptAuthentication(HttpServletRequest, HttpServletResponse) -> Authentication` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:35`
- `JWTCustomerAuthenticationManager.successfullAuthentication(HttpServletRequest, HttpServletResponse, Authentication) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:78`
- `JWTCustomerAuthenticationManager.unSuccessfullAuthentication(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:85`
- `JWTCustomerAuthenticationProvider.authenticate(Authentication) -> Authentication` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:28`
- `JWTCustomerAuthenticationProvider.passwordMatch(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:55`
- `JWTCustomerAuthenticationProvider.supports(Class<?>) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:59`
- `JWTCustomerAuthenticationProvider.getJwtCustomerDetailsService() -> UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:65`
- `JWTCustomerAuthenticationProvider.setJwtCustomerDetailsService(UserDetailsService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationProvider.java:70`
- `JWTCustomerServicesImpl.userDetails(String, Customer, Collection<GrantedAuthority>) -> UserDetails` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java:33`

## Depends on
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java:25`
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java:25`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerServicesImpl.java:25`
- [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:29`

## Calls
- `JWTCustomerAuthenticationManager.attemptAuthentication` calls [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `JWTTokenUtil.validateToken` `sm-shop/src/main/java/com/salesmanager/shop/store/security/customer/JWTCustomerAuthenticationManager.java:67`
