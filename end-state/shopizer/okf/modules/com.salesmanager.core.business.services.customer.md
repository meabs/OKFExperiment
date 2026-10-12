---
type: Code Module
title: "com.salesmanager.core.business.services.customer"
description: "com.salesmanager.core.business.services.customer: CustomerServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java"
    sha256: "5a427a849482651039e27c82bf6b2289fb100966576ff0651029f209e1a240f6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java"
    sha256: "1a3f18f50cf5a029230c58cb82dbf8884d91deb688ad6dcefbee13c61c4a82c7"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.customer

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java`

## Types
- `CustomerService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:16`
- `CustomerServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:25`

## Fields
- `CustomerServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:28`
- `CustomerServiceImpl.customerRepository: CustomerRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:30`
- `CustomerServiceImpl.customerAttributeService: CustomerAttributeService` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:33`
- `CustomerServiceImpl.geoLocation: GeoLocation` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:36`

## Functions and methods
- `CustomerService.getByName(String) -> List<Customer>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:18`
- `CustomerService.getListByStore(MerchantStore) -> List<Customer>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:20`
- `CustomerService.getByNick(String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:22`
- `CustomerService.saveOrUpdate(Customer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:24`
- `CustomerService.getListByStore(MerchantStore, CustomerCriteria) -> CustomerList` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:26`
- `CustomerService.getByNick(String, int) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:28`
- `CustomerService.getByNick(String, String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:29`
- `CustomerService.getByPasswordResetToken(String, String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:37`
- `CustomerService.getCustomerAddress(MerchantStore, String) -> Address` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerService.java:46`
- `CustomerServiceImpl.getByName(String) -> List<Customer>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:45`
- `CustomerServiceImpl.getById(Long) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:50`
- `CustomerServiceImpl.getByNick(String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:55`
- `CustomerServiceImpl.getByNick(String, int) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:60`
- `CustomerServiceImpl.getListByStore(MerchantStore) -> List<Customer>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:65`
- `CustomerServiceImpl.getListByStore(MerchantStore, CustomerCriteria) -> CustomerList` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:70`
- `CustomerServiceImpl.getCustomerAddress(MerchantStore, String) -> Address` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:75`
- `CustomerServiceImpl.saveOrUpdate(Customer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:86`
- `CustomerServiceImpl.delete(Customer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:100`
- `CustomerServiceImpl.getByNick(String, String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:114`
- `CustomerServiceImpl.getByPasswordResetToken(String, String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:119`

## Depends on
- [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:30`
- [com.salesmanager.core.business.services.customer.attribute.CustomerAttributeService](/modules/com.salesmanager.core.business.services.customer.attribute.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:32`
- [com.salesmanager.core.modules.utils.GeoLocation](/modules/com.salesmanager.core.modules.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:35`

## Calls
- `CustomerServiceImpl.delete` calls [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:110`
- `CustomerServiceImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:107`
- `CustomerServiceImpl.getById` calls [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:52`
- `CustomerServiceImpl.getByName` calls [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepository.findByName` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:47`
- `CustomerServiceImpl.getByNick` calls [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepository.findByNick` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:57`
- `CustomerServiceImpl.getByPasswordResetToken` calls [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepository.findByResetPasswordToken` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:121`
- `CustomerServiceImpl.getListByStore` calls [com.salesmanager.core.business.repositories.customer.CustomerRepository](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepository.findByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:67`
- `CustomerServiceImpl.getListByStore` calls [com.salesmanager.core.business.repositories.customer.CustomerRepositoryCustom](/modules/com.salesmanager.core.business.repositories.customer.md) `CustomerRepositoryCustom.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/CustomerServiceImpl.java:72`
