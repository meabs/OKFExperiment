---
type: Code Module
title: "com.salesmanager.core.business.repositories.customer"
description: "com.salesmanager.core.business.repositories.customer: CustomerRepositoryImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java"
    sha256: "be731acf2394c18e2729e02a5335087899640598f8fd5bbbb9be99daf1ac3794"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryCustom.java"
    sha256: "b13a9acb4532601ba3f2ac765c6b6ff38f6a33bef1d3b6846617076a2b93cc4d"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryImpl.java"
    sha256: "8e5a883b0891e69f2d8e6063867fd36fd5ad2d2d81bfc69cd543b602d6550544"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.customer

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryCustom.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryImpl.java`

## Types
- `CustomerRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository`, [com.salesmanager.core.business.repositories.customer.CustomerRepositoryCustom](/modules/com.salesmanager.core.business.repositories.customer.md) `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:10`
- `CustomerRepositoryCustom` (interface) `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryCustom.java:9`
- `CustomerRepositoryImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryImpl.java:14`

## Fields
- `CustomerRepositoryImpl.em: EntityManager` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryImpl.java:18`

## Functions and methods
- `CustomerRepository.findOne(Long) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:13`
- `CustomerRepository.findByName(String) -> List<Customer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:16`
- `CustomerRepository.findByNick(String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:19`
- `CustomerRepository.findByNick(String, int) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:22`
- `CustomerRepository.findByNick(String, String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:40`
- `CustomerRepository.findByResetPasswordToken(String, String) -> Customer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:58`
- `CustomerRepository.findByStore(int) -> List<Customer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepository.java:76`
- `CustomerRepositoryCustom.listByStore(MerchantStore, CustomerCriteria) -> CustomerList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryCustom.java:11`
- `CustomerRepositoryImpl.listByStore(MerchantStore, CustomerCriteria) -> CustomerList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/CustomerRepositoryImpl.java:20`
