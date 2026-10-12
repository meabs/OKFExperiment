---
type: Code Module
title: "com.salesmanager.shop.store.controller.user.facade"
description: "com.salesmanager.shop.store.controller.user.facade: findByUserName, findByUserName, findById, create"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java"
    sha256: "3557703b6064174a68419cc6c8bd37762c94fdd5bd1482bd66a8579851ab8118"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.user.facade

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java`

## Types
- `UserFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:21`

## Functions and methods
- `UserFacade.findByUserName(String, String, Language) -> ReadableUser` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:29`
- `UserFacade.findByUserName(String) -> ReadableUser` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:36`
- `UserFacade.findById(Long, MerchantStore, Language) -> ReadableUser` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:45`
- `UserFacade.create(PersistableUser, MerchantStore) -> ReadableUser` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:52`
- `UserFacade.findPermissionsByGroups(List<Integer>) -> List<ReadablePermission>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:61`
- `UserFacade.authorizedStore(String, String) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:71`
- `UserFacade.authorizeStore(MerchantStore, String) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:79`
- `UserFacade.authorizedGroup(String, List<String>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:86`
- `UserFacade.userInRoles(String, List<String>) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:94`
- `UserFacade.sendResetPasswordEmail(ReadableUser, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:103`
- `UserFacade.authenticatedUser() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:109`
- `UserFacade.getByCriteria(Language, String, Criteria) -> ReadableUserList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:116`
- `UserFacade.listByCriteria(UserCriteria, int, int, Language) -> ReadableUserList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:127`
- `UserFacade.delete(Long, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:133`
- `UserFacade.update(Long, String, MerchantStore, PersistableUser) -> ReadableUser` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:139`
- `UserFacade.changePassword(Long, String, UserPassword) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:147`
- `UserFacade.authorizedGroups(String, PersistableUser) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:149`
- `UserFacade.updateEnabled(MerchantStore, PersistableUser) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:156`
- `UserFacade.requestPasswordReset(String, String, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:165`
- `UserFacade.verifyPasswordRequestToken(String, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:172`
- `UserFacade.resetPassword(String, String, String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/user/facade/UserFacade.java:181`
