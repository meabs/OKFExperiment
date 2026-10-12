---
type: Code Module
title: "com.salesmanager.shop.store.facade.customer"
description: "com.salesmanager.shop.store.facade.customer: CustomerFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java"
    sha256: "65995975558fa2748ead02a605371e02364959d8d903cdabd6d8b1bcf2020813"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.customer

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java`

## Types
- `CustomerFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:40`

## Fields
- `CustomerFacadeImpl.customerFacade: com.salesmanager.shop.store.controller.customer.facade.CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:44`
- `CustomerFacadeImpl.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:47`
- `CustomerFacadeImpl.filePathUtils: FilePathUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:50`
- `CustomerFacadeImpl.lamguageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:53`
- `CustomerFacadeImpl.emailUtils: EmailUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:56`
- `CustomerFacadeImpl.emailService: EmailService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:59`
- `CustomerFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:63`
- `CustomerFacadeImpl.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:66`
- `CustomerFacadeImpl.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:69`
- `CustomerFacadeImpl.resetCustomerLink: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:71`
- `CustomerFacadeImpl.ACCOUNT_PASSWORD_RESET_TPL: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:74`
- `CustomerFacadeImpl.RESET_PASSWORD_LINK: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:76`
- `CustomerFacadeImpl.RESET_PASSWORD_TEXT: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:78`

## Functions and methods
- `CustomerFacadeImpl.authorize(Customer, Principal) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:80`
- `CustomerFacadeImpl.requestPasswordReset(String, String, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:93`
- `CustomerFacadeImpl.resetPasswordRequest(Customer, String, MerchantStore, Locale) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:163`
- `CustomerFacadeImpl.verifyPasswordRequestToken(String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:199`
- `CustomerFacadeImpl.resetPassword(String, String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:208`
- `CustomerFacadeImpl.verifyCustomerLink(String, String) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:224`
- `CustomerFacadeImpl.customerExists(String, MerchantStore) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:252`

## Depends on
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:46`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:52`
- [com.salesmanager.core.business.services.system.EmailService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:58`
- [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:43`
- [com.salesmanager.shop.utils.EmailUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:55`
- [com.salesmanager.shop.utils.FilePathUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:49`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:61`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:65`

## Calls
- `CustomerFacadeImpl.requestPasswordReset` calls [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `CustomerService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:116`
- `CustomerFacadeImpl.requestPasswordReset` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.toLocale` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:127`
- `CustomerFacadeImpl.requestPasswordReset` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.addDaysToCurrentDate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:109`
- `CustomerFacadeImpl.requestPasswordReset` calls [com.salesmanager.shop.utils.FilePathUtils](/modules/com.salesmanager.shop.utils.md) `FilePathUtils.buildBaseUrl` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:120`
- `CustomerFacadeImpl.resetPassword` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:217`
- `CustomerFacadeImpl.resetPasswordRequest` calls [com.salesmanager.core.business.services.system.EmailService](/modules/com.salesmanager.core.business.services.system.md) `EmailService.sendHtmlEmail` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:192`
- `CustomerFacadeImpl.resetPasswordRequest` calls [com.salesmanager.shop.utils.EmailUtils](/modules/com.salesmanager.shop.utils.md) `EmailUtils.createEmailObjectsMap` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:171`
- `CustomerFacadeImpl.verifyCustomerLink` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.dateBeforeEqualsDate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/customer/CustomerFacadeImpl.java:244`
