---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.catalog"
description: "com.salesmanager.core.business.services.catalog.catalog: CatalogEntryServiceImpl, CatalogServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java"
    sha256: "0d8bfe324dc3e8cbb21f07b4ac4426b14c5030529c86b9528583715ba00e52dd"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java"
    sha256: "341ca8e8e0723c3c33721728129a81c7aac146a6338ec32590dc54e2b945cb5b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java"
    sha256: "0ac796aa421efba30fc3323ad2fed162c2c1273fae32a1cca97ff67348f03299"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java"
    sha256: "c953ca7e825b40efa7ac67a6d5053db184a721161e2c3824e04b1262dd8de2a1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.catalog

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java`

## Types
- `CatalogEntryService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java:12`
- `CatalogEntryServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:20`
- `CatalogService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:13`
- `CatalogServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:22`

## Fields
- `CatalogEntryServiceImpl.pageableCatalogEntryRepository: PageableCatalogEntryRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:25`
- `CatalogEntryServiceImpl.catalogEntryRepository: CatalogEntryRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:27`
- `CatalogServiceImpl.catalogRepository: CatalogRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:28`
- `CatalogServiceImpl.pageableCatalogRepository: PageableCatalogRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:31`

## Functions and methods
- `CatalogEntryService.add(CatalogCategoryEntry, Catalog) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java:15`
- `CatalogEntryService.remove(CatalogCategoryEntry) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java:17`
- `CatalogEntryService.list(Catalog, MerchantStore, Language, String, int, int) -> Page<CatalogCategoryEntry>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryService.java:19`
- `CatalogEntryServiceImpl.add(CatalogCategoryEntry, Catalog) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:35`
- `CatalogEntryServiceImpl.list(Catalog, MerchantStore, Language, String, int, int) -> Page<CatalogCategoryEntry>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:42`
- `CatalogEntryServiceImpl.remove(CatalogCategoryEntry) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:50`
- `CatalogService.saveOrUpdate(Catalog, MerchantStore) -> Catalog` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:22`
- `CatalogService.getById(Long, MerchantStore) -> Optional<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:24`
- `CatalogService.getByCode(String, MerchantStore) -> Optional<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:26`
- `CatalogService.getCatalogs(MerchantStore, Language, String, int, int) -> Page<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:34`
- `CatalogService.delete(Catalog) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:39`
- `CatalogService.existByCode(String, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogService.java:41`
- `CatalogServiceImpl.saveOrUpdate(Catalog, MerchantStore) -> Catalog` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:39`
- `CatalogServiceImpl.getCatalogs(MerchantStore, Language, String, int, int) -> Page<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:45`
- `CatalogServiceImpl.delete(Catalog) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:51`
- `CatalogServiceImpl.getById(Long, MerchantStore) -> Optional<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:57`
- `CatalogServiceImpl.getByCode(String, MerchantStore) -> Optional<Catalog>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:62`
- `CatalogServiceImpl.existByCode(String, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:67`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.catalog.CatalogEntryRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:27`
- [com.salesmanager.core.business.repositories.catalog.catalog.CatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:28`
- [com.salesmanager.core.business.repositories.catalog.catalog.PageableCatalogEntryRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:24`
- [com.salesmanager.core.business.repositories.catalog.catalog.PageableCatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:30`

## Calls
- `CatalogEntryServiceImpl.add` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogEntryRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogEntryRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:38`
- `CatalogEntryServiceImpl.list` calls [com.salesmanager.core.business.repositories.catalog.catalog.PageableCatalogEntryRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `PageableCatalogEntryRepository.listByCatalog` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:46`
- `CatalogEntryServiceImpl.remove` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogEntryRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogEntryRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogEntryServiceImpl.java:52`
- `CatalogServiceImpl.delete` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:54`
- `CatalogServiceImpl.existByCode` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogRepository.existsByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:69`
- `CatalogServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:64`
- `CatalogServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogRepository.findById` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:59`
- `CatalogServiceImpl.getCatalogs` calls [com.salesmanager.core.business.repositories.catalog.catalog.PageableCatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `PageableCatalogRepository.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:48`
- `CatalogServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.repositories.catalog.catalog.CatalogRepository](/modules/com.salesmanager.core.business.repositories.catalog.catalog.md) `CatalogRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/catalog/CatalogServiceImpl.java:41`
