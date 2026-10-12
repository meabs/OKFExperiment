---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.review"
description: "com.salesmanager.core.business.services.catalog.product.review: ProductReviewServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java"
    sha256: "823bef005a14d6151bd588fb8dda364759fbcbfeedef9018097d1b5ae004c5e6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java"
    sha256: "68a58472680e85239fef7719b29e038dafa7ea9df536ec455c7d2d92127ff0b1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.review

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java`

## Types
- `ProductReviewService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java:11`
- `ProductReviewServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:20`

## Fields
- `ProductReviewServiceImpl.productReviewRepository: ProductReviewRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:26`
- `ProductReviewServiceImpl.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:29`

## Functions and methods
- `ProductReviewService.getByCustomer(Customer) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java:15`
- `ProductReviewService.getByProduct(Product) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java:16`
- `ProductReviewService.getByProduct(Product, Language) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java:17`
- `ProductReviewService.getByProductAndCustomer(Long, Long) -> ProductReview` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java:18`
- `ProductReviewService.getByProductNoCustomers(Product) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewService.java:23`
- `ProductReviewServiceImpl.getByCustomer(Customer) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:38`
- `ProductReviewServiceImpl.getByProduct(Product) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:43`
- `ProductReviewServiceImpl.getByProductAndCustomer(Long, Long) -> ProductReview` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:48`
- `ProductReviewServiceImpl.getByProduct(Product, Language) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:53`
- `ProductReviewServiceImpl.saveOrUpdate(ProductReview) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:58`
- `ProductReviewServiceImpl.update(ProductReview) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:101`
- `ProductReviewServiceImpl.create(ProductReview) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:105`
- `ProductReviewServiceImpl.getByProductNoCustomers(Product) -> List<ProductReview>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:112`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.review.ProductReviewRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.review.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:26`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:28`

## Calls
- `ProductReviewServiceImpl.getByCustomer` calls [com.salesmanager.core.business.repositories.catalog.product.review.ProductReviewRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.review.md) `ProductReviewRepository.findByCustomer` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:40`
- `ProductReviewServiceImpl.getByProduct` calls [com.salesmanager.core.business.repositories.catalog.product.review.ProductReviewRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.review.md) `ProductReviewRepository.findByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:45`
- `ProductReviewServiceImpl.getByProductAndCustomer` calls [com.salesmanager.core.business.repositories.catalog.product.review.ProductReviewRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.review.md) `ProductReviewRepository.findByProductAndCustomer` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:50`
- `ProductReviewServiceImpl.getByProductNoCustomers` calls [com.salesmanager.core.business.repositories.catalog.product.review.ProductReviewRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.review.md) `ProductReviewRepository.findByProductNoCustomers` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:114`
- `ProductReviewServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/review/ProductReviewServiceImpl.java:95`
