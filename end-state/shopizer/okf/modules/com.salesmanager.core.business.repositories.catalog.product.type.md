---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.type"
description: "com.salesmanager.core.business.repositories.catalog.product.type: listByStore, findByCode, findByCode, findById"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/PageableProductTypeRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/PageableProductTypeRepository.java"
    sha256: "6e2e7fcf43313f33181bf7f72b88bad82b1e9de3e3fda670c35badd0a6d69942"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java"
    sha256: "3a6debaa6ca834d370138444722b9b9803a384bde2f712b6e0e426a21ae00d59"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.type

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/PageableProductTypeRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java`

## Types
- `PageableProductTypeRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/PageableProductTypeRepository.java:10`
- `ProductTypeRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java:10`

## Functions and methods
- `PageableProductTypeRepository.listByStore(Integer, Pageable) -> Page<ProductType>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/PageableProductTypeRepository.java:13`
- `ProductTypeRepository.findByCode(String) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java:12`
- `ProductTypeRepository.findByCode(String, Integer) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java:15`
- `ProductTypeRepository.findById(Long, Integer, int) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java:18`
- `ProductTypeRepository.findById(Long, Integer) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java:21`
- `ProductTypeRepository.findByIds(List<Long>, Integer, int) -> List<ProductType>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/type/ProductTypeRepository.java:24`
