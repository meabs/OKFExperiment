---
type: Code Module
title: "com.salesmanager.shop.store.facade.user"
description: "com.salesmanager.shop.store.facade.user: UserFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java"
    sha256: "18957a68ee8dafeee383769bfb4026fe05324ce772a1441b6172324c744ba0d4"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.user

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java`

## Types
- `UserFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:72`

## Fields
- `UserFacadeImpl.PRIVATE_PATH: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:75`
- `UserFacadeImpl.resetUserLink: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:77`
- `UserFacadeImpl.ACCOUNT_PASSWORD_RESET_TPL: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:79`
- `UserFacadeImpl.RESET_PASSWORD_LINK: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:81`
- `UserFacadeImpl.RESET_PASSWORD_TEXT: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:83`
- `UserFacadeImpl.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:86`
- `UserFacadeImpl.userService: UserService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:89`
- `UserFacadeImpl.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:92`
- `UserFacadeImpl.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:95`
- `UserFacadeImpl.persistableUserPopulator: PersistableUserPopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:98`
- `UserFacadeImpl.securityFacade: SecurityFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:101`
- `UserFacadeImpl.filePathUtils: FilePathUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:104`
- `UserFacadeImpl.lamguageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:107`
- `UserFacadeImpl.emailUtils: EmailUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:110`
- `UserFacadeImpl.emailService: EmailService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:113`
- `UserFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:117`
- `UserFacadeImpl.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:120`
- `UserFacadeImpl.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:123`
- `UserFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:125`

## Functions and methods
- `UserFacadeImpl.findByUserName(String, String, Language) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:127`
- `UserFacadeImpl.findByUserName(String, Language) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:138`
- `UserFacadeImpl.convertUserToReadableUser(Language, User) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:146`
- `UserFacadeImpl.converPersistabletUserToUser(MerchantStore, Language, User, PersistableUser) -> User` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:163`
- `UserFacadeImpl.getByUserName(String) -> User` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:172`
- `UserFacadeImpl.getByUserName(String, String) -> User` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:180`
- `UserFacadeImpl.getByUserId(Long, String) -> User` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:188`
- `UserFacadeImpl.getByUserId(Long) -> User` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:196`
- `UserFacadeImpl.findPermissionsByGroups(List<Integer>) -> List<ReadablePermission>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:204`
- `UserFacadeImpl.convertPermissionToReadablePermission(Permission) -> ReadablePermission` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:210`
- `UserFacadeImpl.getPermissionsByIds(List<Integer>) -> List<Permission>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:217`
- `UserFacadeImpl.authorizedStore(String, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:225`
- `UserFacadeImpl.authorizedGroup(String, List<String>) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:271`
- `UserFacadeImpl.authenticatedUser() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:287`
- `UserFacadeImpl.create(PersistableUser, MerchantStore) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:302`
- `UserFacadeImpl.getByCriteria(Language, String, Criteria) -> ReadableUserList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:350`
- `UserFacadeImpl.delete(Long, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:371`
- `UserFacadeImpl.update(Long, String, MerchantStore, PersistableUser) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:393`
- `UserFacadeImpl.changePassword(Long, String, UserPassword) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:477`
- `UserFacadeImpl.listByCriteria(UserCriteria, int, int, Language) -> ReadableUserList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:527`
- `UserFacadeImpl.authorizedGroups(String, PersistableUser) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:579`
- `UserFacadeImpl.userInRoles(String, List<String>) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:611`
- `UserFacadeImpl.updateEnabled(MerchantStore, PersistableUser) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:623`
- `UserFacadeImpl.authorizeStore(MerchantStore, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:646`
- `UserFacadeImpl.findById(Long, MerchantStore, Language) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:720`
- `UserFacadeImpl.findByUserName(String) -> ReadableUser` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:733`
- `UserFacadeImpl.sendResetPasswordEmail(ReadableUser, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:751`
- `UserFacadeImpl.requestPasswordReset(String, String, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:793`
- `UserFacadeImpl.verifyPasswordRequestToken(String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:841`
- `UserFacadeImpl.resetPassword(String, String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:850`
- `UserFacadeImpl.verifyUserLink(String, String) -> User` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:867`
- `UserFacadeImpl.resetPasswordRequest(User, String, MerchantStore, Locale) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:896`

## Depends on
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:85`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:94`
- [com.salesmanager.core.business.services.system.EmailService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:112`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:91`
- [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:88`
- [com.salesmanager.shop.populator.user.PersistableUserPopulator](/modules/com.salesmanager.shop.populator.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:97`
- [com.salesmanager.shop.store.controller.security.facade.SecurityFacade](/modules/com.salesmanager.shop.store.controller.security.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:100`
- [com.salesmanager.shop.utils.EmailUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:109`
- [com.salesmanager.shop.utils.FilePathUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:103`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:115`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:119`

## Calls
- `UserFacadeImpl.authorizeStore` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:668`
- `UserFacadeImpl.authorizedGroup` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:274`
- `UserFacadeImpl.authorizedStore` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:235`
- `UserFacadeImpl.authorizedStore` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.findByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:245`
- `UserFacadeImpl.changePassword` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:518`
- `UserFacadeImpl.changePassword` calls [com.salesmanager.shop.store.controller.security.facade.SecurityFacade](/modules/com.salesmanager.shop.store.controller.security.facade.md) `SecurityFacade.encodePassword`, `SecurityFacade.matchPassword`, `SecurityFacade.validateUserPassword` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:515`
- `UserFacadeImpl.converPersistabletUserToUser` calls [com.salesmanager.shop.populator.user.PersistableUserPopulator](/modules/com.salesmanager.shop.populator.user.md) `PersistableUserPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:166`
- `UserFacadeImpl.convertUserToReadableUser` calls [com.salesmanager.shop.populator.user.ReadableUserPopulator](/modules/com.salesmanager.shop.populator.user.md) `ReadableUserPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:150`
- `UserFacadeImpl.create` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:335`
- `UserFacadeImpl.create` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:340`
- `UserFacadeImpl.create` calls [com.salesmanager.shop.store.controller.security.facade.SecurityFacade](/modules/com.salesmanager.shop.store.controller.security.facade.md) `SecurityFacade.encodePassword`, `SecurityFacade.matchRawPasswords`, `SecurityFacade.validateUserPassword` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:332`
- `UserFacadeImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:386`
- `UserFacadeImpl.delete` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.findByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:376`
- `UserFacadeImpl.getByCriteria` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.listByCriteria` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:354`
- `UserFacadeImpl.getByUserId` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.findByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:190`
- `UserFacadeImpl.listByCriteria` calls [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `MerchantStoreService.findAllStoreNames` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:542`
- `UserFacadeImpl.listByCriteria` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.listByCriteria` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:551`
- `UserFacadeImpl.requestPasswordReset` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.toLocale` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:833`
- `UserFacadeImpl.requestPasswordReset` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:818`
- `UserFacadeImpl.requestPasswordReset` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.addDaysToCurrentDate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:811`
- `UserFacadeImpl.resetPassword` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:860`
- `UserFacadeImpl.resetPasswordRequest` calls [com.salesmanager.core.business.services.system.EmailService](/modules/com.salesmanager.core.business.services.system.md) `EmailService.sendHtmlEmail` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:922`
- `UserFacadeImpl.resetPasswordRequest` calls [com.salesmanager.shop.utils.EmailUtils](/modules/com.salesmanager.shop.utils.md) `EmailUtils.createEmailObjectsMap` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:902`
- `UserFacadeImpl.update` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:469`
- `UserFacadeImpl.update` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.defaultLanguage` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:450`
- `UserFacadeImpl.updateEnabled` calls [com.salesmanager.core.business.services.user.UserService](/modules/com.salesmanager.core.business.services.user.md) `UserService.findByStore`, `UserService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:630`
- `UserFacadeImpl.verifyUserLink` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.dateBeforeEqualsDate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/user/UserFacadeImpl.java:887`
