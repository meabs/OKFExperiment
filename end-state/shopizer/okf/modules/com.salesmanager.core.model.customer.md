---
type: Code Module
title: "com.salesmanager.core.model.customer"
description: "com.salesmanager.core.model.customer: Customer, CustomerCriteria, CustomerList"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java"
    sha256: "c0d13fb616484a35880123e01685c110fdff4ea2c494d78a11496e45d53038cb"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java"
    sha256: "e26c65dc196231dbb7359bd3a53923317f1e49f099d1f9a38496c70eba86cff4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerGender.java"
    sha256: "b7ef8021eb0554fd930cf7b5221b38e020263837dd6830df5116dfc210f89306"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerList.java"
    sha256: "a28582c94ee29e34e56d60fc7050922e86056ed12a1c351e220f18f1e7df8400"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.customer

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerGender.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerList.java`

## Types
- `Customer` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:52`
- `CustomerCriteria` (class) extends [com.salesmanager.core.model.common.Criteria](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:5`
- `CustomerGender` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerGender.java:3`
- `CustomerList` (class) extends [com.salesmanager.core.model.common.EntityList](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerList.java:8`

## Fields
- `Customer.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:64`
- `Customer.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:68`
- `Customer.attributes: Set<CustomerAttribute>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:71`
- `Customer.gender: CustomerGender` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:75`
- `Customer.dateOfBirth: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:80`
- `Customer.emailAddress: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:85`
- `Customer.nick: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:88`
- `Customer.company: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:91`
- `Customer.password: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:95`
- `Customer.anonymous: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:98`
- `Customer.customerReviewAvg: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:101`
- `Customer.customerReviewCount: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:104`
- `Customer.provider: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:107`
- `Customer.defaultLanguage: Language` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:112`
- `Customer.reviews: List<ProductReview>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:116`
- `Customer.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:121`
- `Customer.delivery: Delivery` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:125`
- `Customer.billing: Billing` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:129`
- `Customer.groups: List<Group>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:146`
- `Customer.showCustomerStateList: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:150`
- `Customer.showBillingStateList: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:154`
- `Customer.showDeliveryStateList: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:158`
- `Customer.credentialsResetRequest: CredentialsReset` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:161`
- `CustomerCriteria.firstName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:7`
- `CustomerCriteria.lastName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:8`
- `CustomerCriteria.name: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:9`
- `CustomerCriteria.email: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:10`
- `CustomerCriteria.country: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:11`
- `CustomerList.customers: List<Customer>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerList.java:15`

## Functions and methods
- `Customer.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:166`
- `Customer.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:170`
- `Customer.getDateOfBirth() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:176`
- `Customer.setDateOfBirth(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:180`
- `Customer.getEmailAddress() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:184`
- `Customer.setEmailAddress(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:188`
- `Customer.getNick() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:192`
- `Customer.setNick(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:196`
- `Customer.getCompany() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:200`
- `Customer.setCompany(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:204`
- `Customer.getPassword() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:210`
- `Customer.setPassword(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:214`
- `Customer.isAnonymous() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:220`
- `Customer.setAnonymous(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:224`
- `Customer.getReviews() -> List<ProductReview>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:229`
- `Customer.setReviews(List<ProductReview>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:233`
- `Customer.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:237`
- `Customer.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:241`
- `Customer.setDelivery(Delivery) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:245`
- `Customer.getDelivery() -> Delivery` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:249`
- `Customer.setBilling(Billing) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:253`
- `Customer.getBilling() -> Billing` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:257`
- `Customer.setGroups(List<Group>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:261`
- `Customer.getGroups() -> List<Group>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:265`
- `Customer.getShowCustomerStateList() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:268`
- `Customer.setShowCustomerStateList(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:272`
- `Customer.getShowBillingStateList() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:276`
- `Customer.setShowBillingStateList(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:280`
- `Customer.getShowDeliveryStateList() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:284`
- `Customer.setShowDeliveryStateList(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:288`
- `Customer.getDefaultLanguage() -> Language` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:292`
- `Customer.setDefaultLanguage(Language) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:296`
- `Customer.setAttributes(Set<CustomerAttribute>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:300`
- `Customer.getAttributes() -> Set<CustomerAttribute>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:304`
- `Customer.setGender(CustomerGender) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:308`
- `Customer.getGender() -> CustomerGender` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:312`
- `Customer.getCustomerReviewAvg() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:316`
- `Customer.setCustomerReviewAvg(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:320`
- `Customer.getCustomerReviewCount() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:324`
- `Customer.setCustomerReviewCount(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:328`
- `Customer.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:332`
- `Customer.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:337`
- `Customer.getProvider() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:342`
- `Customer.setProvider(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:346`
- `Customer.getCredentialsResetRequest() -> CredentialsReset` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:350`
- `Customer.setCredentialsResetRequest(CredentialsReset) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:354`
- `CustomerCriteria.getFirstName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:12`
- `CustomerCriteria.setFirstName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:15`
- `CustomerCriteria.getLastName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:18`
- `CustomerCriteria.setLastName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:21`
- `CustomerCriteria.getName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:24`
- `CustomerCriteria.setName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:27`
- `CustomerCriteria.getEmail() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:30`
- `CustomerCriteria.setEmail(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:33`
- `CustomerCriteria.getCountry() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:36`
- `CustomerCriteria.setCountry(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerCriteria.java:39`
- `CustomerList.setCustomers(List<Customer>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerList.java:16`
- `CustomerList.getCustomers() -> List<Customer>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/CustomerList.java:19`

## Depends on
- [com.salesmanager.core.model.catalog.product.review.ProductReview](/modules/com.salesmanager.core.model.catalog.product.review.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:115`
- [com.salesmanager.core.model.common.Billing](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:127`
- [com.salesmanager.core.model.common.CredentialsReset](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:160`
- [com.salesmanager.core.model.common.Delivery](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:124`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:66`
- [com.salesmanager.core.model.customer.attribute.CustomerAttribute](/modules/com.salesmanager.core.model.customer.attribute.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:70`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:118`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:110`
- [com.salesmanager.core.model.user.Group](/modules/com.salesmanager.core.model.user.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:131`

## Calls
- `Customer.getDateOfBirth` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:177`
- `Customer.setDateOfBirth` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/Customer.java:181`

## Tests
- `com.salesmanager.test.customer.CustomerTest`
