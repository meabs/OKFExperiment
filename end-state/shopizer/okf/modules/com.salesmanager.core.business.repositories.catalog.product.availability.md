---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.availability"
description: "com.salesmanager.core.business.repositories.catalog.product.availability: listByStore, listByStore, getByProductId, getBySku"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java"
    sha256: "49acb4d38480ea532189907bdbce86c11b71eed1547fd9dacfcb4ae4d3fc0b98"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java"
    sha256: "ce0ddf29a6b728acaf21deb07d157e6320664ce999d2f7a49e91b22754a66607"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.availability

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java`

## Types
- `PageableProductAvailabilityRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java:10`
- `ProductAvailabilityRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java:10`

## Functions and methods
- `PageableProductAvailabilityRepository.listByStore(Long, Integer, String, Pageable) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java:12`
- `PageableProductAvailabilityRepository.listByStore(Integer, Pageable) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java:21`
- `PageableProductAvailabilityRepository.getByProductId(Long, String, Pageable) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java:28`
- `PageableProductAvailabilityRepository.getBySku(String, String, Pageable) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java:42`
- `PageableProductAvailabilityRepository.getBySku(String, Pageable) -> Page<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/PageableProductAvailabilityRepository.java:53`
- `ProductAvailabilityRepository.getById(Long) -> ProductAvailability` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java:13`
- `ProductAvailabilityRepository.getById(Long, int) -> ProductAvailability` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java:23`
- `ProductAvailabilityRepository.getBySku(String, String) -> List<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java:35`
- `ProductAvailabilityRepository.getBySku(String) -> List<ProductAvailability>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/availability/ProductAvailabilityRepository.java:46`
