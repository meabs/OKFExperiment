---
type: Code Module
title: "com.salesmanager.core.business.repositories.payments"
description: "com.salesmanager.core.business.repositories.payments: findByOrder, findByDates"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/payments/TransactionRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/payments/TransactionRepository.java"
    sha256: "5bbc1331efc2a7fb9fc3fe45b2ad9ca50871503b6210d3cd74ab84da41548ae8"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.payments

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/payments/TransactionRepository.java`

## Types
- `TransactionRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/payments/TransactionRepository.java:13`

## Functions and methods
- `TransactionRepository.findByOrder(Long) -> List<Transaction>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/payments/TransactionRepository.java:15`
- `TransactionRepository.findByDates(Date, Date) -> List<Transaction>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/payments/TransactionRepository.java:18`
