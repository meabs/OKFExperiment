---
type: Code Module
title: "com.salesmanager.shop.store.controller.security.facade"
description: "com.salesmanager.shop.store.controller.security.facade: SecurityFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java"
    sha256: "abd163a580800229d629c707415a5599c6b4d91cb9018af0a5b6d546056e9adb"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java"
    sha256: "237f810844fa4e1fd14aecf169c1a275eb6678c6ee6a83f0e43b5e5d0a851a15"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.security.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java`

## Types
- `SecurityFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java:6`
- `SecurityFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:22`

## Fields
- `SecurityFacadeImpl.USER_PASSWORD_PATTERN: String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:25`
- `SecurityFacadeImpl.userPasswordPattern: Pattern` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:27`
- `SecurityFacadeImpl.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:30`
- `SecurityFacadeImpl.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:33`
- `SecurityFacadeImpl.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:36`

## Functions and methods
- `SecurityFacade.getPermissions(List<String>) -> List<ReadablePermission>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java:13`
- `SecurityFacade.validateUserPassword(String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java:20`
- `SecurityFacade.encodePassword(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java:27`
- `SecurityFacade.matchPassword(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java:35`
- `SecurityFacade.matchRawPasswords(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacade.java:43`
- `SecurityFacadeImpl.getPermissions(List<String>) -> List<ReadablePermission>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:38`
- `SecurityFacadeImpl.validateUserPassword(String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:63`
- `SecurityFacadeImpl.encodePassword(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:70`
- `SecurityFacadeImpl.matchPassword(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:79`
- `SecurityFacadeImpl.matchRawPasswords(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:84`

## Depends on
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:32`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:29`

## Calls
- `SecurityFacadeImpl.getPermissions` calls [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `GroupService.listGroupByNames` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:44`
- `SecurityFacadeImpl.getPermissions` calls [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `PermissionService.listByCriteria` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/security/facade/SecurityFacadeImpl.java:54`
