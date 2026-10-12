---
type: Code Module
title: "com.salesmanager.core.model.customer.review"
description: "com.salesmanager.core.model.customer.review: CustomerReview, CustomerReviewDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java"
    sha256: "3b0996ba20add78fa5ad02e817d4bdea541fc13398aa56e74f600752a512a3c5"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java"
    sha256: "f1791a56deb89335b301382a4ff62b5b6af2470603b4f204f7d0ca6776ffa6a1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.customer.review

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java`

## Types
- `CustomerReview` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:33`
- `CustomerReviewDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java:29`

## Fields
- `CustomerReview.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:50`
- `CustomerReview.audit: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:53`
- `CustomerReview.reviewRating: Double` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:56`
- `CustomerReview.reviewRead: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:59`
- `CustomerReview.reviewDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:63`
- `CustomerReview.status: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:66`
- `CustomerReview.customer: Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:70`
- `CustomerReview.reviewedCustomer: Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:76`
- `CustomerReview.descriptions: Set<CustomerReviewDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:87`
- `CustomerReviewDescription.customerReview: CustomerReview` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java:44`

## Functions and methods
- `CustomerReview.getReviewedCustomer() -> Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:78`
- `CustomerReview.setReviewedCustomer(Customer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:82`
- `CustomerReview.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:92`
- `CustomerReview.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:96`
- `CustomerReview.getReviewRating() -> Double` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:100`
- `CustomerReview.setReviewRating(Double) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:104`
- `CustomerReview.getReviewRead() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:108`
- `CustomerReview.setReviewRead(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:112`
- `CustomerReview.getStatus() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:116`
- `CustomerReview.setStatus(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:120`
- `CustomerReview.getCustomer() -> Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:124`
- `CustomerReview.setCustomer(Customer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:128`
- `CustomerReview.getDescriptions() -> Set<CustomerReviewDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:133`
- `CustomerReview.setDescriptions(Set<CustomerReviewDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:137`
- `CustomerReview.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:141`
- `CustomerReview.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:146`
- `CustomerReview.getReviewDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:151`
- `CustomerReview.setReviewDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:155`
- `CustomerReviewDescription.getCustomerReview() -> CustomerReview` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java:46`
- `CustomerReviewDescription.setCustomerReview(CustomerReview) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java:50`

## Depends on
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:52`
- [com.salesmanager.core.model.customer.Customer](/modules/com.salesmanager.core.model.customer.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReview.java:68`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/review/CustomerReviewDescription.java:57`
