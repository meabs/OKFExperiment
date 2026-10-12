---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.availability"
description: "com.salesmanager.core.business.services.catalog.product.availability: ProductAvailabilityServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java"
    sha256: "5dc5c18ea9da4e2a4a7802b260afc60e1d6fdfe80fd685e50ca0fef342237ac2"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java"
    sha256: "c8d5c017ebc586bb2b7ebfdf70a55fe2d9979ea94273905b503b7e9be5faec08"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.availability

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java`

## Types
- `ProductAvailabilityService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:13`
- `ProductAvailabilityServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:30`

## Fields
- `ProductAvailabilityServiceImpl.productAvailabilityRepository: ProductAvailabilityRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:34`
- `ProductAvailabilityServiceImpl.pageableProductAvailabilityRepository: PageableProductAvailabilityRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:37`

## Functions and methods
- `ProductAvailabilityService.saveOrUpdate(ProductAvailability) -> ProductAvailability` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:16`
- `ProductAvailabilityService.listByProduct(Long, MerchantStore, int, int) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:18`
- `ProductAvailabilityService.getBySku(String, MerchantStore, int, int) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:26`
- `ProductAvailabilityService.getBySku(String, int, int) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:34`
- `ProductAvailabilityService.getBySku(String, MerchantStore) -> List<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:42`
- `ProductAvailabilityService.getById(Long, MerchantStore) -> Optional<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityService.java:44`
- `ProductAvailabilityServiceImpl.saveOrUpdate(ProductAvailability) -> ProductAvailability` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:45`
- `ProductAvailabilityServiceImpl.isPositive(Long) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:56`
- `ProductAvailabilityServiceImpl.listByProduct(Long, MerchantStore, int, int) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:62`
- `ProductAvailabilityServiceImpl.getById(Long, MerchantStore) -> Optional<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:73`
- `ProductAvailabilityServiceImpl.getBySku(String, MerchantStore, int, int) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:79`
- `ProductAvailabilityServiceImpl.getBySku(String, int, int) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:86`
- `ProductAvailabilityServiceImpl.getBySku(String, MerchantStore) -> List<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:92`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.availability.PageableProductAvailabilityRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.availability.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:36`
- [com.salesmanager.core.business.repositories.catalog.product.availability.ProductAvailabilityRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.availability.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/availability/ProductAvailabilityServiceImpl.java:34`
