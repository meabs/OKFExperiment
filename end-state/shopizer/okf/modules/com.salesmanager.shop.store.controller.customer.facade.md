---
type: Code Module
title: "com.salesmanager.shop.store.controller.customer.facade"
description: "com.salesmanager.shop.store.controller.customer.facade: CustomerFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java"
    sha256: "b9345fcb31e43d1bf701f540f9659a750792fee8dd7c6d7835f607bb181f589c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java"
    sha256: "073a86995329431711d509aa28eb2297a4864e3c78165e468393a7ce27d54831"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.customer.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java`

## Types
- `CustomerFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:33`
- `CustomerFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:102`

## Fields
- `CustomerFacadeImpl.LOG: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:105`
- `CustomerFacadeImpl.USERNAME_LENGTH: int` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:106`
- `CustomerFacadeImpl.RESET_PASSWORD_TPL: String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:108`
- `CustomerFacadeImpl.ROLE_PREFIX: String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:110`
- `CustomerFacadeImpl.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:114`
- `CustomerFacadeImpl.optinService: OptinService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:117`
- `CustomerFacadeImpl.customerOptinService: CustomerOptinService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:120`
- `CustomerFacadeImpl.shoppingCartService: ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:123`
- `CustomerFacadeImpl.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:126`
- `CustomerFacadeImpl.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:129`
- `CustomerFacadeImpl.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:132`
- `CustomerFacadeImpl.groupService: GroupService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:135`
- `CustomerFacadeImpl.permissionService: PermissionService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:138`
- `CustomerFacadeImpl.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:141`
- `CustomerFacadeImpl.passwordEncoder: PasswordEncoder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:144`
- `CustomerFacadeImpl.emailService: EmailService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:147`
- `CustomerFacadeImpl.emailTemplatesUtils: EmailTemplatesUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:150`
- `CustomerFacadeImpl.customerAuthenticationManager: AuthenticationManager` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:153`
- `CustomerFacadeImpl.customerReviewService: CustomerReviewService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:156`
- `CustomerFacadeImpl.coreConfiguration: CoreConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:159`
- `CustomerFacadeImpl.customerPopulator: CustomerPopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:162`
- `CustomerFacadeImpl.emailUtils: EmailUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:165`
- `CustomerFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:169`

## Functions and methods
- `CustomerFacade.getCustomerDataByUserName(String, MerchantStore, Language) -> CustomerEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:47`
- `CustomerFacade.getCustomerById(Long, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:56`
- `CustomerFacade.getByUserName(String, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:66`
- `CustomerFacade.mergeCart(Customer, String, MerchantStore, Language) -> ShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:78`
- `CustomerFacade.getCustomerByUserName(String, MerchantStore) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:80`
- `CustomerFacade.checkIfUserExists(String, MerchantStore) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:82`
- `CustomerFacade.registerCustomer(PersistableCustomer, MerchantStore, Language) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:84`
- `CustomerFacade.getAddress(Long, MerchantStore, boolean) -> Address` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:86`
- `CustomerFacade.updateAddress(Long, MerchantStore, Address, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:88`
- `CustomerFacade.setCustomerModelDefaultProperties(Customer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:91`
- `CustomerFacade.authenticate(Customer, String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:94`
- `CustomerFacade.getCustomerModel(PersistableCustomer, MerchantStore, Language) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:96`
- `CustomerFacade.populateCustomerModel(Customer, PersistableCustomer, MerchantStore, Language) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:99`
- `CustomerFacade.create(PersistableCustomer, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:105`
- `CustomerFacade.resetPassword(Customer, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:114`
- `CustomerFacade.update(PersistableCustomer, MerchantStore) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:122`
- `CustomerFacade.update(String, PersistableCustomer, MerchantStore) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:124`
- `CustomerFacade.updateAddress(PersistableCustomer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:132`
- `CustomerFacade.updateAddress(String, PersistableCustomer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:134`
- `CustomerFacade.saveOrUpdateCustomerReview(PersistableCustomerReview, MerchantStore, Language) -> PersistableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:143`
- `CustomerFacade.getAllCustomerReviewsByReviewed(Long, MerchantStore, Language) -> List<ReadableCustomerReview>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:152`
- `CustomerFacade.deleteCustomerReview(Long, Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:160`
- `CustomerFacade.optinCustomer(PersistableCustomerOptin, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:168`
- `CustomerFacade.getCustomerByNick(String, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:170`
- `CustomerFacade.deleteByNick(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:172`
- `CustomerFacade.deleteById(Long) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:174`
- `CustomerFacade.delete(Customer) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:176`
- `CustomerFacade.getListByStore(MerchantStore, CustomerCriteria, Language) -> ReadableCustomerList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:178`
- `CustomerFacade.createCustomerReview(Long, PersistableCustomerReview, MerchantStore, Language) -> PersistableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:180`
- `CustomerFacade.updateCustomerReview(Long, Long, PersistableCustomerReview, MerchantStore, Language) -> PersistableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:186`
- `CustomerFacade.passwordMatch(String, Customer) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:188`
- `CustomerFacade.changePassword(Customer, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacade.java:190`
- `CustomerFacadeImpl.getCustomerDataByUserName(String, MerchantStore, Language) -> CustomerEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:179`
- `CustomerFacadeImpl.mergeCart(Customer, String, MerchantStore, Language) -> ShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:209`
- `CustomerFacadeImpl.getCustomerByUserName(String, MerchantStore) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:285`
- `CustomerFacadeImpl.getByUserName(String, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:297`
- `CustomerFacadeImpl.getCustomerByNickAndStoreId(String, MerchantStore) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:306`
- `CustomerFacadeImpl.checkIfUserExists(String, MerchantStore) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:325`
- `CustomerFacadeImpl.registerCustomer(PersistableCustomer, MerchantStore, Language) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:345`
- `CustomerFacadeImpl.getCustomerModel(PersistableCustomer, MerchantStore, Language) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:370`
- `CustomerFacadeImpl.setCustomerModelDefaultProperties(Customer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:397`
- `CustomerFacadeImpl.authenticate(Customer, String, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:427`
- `CustomerFacadeImpl.getAddress(Long, MerchantStore, boolean) -> Address` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:463`
- `CustomerFacadeImpl.updateAddress(Long, MerchantStore, Address, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:495`
- `CustomerFacadeImpl.getCustomerById(Long, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:556`
- `CustomerFacadeImpl.populateCustomerModel(Customer, PersistableCustomer, MerchantStore, Language) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:567`
- `CustomerFacadeImpl.create(PersistableCustomer, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:581`
- `CustomerFacadeImpl.saveCustomer(Customer) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:610`
- `CustomerFacadeImpl.userExist(String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:619`
- `CustomerFacadeImpl.getListOfGroups(GroupType) -> List<Group>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:624`
- `CustomerFacadeImpl.convertPersistableCustomerToCustomer(PersistableCustomer, MerchantStore) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:633`
- `CustomerFacadeImpl.notifyNewCustomer(PersistableCustomer, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:658`
- `CustomerFacadeImpl.updateAuthCustomer(PersistableCustomer, MerchantStore) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:671`
- `CustomerFacadeImpl.update(PersistableCustomer, MerchantStore) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:692`
- `CustomerFacadeImpl.saveOrUpdateCustomerReview(PersistableCustomerReview, MerchantStore, Language) -> PersistableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:720`
- `CustomerFacadeImpl.createReview(CustomerReview) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:729`
- `CustomerFacadeImpl.convertPersistableCustomerReviewToCustomerReview(PersistableCustomerReview, MerchantStore, Language) -> CustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:738`
- `CustomerFacadeImpl.getAllCustomerReviewsByReviewed(Long, MerchantStore, Language) -> List<ReadableCustomerReview>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:751`
- `CustomerFacadeImpl.convertCustomerReviewToReadableCustomerReview(CustomerReview, MerchantStore, Language) -> ReadableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:767`
- `CustomerFacadeImpl.getCustomerById(Long) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:777`
- `CustomerFacadeImpl.deleteCustomerReview(Long, Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:783`
- `CustomerFacadeImpl.getCustomerReviewById(Long) -> CustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:794`
- `CustomerFacadeImpl.deleteCustomerReview(CustomerReview) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:799`
- `CustomerFacadeImpl.optinCustomer(PersistableCustomerOptin, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:808`
- `CustomerFacadeImpl.saveCustomerOption(CustomerOptin) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:832`
- `CustomerFacadeImpl.getOptinByCode(MerchantStore) -> Optin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:840`
- `CustomerFacadeImpl.getCustomerOptinByEmailAddress(String, MerchantStore, OptinType) -> CustomerOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:849`
- `CustomerFacadeImpl.resetPassword(Customer, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:860`
- `CustomerFacadeImpl.getCustomerByNick(String, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:921`
- `CustomerFacadeImpl.deleteByNick(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:928`
- `CustomerFacadeImpl.getByNick(String) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:934`
- `CustomerFacadeImpl.delete(Customer) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:939`
- `CustomerFacadeImpl.getListByStore(MerchantStore, CustomerCriteria, Language) -> ReadableCustomerList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:948`
- `CustomerFacadeImpl.convertCustomerListToReadableCustomerList(CustomerList, MerchantStore, Language) -> ReadableCustomerList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:955`
- `CustomerFacadeImpl.convertCustomerToReadableCustomer(Customer, MerchantStore, Language) -> ReadableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:968`
- `CustomerFacadeImpl.createCustomerReview(Long, PersistableCustomerReview, MerchantStore, Language) -> PersistableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:977`
- `CustomerFacadeImpl.updateCustomerReview(Long, Long, PersistableCustomerReview, MerchantStore, Language) -> PersistableCustomerReview` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1005`
- `CustomerFacadeImpl.deleteById(Long) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1025`
- `CustomerFacadeImpl.updateAddress(PersistableCustomer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1033`
- `CustomerFacadeImpl.updateAddress(String, PersistableCustomer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1084`
- `CustomerFacadeImpl.update(String, PersistableCustomer, MerchantStore) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1095`
- `CustomerFacadeImpl.passwordMatch(String, Customer) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1105`
- `CustomerFacadeImpl.changePassword(Customer, String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1111`

## Depends on
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:113`
- [com.salesmanager.core.business.services.customer.optin.CustomerOptinService](/modules/com.salesmanager.core.business.services.customer.optin.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:119`
- [com.salesmanager.core.business.services.customer.review.CustomerReviewService](/modules/com.salesmanager.core.business.services.customer.review.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:155`
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:131`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:125`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:140`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:122`
- [com.salesmanager.core.business.services.system.EmailService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:146`
- [com.salesmanager.core.business.services.system.optin.OptinService](/modules/com.salesmanager.core.business.services.system.optin.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:116`
- [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:134`
- [com.salesmanager.core.business.services.user.PermissionService](/modules/com.salesmanager.core.business.services.user.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:137`
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:158`
- [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:161`
- [com.salesmanager.shop.utils.EmailTemplatesUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:149`
- [com.salesmanager.shop.utils.EmailUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:164`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:167`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:128`

## Calls
- `CustomerFacadeImpl.changePassword` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:1116`
- `CustomerFacadeImpl.convertCustomerReviewToReadableCustomerReview` calls [com.salesmanager.shop.populator.customer.ReadableCustomerReviewPopulator](/modules/com.salesmanager.shop.populator.customer.md) `ReadableCustomerReviewPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:771`
- `CustomerFacadeImpl.convertCustomerToReadableCustomer` calls [com.salesmanager.shop.populator.customer.ReadableCustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `ReadableCustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:971`
- `CustomerFacadeImpl.convertPersistableCustomerReviewToCustomerReview` calls [com.salesmanager.shop.populator.customer.PersistableCustomerReviewPopulator](/modules/com.salesmanager.shop.populator.customer.md) `PersistableCustomerReviewPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:744`
- `CustomerFacadeImpl.convertPersistableCustomerToCustomer` calls [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:638`
- `CustomerFacadeImpl.createReview` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:731`
- `CustomerFacadeImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:942`
- `CustomerFacadeImpl.deleteCustomerReview` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:801`
- `CustomerFacadeImpl.getAddress` calls [com.salesmanager.shop.populator.customer.CustomerBillingAddressPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerBillingAddressPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:480`
- `CustomerFacadeImpl.getAddress` calls [com.salesmanager.shop.populator.customer.CustomerDeliveryAddressPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerDeliveryAddressPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:489`
- `CustomerFacadeImpl.getCustomerDataByUserName` calls [com.salesmanager.shop.populator.customer.CustomerEntityPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerEntityPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:189`
- `CustomerFacadeImpl.getCustomerModel` calls [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:377`
- `CustomerFacadeImpl.getCustomerOptinByEmailAddress` calls [com.salesmanager.core.business.services.customer.optin.CustomerOptinService](/modules/com.salesmanager.core.business.services.customer.optin.md) `CustomerOptinService.findByEmailAddress` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:852`
- `CustomerFacadeImpl.getCustomerOptinByEmailAddress` calls [com.salesmanager.core.model.system.optin.OptinType](/modules/com.salesmanager.core.model.system.optin.md) `OptinType.name` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:852`
- `CustomerFacadeImpl.getListOfGroups` calls [com.salesmanager.core.business.services.user.GroupService](/modules/com.salesmanager.core.business.services.user.md) `GroupService.listGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:626`
- `CustomerFacadeImpl.mergeCart` calls [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `ShoppingCartService.mergeShoppingCarts`, `ShoppingCartService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:239`
- `CustomerFacadeImpl.notifyNewCustomer` calls [com.salesmanager.shop.utils.EmailTemplatesUtils](/modules/com.salesmanager.shop.utils.md) `EmailTemplatesUtils.sendRegistrationEmail` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:664`
- `CustomerFacadeImpl.populateCustomerModel` calls [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `CustomerService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:576`
- `CustomerFacadeImpl.populateCustomerModel` calls [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:573`
- `CustomerFacadeImpl.registerCustomer` calls [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `CustomerService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:362`
- `CustomerFacadeImpl.resetPassword` calls [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `CustomerService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:870`
- `CustomerFacadeImpl.resetPassword` calls [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `LanguageService.toLocale` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:876`
- `CustomerFacadeImpl.resetPassword` calls [com.salesmanager.core.business.services.system.EmailService](/modules/com.salesmanager.core.business.services.system.md) `EmailService.sendHtmlEmail` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:912`
- `CustomerFacadeImpl.resetPassword` calls [com.salesmanager.shop.utils.EmailUtils](/modules/com.salesmanager.shop.utils.md) `EmailUtils.createEmailObjectsMap` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:887`
- `CustomerFacadeImpl.saveCustomer` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:612`
- `CustomerFacadeImpl.saveCustomerOption` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:834`
- `CustomerFacadeImpl.update` calls [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:702`
- `CustomerFacadeImpl.updateAddress` calls [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `CustomerService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:552`
- `CustomerFacadeImpl.updateAddress` calls [com.salesmanager.shop.populator.customer.PersistableCustomerBillingAddressPopulator](/modules/com.salesmanager.shop.populator.customer.md) `PersistableCustomerBillingAddressPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:513`
- `CustomerFacadeImpl.updateAddress` calls [com.salesmanager.shop.populator.customer.PersistableCustomerShippingAddressPopulator](/modules/com.salesmanager.shop.populator.customer.md) `PersistableCustomerShippingAddressPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:532`
- `CustomerFacadeImpl.updateAuthCustomer` calls [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/customer/facade/CustomerFacadeImpl.java:680`
