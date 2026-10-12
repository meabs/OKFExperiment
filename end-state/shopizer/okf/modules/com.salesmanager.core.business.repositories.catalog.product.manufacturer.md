---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.manufacturer"
description: "com.salesmanager.core.business.repositories.catalog.product.manufacturer: countByProduct, findByStoreAndLanguage, findOne, findByStore"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java"
    sha256: "ef59065ae6f6c2df88e88f0cdecd21645983e10f871181031b9e53b25c36561c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/PageableManufacturerRepository.java"
    sha256: "87eb2c3b1cb9dd980d2c31d29aeedac623690bcd114b70c6d62004752b21177c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.manufacturer

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/PageableManufacturerRepository.java`

## Types
- `ManufacturerRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:8`
- `PageableManufacturerRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/PageableManufacturerRepository.java:9`

## Functions and methods
- `ManufacturerRepository.countByProduct(Long) -> Long` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:10`
- `ManufacturerRepository.findByStoreAndLanguage(Integer, Integer) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:13`
- `ManufacturerRepository.findOne(Long) -> Manufacturer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:16`
- `ManufacturerRepository.findByStore(Integer) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:19`
- `ManufacturerRepository.findByStore(Integer, Integer, String) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:22`
- `ManufacturerRepository.findByCategoriesAndLanguage(List<Long>, Integer) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:28`
- `ManufacturerRepository.findByCodeAndMerchandStore(String, Integer) -> Manufacturer` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:31`
- `ManufacturerRepository.count(Integer) -> int` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:34`
- `ManufacturerRepository.findByProductInCategoryId(Integer, String, Integer) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/ManufacturerRepository.java:37`
- `PageableManufacturerRepository.findByStore(Integer, Integer, String, Pageable) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/PageableManufacturerRepository.java:11`
- `PageableManufacturerRepository.findByStore(Integer, String, Pageable) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/manufacturer/PageableManufacturerRepository.java:14`
