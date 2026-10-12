---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.review"
description: "com.salesmanager.core.model.catalog.product.review: ProductReview, ProductReviewDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java"
    sha256: "0e37a2cddec7eb2b53687c806e10370db4a6d07c3acdb9b38c48e8b41dd1659e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java"
    sha256: "8aa271ab2dacaae770819bb496e4702745186cf01488df0108a0456bb169b8ca"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.review

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java`

## Types
- `ProductReview` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:35`
- `ProductReviewDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java:28`

## Fields
- `ProductReview.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:52`
- `ProductReview.audit: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:55`
- `ProductReview.reviewRating: Double` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:58`
- `ProductReview.reviewRead: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:61`
- `ProductReview.reviewDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:65`
- `ProductReview.status: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:68`
- `ProductReview.customer: Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:73`
- `ProductReview.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:77`
- `ProductReview.descriptions: Set<ProductReviewDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:80`
- `ProductReviewDescription.productReview: ProductReview` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java:42`

## Functions and methods
- `ProductReview.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:85`
- `ProductReview.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:89`
- `ProductReview.getReviewRating() -> Double` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:93`
- `ProductReview.setReviewRating(Double) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:97`
- `ProductReview.getReviewRead() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:101`
- `ProductReview.setReviewRead(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:105`
- `ProductReview.getStatus() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:109`
- `ProductReview.setStatus(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:113`
- `ProductReview.getCustomer() -> Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:117`
- `ProductReview.setCustomer(Customer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:121`
- `ProductReview.getProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:125`
- `ProductReview.setProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:129`
- `ProductReview.getDescriptions() -> Set<ProductReviewDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:133`
- `ProductReview.setDescriptions(Set<ProductReviewDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:137`
- `ProductReview.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:141`
- `ProductReview.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:146`
- `ProductReview.getReviewDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:151`
- `ProductReview.setReviewDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:155`
- `ProductReviewDescription.getProductReview() -> ProductReview` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java:52`
- `ProductReviewDescription.setProductReview(ProductReview) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java:56`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:75`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:54`
- [com.salesmanager.core.model.customer.Customer](/modules/com.salesmanager.core.model.customer.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReview.java:70`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/review/ProductReviewDescription.java:47`
