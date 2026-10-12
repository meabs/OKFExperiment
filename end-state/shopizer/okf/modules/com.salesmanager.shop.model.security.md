---
type: Code Module
title: "com.salesmanager.shop.model.security"
description: "com.salesmanager.shop.model.security: GroupEntity, PermissionEntity, PersistableGroup, ReadableGroup"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java"
    sha256: "d2d63c1bf924cb7973f5373481508f18ef8b25e515ce1fac032a671e176be936"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java"
    sha256: "8be11a0f8e86d60e8274a4f5723782bc6fa6dc0d55eb853ac1086c8538be1724"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PersistableGroup.java"
    sha256: "6a556d8c311485b0229cd4d949633c630e61f7cc021fab771c00c79bdf031656"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadableGroup.java"
    sha256: "766a15054009ec8d7f1b6fc597b3a48d21e3f852e95dde93dfeabb4f82b93041"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadablePermission.java"
    sha256: "39e19d1241f291ab66f7fe768c9f7aa477ec600c33c499c9ac766e81b40ed0ee"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.security

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PersistableGroup.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadableGroup.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadablePermission.java`

## Types
- `GroupEntity` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:5`
- `PermissionEntity` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:5`
- `PersistableGroup` (class) extends [com.salesmanager.shop.model.security.GroupEntity](/modules/com.salesmanager.shop.model.security.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PersistableGroup.java:9`
- `ReadableGroup` (class) extends [com.salesmanager.shop.model.security.GroupEntity](/modules/com.salesmanager.shop.model.security.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadableGroup.java:9`
- `ReadablePermission` (class) extends [com.salesmanager.shop.model.security.PermissionEntity](/modules/com.salesmanager.shop.model.security.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadablePermission.java:3`

## Fields
- `GroupEntity.name: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:12`
- `GroupEntity.type: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:13`
- `PermissionEntity.id: Integer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:11`
- `PermissionEntity.name: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:12`
- `ReadableGroup.id: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadableGroup.java:16`

## Functions and methods
- `GroupEntity.getName() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:15`
- `GroupEntity.setName(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:19`
- `GroupEntity.getType() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:23`
- `GroupEntity.setType(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/GroupEntity.java:27`
- `PermissionEntity.getName() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:13`
- `PermissionEntity.setName(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:16`
- `PermissionEntity.getId() -> Integer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:19`
- `PermissionEntity.setId(Integer) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/PermissionEntity.java:22`
- `ReadableGroup.setId(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadableGroup.java:18`
- `ReadableGroup.getId() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/security/ReadableGroup.java:22`
