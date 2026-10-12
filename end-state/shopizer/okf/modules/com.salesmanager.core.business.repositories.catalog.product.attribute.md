---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.attribute"
description: "com.salesmanager.core.business.repositories.catalog.product.attribute: findByProductId, findByProductId, listOptions, listOptionValues"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductAttributeRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductAttributeRepository.java"
    sha256: "874198289e02904f39788c0a7cf8f2065fb3b48d3e3fb6f2558a20b1ab7a2df0"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionRepository.java"
    sha256: "d011332ede6e6bcb212c0e829137cf2e7eae0d8a000c85f6013bcfa0fbb3b8de"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionValueRepository.java"
    sha256: "734ea5cf71c0cc56f6067841b122f4fc5502745846662c4816ddac197559cf9c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java"
    sha256: "08c9e643bad44210197a205e76c5b95130251c5c7c8abf1091a1308b37f4aa49"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java"
    sha256: "f12c197b35a729a54c8933d43539d0d14fae1faeb1a0edb91dde027cb2f4ab99"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java"
    sha256: "56b21dc8eb61fa4c8891d3664f65fe7e86de80dae2a7a05f2a81c207a3992c26"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java"
    sha256: "8c53a0054b02c260ee297cd8f7d2fd0c87c5101aaf0d3c6f3fb82c8fa086adb2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.attribute

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductAttributeRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionValueRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java`

## Types
- `PageableProductAttributeRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductAttributeRepository.java:11`
- `PageableProductOptionRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionRepository.java:9`
- `PageableProductOptionValueRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionValueRepository.java:10`
- `ProductAttributeRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:10`
- `ProductOptionRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:10`
- `ProductOptionSetRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java:10`
- `ProductOptionValueRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:10`

## Functions and methods
- `PageableProductAttributeRepository.findByProductId(Integer, Long, Integer, Pageable) -> Page<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductAttributeRepository.java:13`
- `PageableProductAttributeRepository.findByProductId(Integer, Long, Pageable) -> Page<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductAttributeRepository.java:28`
- `PageableProductOptionRepository.listOptions(int, String, Pageable) -> Page<ProductOption>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionRepository.java:11`
- `PageableProductOptionValueRepository.listOptionValues(int, String, Pageable) -> Page<ProductOptionValue>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/PageableProductOptionValueRepository.java:12`
- `ProductAttributeRepository.findOne(Long) -> ProductAttribute` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:12`
- `ProductAttributeRepository.findByOptionId(Integer, Long) -> List<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:15`
- `ProductAttributeRepository.findByOptionValueId(Integer, Long) -> List<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:18`
- `ProductAttributeRepository.findByAttributeIds(Integer, Long, List<Long>) -> List<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:21`
- `ProductAttributeRepository.findByProductId(Integer, Long) -> List<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:31`
- `ProductAttributeRepository.findOptionsByCategoryLineage(Integer, String, Integer) -> List<ProductAttribute>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductAttributeRepository.java:34`
- `ProductOptionRepository.findOne(Long) -> ProductOption` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:12`
- `ProductOptionRepository.findOne(Integer, Long) -> ProductOption` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:15`
- `ProductOptionRepository.findByStoreId(Integer, Integer) -> List<ProductOption>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:18`
- `ProductOptionRepository.findByName(Integer, String, Integer) -> List<ProductOption>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:21`
- `ProductOptionRepository.findByCode(Integer, String) -> ProductOption` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:24`
- `ProductOptionRepository.findByReadOnly(Integer, Integer, boolean) -> List<ProductOption>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionRepository.java:27`
- `ProductOptionSetRepository.findOne(Integer, Long, Integer) -> ProductOptionSet` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java:12`
- `ProductOptionSetRepository.findByStore(Integer, Integer) -> List<ProductOptionSet>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java:15`
- `ProductOptionSetRepository.findByProductType(Long, Integer, Integer) -> List<ProductOptionSet>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java:18`
- `ProductOptionSetRepository.findByCode(Integer, String) -> ProductOptionSet` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionSetRepository.java:26`
- `ProductOptionValueRepository.findOne(Long) -> ProductOptionValue` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:12`
- `ProductOptionValueRepository.findOne(Integer, Long) -> ProductOptionValue` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:15`
- `ProductOptionValueRepository.findByStoreId(Integer, Integer) -> List<ProductOptionValue>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:18`
- `ProductOptionValueRepository.findByCode(Integer, String) -> ProductOptionValue` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:21`
- `ProductOptionValueRepository.findByName(Integer, String, Integer) -> List<ProductOptionValue>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:24`
- `ProductOptionValueRepository.findByReadOnly(Integer, Integer, boolean) -> List<ProductOptionValue>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/attribute/ProductOptionValueRepository.java:27`
