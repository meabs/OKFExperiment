---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.variation"
description: "com.salesmanager.core.business.services.catalog.product.variation: ProductVariationServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java"
    sha256: "8a0956cd820940cf8e66c131119ebd203d339e317673b2eb53a6464e0a7a9de0"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java"
    sha256: "dfd2a87c5ff6194501c1f4ff065a0fa46e6b2d1f9646fa981d634cdbbb6435c5"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.variation

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java`

## Types
- `ProductVariationService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:14`
- `ProductVariationServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:22`

## Fields
- `ProductVariationServiceImpl.productVariationRepository: ProductVariationRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:28`
- `ProductVariationServiceImpl.pageableProductVariationSetRepository: PageableProductVariationRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:39`

## Functions and methods
- `ProductVariationService.saveOrUpdate(ProductVariation) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:17`
- `ProductVariationService.getById(MerchantStore, Long, Language) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:19`
- `ProductVariationService.getById(MerchantStore, Long) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:21`
- `ProductVariationService.getByCode(MerchantStore, String) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:23`
- `ProductVariationService.getByMerchant(MerchantStore, Language, String, int, int) -> Page<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:25`
- `ProductVariationService.getByIds(List<Long>, MerchantStore) -> List<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationService.java:27`
- `ProductVariationServiceImpl.getById(MerchantStore, Long, Language) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:42`
- `ProductVariationServiceImpl.getByCode(MerchantStore, String) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:47`
- `ProductVariationServiceImpl.getByMerchant(MerchantStore, Language, String, int, int) -> Page<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:54`
- `ProductVariationServiceImpl.getById(MerchantStore, Long) -> Optional<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:61`
- `ProductVariationServiceImpl.saveOrUpdate(ProductVariation) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:66`
- `ProductVariationServiceImpl.getByIds(List<Long>, MerchantStore) -> List<ProductVariation>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:82`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.variation.PageableProductVariationRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.variation.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:38`
- [com.salesmanager.core.business.repositories.catalog.product.variation.ProductVariationRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.variation.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:27`

## Calls
- `ProductVariationServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.catalog.product.variation.ProductVariationRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.variation.md) `ProductVariationRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:49`
- `ProductVariationServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.product.variation.ProductVariationRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.variation.md) `ProductVariationRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:44`
- `ProductVariationServiceImpl.getByIds` calls [com.salesmanager.core.business.repositories.catalog.product.variation.ProductVariationRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.variation.md) `ProductVariationRepository.findByIds` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:84`
- `ProductVariationServiceImpl.getByMerchant` calls [com.salesmanager.core.business.repositories.catalog.product.variation.PageableProductVariationRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.variation.md) `PageableProductVariationRepository.list` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/variation/ProductVariationServiceImpl.java:58`
