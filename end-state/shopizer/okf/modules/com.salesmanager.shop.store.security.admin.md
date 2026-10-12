---
type: Code Module
title: "com.salesmanager.shop.store.security.admin"
description: "com.salesmanager.shop.store.security.admin: AdminAccessDeniedHandler, JWTAdminAuthenticationManager, JWTAdminAuthenticationProvider, JWTAdminServicesImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java"
    sha256: "2d8fbf71621ebb95402beb54199346cfa865bc9249f08645f7aa65579be63447"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java"
    sha256: "e82aab38fed2d6118c7b3dff4a6b3fe24a836de789bfe2b36324577c0fa50ce4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java"
    sha256: "65e9e9cf8833b6e492b50a11892e9e8ed625508dd280dd44678a0286ffa5af60"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java"
    sha256: "f91addf26537e200e74592fc80661d9b27fbd43617293491f0b5b7f15322222b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.security.admin

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java`

## Types
- `AdminAccessDeniedHandler` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java:12`
- `JWTAdminAuthenticationManager` (class) extends [com.salesmanager.shop.store.security.common.CustomAuthenticationManager](/modules/com.salesmanager.shop.store.security.common.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:23`
- `JWTAdminAuthenticationProvider` (class) extends `org.springframework.security.authentication.dao.DaoAuthenticationProvider` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:21`
- `JWTAdminServicesImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:33`

## Fields
- `AdminAccessDeniedHandler.accessDeniedUrl: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java:31`
- `JWTAdminAuthenticationManager.logger: Log` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:26`
- `JWTAdminAuthenticationManager.BEARER: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:27`
- `JWTAdminAuthenticationManager.jwtTokenUtil: JWTTokenUtil` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:30`
- `JWTAdminAuthenticationManager.jwtAdminDetailsService: UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:33`
- `JWTAdminAuthenticationProvider.jwtAdminDetailsService: UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:24`
- `JWTAdminAuthenticationProvider.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:27`
- `JWTAdminServicesImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:36`
- `JWTAdminServicesImpl.userService: UserService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:40`
- `JWTAdminServicesImpl.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:42`
- `JWTAdminServicesImpl.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:44`
- `JWTAdminServicesImpl.ROLE_PREFIX: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:46`

## Functions and methods
- `AdminAccessDeniedHandler.handle(HttpServletRequest, HttpServletResponse, AccessDeniedException) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java:14`
- `AdminAccessDeniedHandler.getAccessDeniedUrl() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java:23`
- `AdminAccessDeniedHandler.setAccessDeniedUrl(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/AdminAccessDeniedHandler.java:27`
- `JWTAdminAuthenticationManager.attemptAuthentication(HttpServletRequest, HttpServletResponse) -> Authentication` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:35`
- `JWTAdminAuthenticationManager.successfullAuthentication(HttpServletRequest, HttpServletResponse, Authentication) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:80`
- `JWTAdminAuthenticationManager.unSuccessfullAuthentication(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:87`
- `JWTAdminAuthenticationProvider.getJwtAdminDetailsService() -> UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:29`
- `JWTAdminAuthenticationProvider.setJwtAdminDetailsService(UserDetailsService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:32`
- `JWTAdminAuthenticationProvider.authenticate(Authentication) -> Authentication` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:35`
- `JWTAdminAuthenticationProvider.passwordMatch(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:62`
- `JWTAdminAuthenticationProvider.supports(Class<?>) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationProvider.java:66`
- `JWTAdminServicesImpl.userDetails(String, User, Collection<GrantedAuthority>) -> UserDetails` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:49`
- `JWTAdminServicesImpl.loadUserByUsername(String) -> UserDetails` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:71`

## Depends on
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:43`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:41`
- [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminServicesImpl.java:39`
- [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:29`

## Calls
- `JWTAdminAuthenticationManager.attemptAuthentication` calls [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `JWTTokenUtil.validateToken` `sm-shop/src/main/java/com/salesmanager/shop/store/security/admin/JWTAdminAuthenticationManager.java:68`
