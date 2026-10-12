---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.security"
description: "com.salesmanager.shop.store.api.v1.security: SecurityApi; 3 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java"
    sha256: "f0e57851759c217443c5965d07a1c7677a116a7ea2bab1eee2712393a9743cc2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.security

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java`

## Types
- `SecurityApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:39`

## Fields
- `SecurityApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:46`
- `SecurityApi.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:49`
- `SecurityApi.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:52`

## Functions and methods
- `SecurityApi.listPermissions(String) -> List<ReadablePermission>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:54`
- `SecurityApi.permissions() -> List<ReadablePermission>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:87`
- `SecurityApi.groups() -> List<ReadableGroup>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:105`

## HTTP routes
- `GET /api/v1/sec/private/groups` handled by `com.salesmanager.shop.store.api.v1.security.SecurityApi#groups` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:105`
- `GET /api/v1/sec/private/permissions` handled by `com.salesmanager.shop.store.api.v1.security.SecurityApi#permissions` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:87`
- `GET /api/v1/sec/private/{group}/permissions` handled by `com.salesmanager.shop.store.api.v1.security.SecurityApi#listPermissions` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:54`

## Depends on
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:51`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:48`

## Calls
- `SecurityApi.groups` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:107`
- `SecurityApi.listPermissions` calls [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `GroupService.findByName` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:61`
- `SecurityApi.permissions` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/security/SecurityApi.java:89`
