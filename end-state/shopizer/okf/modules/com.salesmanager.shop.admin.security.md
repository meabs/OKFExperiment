---
type: Code Module
title: "com.salesmanager.shop.admin.security"
description: "com.salesmanager.shop.admin.security: AbstractAuthenticatinSuccessHandler, SecurityDataAccessException, UserAuthenticationSuccessHandler, UserServicesImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java"
    sha256: "849a5ed10a8da24177104cc8596b4593b104d1fc2197ae9e3321300f3fe3da26"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/admin/security/SecurityDataAccessException.java"
    sha256: "05c9fe6c2e2da066717851fb07fbfcd4e2937084f219d3917a323d181d7d8786"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java"
    sha256: "d250fc8f0610a4376877116ef82bec2f5ba19646ab9f0205779a01aabdcc0768"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java"
    sha256: "a1898c3aa7a24a01d99fc47510cb42088221d5ebe2b2186da092b37f80642a6a"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/admin/security/WebUserServices.java"
    sha256: "f3bd9ff99786b19fa8285d7ac13d73eddc43bab5561f02721deecb8a26a27425"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.admin.security

Source: `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java`, `sm-shop/src/main/java/com/salesmanager/shop/admin/security/SecurityDataAccessException.java`, `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java`, `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java`, `sm-shop/src/main/java/com/salesmanager/shop/admin/security/WebUserServices.java`

## Types
- `AbstractAuthenticatinSuccessHandler` (class) extends `org.springframework.security.web.authentication.SavedRequestAwareAuthenticationSuccessHandler` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:20`
- `SecurityDataAccessException` (class) extends `org.springframework.dao.DataAccessException` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/SecurityDataAccessException.java:5`
- `UserAuthenticationSuccessHandler` (class) extends [com.salesmanager.shop.admin.security.AbstractAuthenticatinSuccessHandler](/modules/com.salesmanager.shop.admin.security.md) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java:11`
- `UserServicesImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:37`
- `WebUserServices` (interface) extends `org.springframework.security.core.userdetails.UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/WebUserServices.java:5`

## Fields
- `AbstractAuthenticatinSuccessHandler.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:24`
- `AbstractAuthenticatinSuccessHandler.userService: UserService` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:28`
- `UserAuthenticationSuccessHandler.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java:13`
- `UserAuthenticationSuccessHandler.redirectStrategy: RedirectStrategy` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java:15`
- `UserServicesImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:40`
- `UserServicesImpl.DEFAULT_INITIAL_PASSWORD: String` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:42`
- `UserServicesImpl.userService: UserService` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:45`
- `UserServicesImpl.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:49`
- `UserServicesImpl.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:53`
- `UserServicesImpl.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:58`
- `UserServicesImpl.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:61`
- `UserServicesImpl.ROLE_PREFIX: String` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:63`

## Functions and methods
- `AbstractAuthenticatinSuccessHandler.redirectAfterSuccess(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:22`
- `AbstractAuthenticatinSuccessHandler.onAuthenticationSuccess(HttpServletRequest, HttpServletResponse, Authentication) -> void` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:30`
- `UserAuthenticationSuccessHandler.setRedirectStrategy(RedirectStrategy) -> void` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java:18`
- `UserAuthenticationSuccessHandler.getRedirectStrategy() -> RedirectStrategy` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java:21`
- `UserAuthenticationSuccessHandler.redirectAfterSuccess(HttpServletRequest, HttpServletResponse) -> void` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserAuthenticationSuccessHandler.java:25`
- `UserServicesImpl.loadUserByUsername(String) -> UserDetails` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:67`
- `UserServicesImpl.createDefaultAdmin() -> void` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:116`
- `WebUserServices.createDefaultAdmin() -> void` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/WebUserServices.java:7`

## Depends on
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:48`
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:60`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:57`
- [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:27`
- [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:44`

## Calls
- `AbstractAuthenticatinSuccessHandler.onAuthenticationSuccess` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/AbstractAuthenticatinSuccessHandler.java:53`
- `UserServicesImpl.createDefaultAdmin` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:136`
- `UserServicesImpl.createDefaultAdmin` calls [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `GroupService.listGroup` `sm-shop/src/main/java/com/salesmanager/shop/admin/security/UserServicesImpl.java:122`
