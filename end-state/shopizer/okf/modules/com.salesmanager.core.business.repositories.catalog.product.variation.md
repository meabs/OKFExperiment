---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.variation"
description: "com.salesmanager.core.business.repositories.catalog.product.variation: list, findOne, findOne, findByCode"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/PageableProductVariationRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/PageableProductVariationRepository.java"
    sha256: "c9391b1410f90f70d32099bf7506052dfc9548918cec850ac936eae4a8b956bc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java"
    sha256: "129890064a9cafd17c59990da8017cd7bd00b6b15fa010dc3669be9a0a3c9b0e"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.variation

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/PageableProductVariationRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java`

## Types
- `PageableProductVariationRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/PageableProductVariationRepository.java:10`
- `ProductVariationRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java:11`

## Functions and methods
- `PageableProductVariationRepository.list(int, String, Pageable) -> Page<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/PageableProductVariationRepository.java:13`
- `ProductVariationRepository.findOne(Integer, Long, Integer) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java:13`
- `ProductVariationRepository.findOne(Integer, Long) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java:21`
- `ProductVariationRepository.findByCode(String, Integer) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java:29`
- `ProductVariationRepository.findByIds(Integer, List<Long>) -> List<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variation/ProductVariationRepository.java:32`
