---
type: Code Module
title: "com.salesmanager.core.business.repositories.customer.attribute"
description: "com.salesmanager.core.business.repositories.customer.attribute: findOne, findByOptionId, findByOptionId, findByCustomerId"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java"
    sha256: "21082b4587c6b50aa65bbe99bbc5ff9b1eec98e222dd37db83261db564ee83a4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionRepository.java"
    sha256: "ed05b4324dab7c8da3f71779660cf5d535c35f4760e02c9d91b1e287dfaacdb0"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java"
    sha256: "3af03c899d25a5c0a5940b5bc404cce746b8c6deeacd2859af1aff7f660f36b3"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionValueRepository.java"
    sha256: "8c1c047d8622d4bb695f47c5a0635b0df7fe760206df95342154167a828a24c2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.customer.attribute

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionValueRepository.java`

## Types
- `CustomerAttributeRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java:10`
- `CustomerOptionRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionRepository.java:10`
- `CustomerOptionSetRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java:10`
- `CustomerOptionValueRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionValueRepository.java:9`

## Functions and methods
- `CustomerAttributeRepository.findOne(Long) -> CustomerAttribute` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java:13`
- `CustomerAttributeRepository.findByOptionId(Integer, Long, Long) -> CustomerAttribute` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java:16`
- `CustomerAttributeRepository.findByOptionId(Integer, Long) -> List<CustomerAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java:19`
- `CustomerAttributeRepository.findByCustomerId(Integer, Long) -> List<CustomerAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java:22`
- `CustomerAttributeRepository.findByOptionValueId(Integer, Long) -> List<CustomerAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerAttributeRepository.java:25`
- `CustomerOptionRepository.findOne(Long) -> CustomerOption` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionRepository.java:13`
- `CustomerOptionRepository.findByCode(Integer, String) -> CustomerOption` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionRepository.java:16`
- `CustomerOptionRepository.findByStore(Integer, Integer) -> List<CustomerOption>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionRepository.java:19`
- `CustomerOptionSetRepository.findOne(Long) -> CustomerOptionSet` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java:13`
- `CustomerOptionSetRepository.findByOptionId(Integer, Long) -> List<CustomerOptionSet>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java:16`
- `CustomerOptionSetRepository.findByOptionValueId(Integer, Long) -> List<CustomerOptionSet>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java:19`
- `CustomerOptionSetRepository.findByStore(Integer, Integer) -> List<CustomerOptionSet>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionSetRepository.java:22`
- `CustomerOptionValueRepository.findOne(Long) -> CustomerOptionValue` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionValueRepository.java:12`
- `CustomerOptionValueRepository.findByCode(Integer, String) -> CustomerOptionValue` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionValueRepository.java:15`
- `CustomerOptionValueRepository.findByStore(Integer, Integer) -> List<CustomerOptionValue>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/customer/attribute/CustomerOptionValueRepository.java:18`
