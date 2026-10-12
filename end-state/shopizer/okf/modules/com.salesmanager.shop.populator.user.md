---
type: Code Module
title: "com.salesmanager.shop.populator.user"
description: "com.salesmanager.shop.populator.user: PersistableUserPopulator, ReadableUserPopulator"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java"
    sha256: "96998ddea7d0285bafed52246975f264d8643a07b37805c82581153e5c9e9abc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/user/ReadableUserPopulator.java"
    sha256: "7d3bd6390424f3752634a1c1e06088452e38e86a9d8df49d1158fe0f1f4045c5"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.populator.user

Source: `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/user/ReadableUserPopulator.java`

## Types
- `PersistableUserPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:28`
- `ReadableUserPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/user/ReadableUserPopulator.java:22`

## Fields
- `PersistableUserPopulator.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:32`
- `PersistableUserPopulator.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:35`
- `PersistableUserPopulator.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:38`
- `PersistableUserPopulator.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:42`

## Functions and methods
- `PersistableUserPopulator.populate(PersistableUser, User, MerchantStore, Language) -> User` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:44`
- `PersistableUserPopulator.createTarget() -> User` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:105`
- `ReadableUserPopulator.populate(User, ReadableUser, MerchantStore, Language) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/ReadableUserPopulator.java:24`
- `ReadableUserPopulator.createTarget() -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/ReadableUserPopulator.java:69`

## Depends on
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:37`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:31`
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:34`

## Calls
- `PersistableUserPopulator.populate` calls [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `GroupService.listGroupByNames` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/PersistableUserPopulator.java:92`
- `ReadableUserPopulator.populate` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.formatLongDate` `sm-shop/src/main/java/com/salesmanager/shop/populator/user/ReadableUserPopulator.java:40`
