---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.review"
description: "com.salesmanager.core.business.repositories.catalog.product.review: findOne, findByCustomer, findByProduct, findByProductNoCustomers"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java"
    sha256: "4c0fa2f34fc1ba78490a4c31c1ec16cbfaa301e175e844346fd7e3eca5fb9e72"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.review

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java`

## Types
- `ProductReviewRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:10`

## Functions and methods
- `ProductReviewRepository.findOne(Long) -> ProductReview` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:13`
- `ProductReviewRepository.findByCustomer(Long) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:16`
- `ProductReviewRepository.findByProduct(Long) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:19`
- `ProductReviewRepository.findByProductNoCustomers(Long) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:22`
- `ProductReviewRepository.findByProduct(Long, Integer) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:25`
- `ProductReviewRepository.findByProductAndCustomer(Long, Long) -> ProductReview` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/review/ProductReviewRepository.java:28`
