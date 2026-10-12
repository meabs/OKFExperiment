---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.catalog"
description: "com.salesmanager.core.business.repositories.catalog.catalog: findById, findByCode, existsByCode, listByCatalog"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogEntryRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogEntryRepository.java"
    sha256: "23c96edbbd1ef86f955f4f3dcfa839d4e478c8b4737b19996d37464fd5aa632d"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogRepository.java"
    sha256: "3a5d50d12596ddefab0d8cc0549b5d4fd49a9383aba948a4f07bbdb9a634ac44"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogEntryRepository.java"
    sha256: "c8e4a0d65c43c193a3efbc82eca53976943f0b159f6ba522f42b7bc382d82375"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogRepository.java"
    sha256: "83dc54e4b7562e6cf42e5fc2ddb90e4f4094922a9aba738c1743256fb59ecc4c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.catalog

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogEntryRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogEntryRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogRepository.java`

## Types
- `CatalogEntryRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogEntryRepository.java:7`
- `CatalogRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogRepository.java:10`
- `PageableCatalogEntryRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogEntryRepository.java:10`
- `PageableCatalogRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogRepository.java:10`

## Functions and methods
- `CatalogRepository.findById(Long, Integer) -> Optional<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogRepository.java:13`
- `CatalogRepository.findByCode(String, Integer) -> Optional<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogRepository.java:20`
- `CatalogRepository.existsByCode(String, Integer) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/CatalogRepository.java:27`
- `PageableCatalogEntryRepository.listByCatalog(Long, Integer, Integer, String, Pageable) -> Page<CatalogCategoryEntry>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogEntryRepository.java:23`
- `PageableCatalogRepository.listByStore(Integer, String, Pageable) -> Page<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/catalog/PageableCatalogRepository.java:13`
