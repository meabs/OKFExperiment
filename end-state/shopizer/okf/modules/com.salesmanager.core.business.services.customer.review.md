---
type: Code Module
title: "com.salesmanager.core.business.services.customer.review"
description: "com.salesmanager.core.business.services.customer.review: CustomerReviewServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java"
    sha256: "b582a680abca7e0bd2f7c2071ff9ad129dbdebe20353122d279c7d738fd751dd"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java"
    sha256: "06c86768a28a0751d28db54452a4f1dd22b592d79d38755aceec5812bbb66b33"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.customer.review

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java`

## Types
- `CustomerReviewService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java:9`
- `CustomerReviewServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:18`

## Fields
- `CustomerReviewServiceImpl.customerReviewRepository: CustomerReviewRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:22`
- `CustomerReviewServiceImpl.customerService: CustomerService` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:25`

## Functions and methods
- `CustomerReviewService.getByCustomer(Customer) -> List<CustomerReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java:17`
- `CustomerReviewService.getByReviewedCustomer(Customer) -> List<CustomerReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java:24`
- `CustomerReviewService.getByReviewerAndReviewed(Long, Long) -> CustomerReview` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewService.java:32`
- `CustomerReviewServiceImpl.saveOrUpdate(CustomerReview) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:35`
- `CustomerReviewServiceImpl.update(CustomerReview) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:79`
- `CustomerReviewServiceImpl.create(CustomerReview) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:83`
- `CustomerReviewServiceImpl.getByCustomer(Customer) -> List<CustomerReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:89`
- `CustomerReviewServiceImpl.getByReviewedCustomer(Customer) -> List<CustomerReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:95`
- `CustomerReviewServiceImpl.getByReviewerAndReviewed(Long, Long) -> CustomerReview` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:102`

## Depends on
- [com.salesmanager.core.business.repositories.customer.review.CustomerReviewRepository](/modules/com.salesmanager.core.business.repositories.customer.review.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:22`
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:24`

## Calls
- `CustomerReviewServiceImpl.getByCustomer` calls [com.salesmanager.core.business.repositories.customer.review.CustomerReviewRepository](/modules/com.salesmanager.core.business.repositories.customer.review.md) `CustomerReviewRepository.findByReviewer` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:92`
- `CustomerReviewServiceImpl.getByReviewedCustomer` calls [com.salesmanager.core.business.repositories.customer.review.CustomerReviewRepository](/modules/com.salesmanager.core.business.repositories.customer.review.md) `CustomerReviewRepository.findByReviewed` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:98`
- `CustomerReviewServiceImpl.getByReviewerAndReviewed` calls [com.salesmanager.core.business.repositories.customer.review.CustomerReviewRepository](/modules/com.salesmanager.core.business.repositories.customer.review.md) `CustomerReviewRepository.findByRevieweAndReviewed` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:106`
- `CustomerReviewServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/customer/review/CustomerReviewServiceImpl.java:72`
