---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product"
description: "com.salesmanager.core.business.repositories.catalog.product: ProductRepositoryImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepository.java"
    sha256: "c261ae4b460b2f58187ff929b00294aa3cb9f905cf9a44c4e76930a5419faf3f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java"
    sha256: "35630e7eff920043f2487f1bcd2b6712f9f94b5c9bf04f207c1cf2c834015d51"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java"
    sha256: "9ea72b03f17a97cd4de9be4c7e74ed07fe191a3edf17ab5f516317823e344da9"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java`

## Types
- `ProductRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository`, [com.salesmanager.core.business.repositories.catalog.product.ProductRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepository.java:11`
- `ProductRepositoryCustom` (interface) `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:15`
- `ProductRepositoryImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:31`

## Fields
- `ProductRepositoryImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:33`
- `ProductRepositoryImpl.em: EntityManager` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:36`

## Functions and methods
- `ProductRepository.existsBySku(String, Integer) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepository.java:14`
- `ProductRepository.findBySku(String, Integer) -> List<Object>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepository.java:23`
- `ProductRepositoryCustom.listByStore(MerchantStore, Language, ProductCriteria) -> ProductList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:18`
- `ProductRepositoryCustom.getProductWithOnlyMerchantStoreById(Long) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:21`
- `ProductRepositoryCustom.getByFriendlyUrl(MerchantStore, String, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:23`
- `ProductRepositoryCustom.getProductsListByCategories(Set) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:25`
- `ProductRepositoryCustom.getProductsListByCategories(Set<Long>, Language) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:27`
- `ProductRepositoryCustom.getProductsListByIds(Set<Long>) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:30`
- `ProductRepositoryCustom.listByTaxClass(TaxClass) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:32`
- `ProductRepositoryCustom.listByStore(MerchantStore) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:34`
- `ProductRepositoryCustom.getProductForLocale(long, Language, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:36`
- `ProductRepositoryCustom.getById(Long) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:39`
- `ProductRepositoryCustom.getById(Long, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:40`
- `ProductRepositoryCustom.getByCode(String, Language) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:48`
- `ProductRepositoryCustom.getByCode(String, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:57`
- `ProductRepositoryCustom.getById(Long, MerchantStore, Language) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:60`
- `ProductRepositoryCustom.getProductsForLocale(MerchantStore, Set<Long>, Language, Locale) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryCustom.java:62`
- `ProductRepositoryImpl.getById(Long, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:38`
- `ProductRepositoryImpl.getById(Long) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:43`
- `ProductRepositoryImpl.getProductWithOnlyMerchantStoreById(Long) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:49`
- `ProductRepositoryImpl.get(Long, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:67`
- `ProductRepositoryImpl.getByCode(String, Language) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:112`
- `ProductRepositoryImpl.getByCode(String, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:165`
- `ProductRepositoryImpl.getByFriendlyUrl(MerchantStore, String, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:207`
- `ProductRepositoryImpl.getProductsForLocale(MerchantStore, Set<Long>, Language, Locale) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:271`
- `ProductRepositoryImpl.getProductForLocale(long, Language, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:280`
- `ProductRepositoryImpl.getProductsListByCategories(Set) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:337`
- `ProductRepositoryImpl.getProductsListByCategories(Set<Long>, Language) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:395`
- `ProductRepositoryImpl.getProductsListByIds(Set<Long>) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:458`
- `ProductRepositoryImpl.getProductsListForLocale(MerchantStore, Set, Language, Locale, int, int) -> ProductList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:479`
- `ProductRepositoryImpl.listByStore(MerchantStore, Language, ProductCriteria) -> ProductList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:577`
- `ProductRepositoryImpl.listByStore(MerchantStore) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:973`
- `ProductRepositoryImpl.listByTaxClass(TaxClass) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:1026`
- `ProductRepositoryImpl.productQueryV1() -> String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:1079`
- `ProductRepositoryImpl.productQueryV2() -> String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:1122`
- `ProductRepositoryImpl.getById(Long, MerchantStore, Language) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:1177`

## Calls
- `ProductRepositoryImpl.listByStore` calls [com.salesmanager.core.business.utils.RepositoryHelper](/modules/com.salesmanager.core.business.utils.md) `RepositoryHelper.paginateQuery` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/ProductRepositoryImpl.java:962`
