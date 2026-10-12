---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.variant"
description: "com.salesmanager.core.business.repositories.catalog.product.variant: findByProductId, findByProductId, findOne, finByProductVariant"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantGroupRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantGroupRepository.java"
    sha256: "f6215344b37a0009440fe821414344901104aac3a20ad1da8fa8c659960a1f2c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantRepositoty.java"
    sha256: "757040b6c1c1b8ac8f1152339b7f77c69ebbc51014eca45eba88d67a458b9b50"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantGroupRepository.java"
    sha256: "a5e7246a1331b771d4f1c60b4e5f81a02635fa99b48a16bf46016ddd8a22b4a1"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java"
    sha256: "87eb2497abfae5da64e2b9b913c712e39eb410f591b4117cd4132b5658f801a8"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java"
    sha256: "39b9771ba6d13196e574144be7d94eca8b28163329b216d6ff63c81c31c5fabb"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.variant

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantGroupRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantRepositoty.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantGroupRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java`

## Types
- `PageableProductVariantGroupRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantGroupRepository.java:10`
- `PageableProductVariantRepositoty` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantRepositoty.java:10`
- `ProductVariantGroupRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantGroupRepository.java:11`
- `ProductVariantImageRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java:10`
- `ProductVariantRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:11`

## Functions and methods
- `PageableProductVariantGroupRepository.findByProductId(Integer, Long, Pageable) -> Page<ProductVariantGroup>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantGroupRepository.java:15`
- `PageableProductVariantRepositoty.findByProductId(Integer, Long, Pageable) -> Page<ProductVariant>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/PageableProductVariantRepositoty.java:14`
- `ProductVariantGroupRepository.findOne(Long, String) -> Optional<ProductVariantGroup>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantGroupRepository.java:14`
- `ProductVariantGroupRepository.finByProductVariant(Long, String) -> Optional<ProductVariantGroup>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantGroupRepository.java:22`
- `ProductVariantGroupRepository.finByProduct(Long, String) -> List<ProductVariantGroup>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantGroupRepository.java:31`
- `ProductVariantImageRepository.findOne(Long) -> ProductVariantImage` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java:12`
- `ProductVariantImageRepository.finByProduct(Long, String) -> List<ProductVariantImage>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java:19`
- `ProductVariantImageRepository.finByProductVariantGroup(Long, String) -> List<ProductVariantImage>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java:28`
- `ProductVariantImageRepository.finByProductVariant(Long, String) -> List<ProductVariantImage>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantImageRepository.java:48`
- `ProductVariantRepository.findOne(Long, Integer) -> Optional<ProductVariant>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:16`
- `ProductVariantRepository.findByIds(List<Long>, Integer) -> List<ProductVariant>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:33`
- `ProductVariantRepository.findById(Long, Long, Integer) -> Optional<ProductVariant>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:51`
- `ProductVariantRepository.findBySku(String, Long, Integer, Integer) -> Optional<ProductVariant>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:70`
- `ProductVariantRepository.findByProductId(Integer, Long) -> List<ProductVariant>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:98`
- `ProductVariantRepository.existsBySkuAndProduct(String, Long) -> ProductVariant` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/variant/ProductVariantRepository.java:122`
