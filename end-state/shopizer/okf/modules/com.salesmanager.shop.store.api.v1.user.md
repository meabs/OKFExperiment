---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.user"
description: "com.salesmanager.shop.store.api.v1.user: AuthenticateUserApi, ResetUserPasswordApi, UserApi; 14 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java"
    sha256: "c4d06aa66b70264dfc789da3f8e15898f06bfee6c4824d6d78cc17de609900b1"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java"
    sha256: "b3842ed6e1d01cb519dc8a444ec36dd3997d142923aa5e841b20256a76a681fd"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java"
    sha256: "1687c1fbc8f0f1edfffbdb99b489853b3599ef753eeb695921707461b8de2403"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.user

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java`

## Types
- `AuthenticateUserApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:38`
- `ResetUserPasswordApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:36`
- `UserApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:57`

## Fields
- `AuthenticateUserApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:45`
- `AuthenticateUserApi.tokenHeader: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:48`
- `AuthenticateUserApi.jwtAdminAuthenticationManager: AuthenticationManager` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:51`
- `AuthenticateUserApi.jwtAdminDetailsService: UserDetailsService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:54`
- `AuthenticateUserApi.jwtTokenUtil: JWTTokenUtil` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:57`
- `ResetUserPasswordApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:43`
- `ResetUserPasswordApi.userFacade: UserFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:48`
- `UserApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:63`
- `UserApi.userFacade: UserFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:67`

## Functions and methods
- `AuthenticateUserApi.authenticate(AuthenticationRequest) -> ResponseEntity<?>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:66`
- `AuthenticateUserApi.refreshAndGetAuthenticationToken(HttpServletRequest) -> ResponseEntity<AuthenticationResponse>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:107`
- `ResetUserPasswordApi.passwordResetRequest(MerchantStore, Language, ResetPasswordRequest, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:57`
- `ResetUserPasswordApi.passwordResetVerify(String, String, MerchantStore, Language, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:80`
- `ResetUserPasswordApi.changePassword(PasswordRequest, String, String, MerchantStore, Language, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:109`
- `UserApi.get(MerchantStore, Language, Long, HttpServletRequest) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:77`
- `UserApi.create(MerchantStore, Language, PersistableUser, HttpServletRequest) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:106`
- `UserApi.update(PersistableUser, Long, MerchantStore, Language) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:134`
- `UserApi.password(UserPassword, Long) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:154`
- `UserApi.list(MerchantStore, Language, Integer, Integer, String) -> ReadableUserList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:166`
- `UserApi.updateEnabled(Long, PersistableUser, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:202`
- `UserApi.delete(MerchantStore, Language, Long, HttpServletRequest) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:222`
- `UserApi.exists(MerchantStore, Language, UniqueEntity) -> ResponseEntity<EntityExists>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:245`
- `UserApi.getAuthUser(Language, HttpServletRequest) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:270`

## HTTP routes
- `GET /api/v1/auth/refresh` handled by `com.salesmanager.shop.store.api.v1.user.AuthenticateUserApi#refreshAndGetAuthenticationToken` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:107`
- `POST /api/v1/private/login` handled by `com.salesmanager.shop.store.api.v1.user.AuthenticateUserApi#authenticate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:66`
- `POST /api/v1/private/user` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:106`
- `GET /api/v1/private/user/profile` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#getAuthUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:270`
- `POST /api/v1/private/user/unique` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:245`
- `DELETE /api/v1/private/user/{id}` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#delete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:222`
- `PUT /api/v1/private/user/{id}` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:134`
- `PATCH /api/v1/private/user/{id}/enabled` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#updateEnabled` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:202`
- `PATCH /api/v1/private/user/{id}/password` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#password` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:154`
- `GET /api/v1/private/users` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:166`
- `GET /api/v1/private/users/{id}` handled by `com.salesmanager.shop.store.api.v1.user.UserApi#get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:77`
- `POST /api/v1/user/password/reset/request` handled by `com.salesmanager.shop.store.api.v1.user.ResetUserPasswordApi#passwordResetRequest` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:57`
- `POST /api/v1/user/{store}/password/{token}` handled by `com.salesmanager.shop.store.api.v1.user.ResetUserPasswordApi#changePassword` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:109`
- `GET /api/v1/user/{store}/reset/{token}` handled by `com.salesmanager.shop.store.api.v1.user.ResetUserPasswordApi#passwordResetVerify` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:80`

## Depends on
- [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:47`
- [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:66`
- [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:56`

## Calls
- `AuthenticateUserApi.authenticate` calls [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `JWTTokenUtil.generateToken` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:100`
- `AuthenticateUserApi.refreshAndGetAuthenticationToken` calls [com.salesmanager.shop.store.security.JWTTokenUtil](/modules/com.salesmanager.shop.store.security.md) `JWTTokenUtil.canTokenBeRefreshedWithGrace`, `JWTTokenUtil.refreshToken` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/AuthenticateUserApi.java:118`
- `ResetUserPasswordApi.changePassword` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.resetPassword` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:128`
- `ResetUserPasswordApi.passwordResetRequest` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.requestPasswordReset` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:68`
- `ResetUserPasswordApi.passwordResetVerify` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.verifyPasswordRequestToken` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/ResetUserPasswordApi.java:96`
- `UserApi.create` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.authorizedStore`, `UserFacade.create`, `UserFacade.userInRoles` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:116`
- `UserApi.delete` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.authorizedStore`, `UserFacade.delete`, `UserFacade.userInRoles` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:231`
- `UserApi.exists` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.findByUserName` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:254`
- `UserApi.get` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.findById` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:89`
- `UserApi.getAuthUser` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.findByUserName` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:275`
- `UserApi.list` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.authorizedStore`, `UserFacade.listByCriteria`, `UserFacade.userInRoles` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:179`
- `UserApi.password` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.changePassword` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:159`
- `UserApi.update` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroups`, `UserFacade.update` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:144`
- `UserApi.updateEnabled` calls [com.salesmanager.shop.store.controller.user.facade.UserFacade](/modules/com.salesmanager.shop.store.controller.user.facade.md) `UserFacade.authenticatedUser`, `UserFacade.authorizedGroup`, `UserFacade.updateEnabled` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/user/UserApi.java:211`

## Tests
- `com.salesmanager.test.shop.integration.user.UserApiIntegrationTest`
