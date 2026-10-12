---
type: Code Module
title: "com.salesmanager.shop.store.facade.catalog"
description: "com.salesmanager.shop.store.facade.catalog: CatalogFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java"
    sha256: "c59d8c0e3056187952694966f66b189ab46cc0592a7aad4d8f6b5970824fa36b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.catalog

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java`

## Types
- `CatalogFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:35`

## Fields
- `CatalogFacadeImpl.catalogService: CatalogService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:40`
- `CatalogFacadeImpl.catalogEntryService: CatalogEntryService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:43`
- `CatalogFacadeImpl.persistableCatalogMapper: PersistableCatalogMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:46`
- `CatalogFacadeImpl.readableCatalogMapper: ReadableCatalogMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:49`
- `CatalogFacadeImpl.persistableCatalogEntryMapper: Mapper<PersistableCatalogCategoryEntry, CatalogCategoryEntry>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:52`
- `CatalogFacadeImpl.readableCatalogEntryMapper: ReadableCatalogCategoryEntryMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:55`

## Functions and methods
- `CatalogFacadeImpl.saveCatalog(PersistableCatalog, MerchantStore, Language) -> ReadableCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:58`
- `CatalogFacadeImpl.deleteCatalog(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:74`
- `CatalogFacadeImpl.getCatalog(String, MerchantStore, Language) -> ReadableCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:98`
- `CatalogFacadeImpl.updateCatalog(Long, PersistableCatalog, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:109`
- `CatalogFacadeImpl.getCatalog(Long, MerchantStore, Language) -> ReadableCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:129`
- `CatalogFacadeImpl.getCatalog(String, MerchantStore) -> Catalog` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:139`
- `CatalogFacadeImpl.getListCatalogs(Optional<String>, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableCatalog>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:147`
- `CatalogFacadeImpl.listCatalogEntry(Optional<String>, Long, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableCatalogCategoryEntry>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:163`
- `CatalogFacadeImpl.getCatalogEntry(Long, MerchantStore, Language) -> ReadableCatalogCategoryEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:183`
- `CatalogFacadeImpl.addCatalogEntry(PersistableCatalogCategoryEntry, MerchantStore, Language) -> ReadableCatalogCategoryEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:196`
- `CatalogFacadeImpl.removeCatalogEntry(Long, Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:212`
- `CatalogFacadeImpl.uniqueCatalog(String, MerchantStore) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:235`

## Depends on
- [com.salesmanager.core.business.services.catalog.catalog.CatalogEntryService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:42`
- [com.salesmanager.core.business.services.catalog.catalog.CatalogService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:39`
- [com.salesmanager.core.model.catalog.catalog.CatalogCategoryEntry](/modules/com.salesmanager.core.model.catalog.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:51`
- [com.salesmanager.shop.mapper.Mapper](/modules/com.salesmanager.shop.mapper.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:51`
- [com.salesmanager.shop.mapper.catalog.PersistableCatalogMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:45`
- [com.salesmanager.shop.mapper.catalog.ReadableCatalogCategoryEntryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:54`
- [com.salesmanager.shop.mapper.catalog.ReadableCatalogMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:48`
- [com.salesmanager.shop.model.catalog.catalog.PersistableCatalogCategoryEntry](/modules/com.salesmanager.shop.model.catalog.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:51`

## Calls
- `CatalogFacadeImpl.addCatalogEntry` calls [com.salesmanager.core.business.services.catalog.catalog.CatalogEntryService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `CatalogEntryService.add` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:207`
- `CatalogFacadeImpl.addCatalogEntry` calls [com.salesmanager.shop.mapper.Mapper](/modules/com.salesmanager.shop.mapper.md) `Mapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:206`
- `CatalogFacadeImpl.addCatalogEntry` calls [com.salesmanager.shop.mapper.catalog.ReadableCatalogCategoryEntryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCatalogCategoryEntryMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:208`
- `CatalogFacadeImpl.deleteCatalog` calls [com.salesmanager.core.business.services.catalog.catalog.CatalogService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `CatalogService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:91`
- `CatalogFacadeImpl.getCatalog` calls [com.salesmanager.shop.mapper.catalog.ReadableCatalogMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCatalogMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:106`
- `CatalogFacadeImpl.getCatalogEntry` calls [com.salesmanager.shop.mapper.catalog.ReadableCatalogCategoryEntryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCatalogCategoryEntryMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:193`
- `CatalogFacadeImpl.getListCatalogs` calls [com.salesmanager.shop.mapper.catalog.ReadableCatalogMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCatalogMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:158`
- `CatalogFacadeImpl.listCatalogEntry` calls [com.salesmanager.core.business.services.catalog.catalog.CatalogEntryService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `CatalogEntryService.list` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:171`
- `CatalogFacadeImpl.listCatalogEntry` calls [com.salesmanager.shop.mapper.catalog.ReadableCatalogCategoryEntryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCatalogCategoryEntryMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:178`
- `CatalogFacadeImpl.removeCatalogEntry` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:228`
- `CatalogFacadeImpl.saveCatalog` calls [com.salesmanager.core.business.services.catalog.catalog.CatalogService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `CatalogService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:69`
- `CatalogFacadeImpl.saveCatalog` calls [com.salesmanager.shop.mapper.catalog.PersistableCatalogMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `PersistableCatalogMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:63`
- `CatalogFacadeImpl.saveCatalog` calls [com.salesmanager.shop.mapper.catalog.ReadableCatalogMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCatalogMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:71`
- `CatalogFacadeImpl.uniqueCatalog` calls [com.salesmanager.core.business.services.catalog.catalog.CatalogService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `CatalogService.existByCode` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:237`
- `CatalogFacadeImpl.updateCatalog` calls [com.salesmanager.core.business.services.catalog.catalog.CatalogService](/modules/com.salesmanager.core.business.services.catalog.catalog.md) `CatalogService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/catalog/CatalogFacadeImpl.java:126`
