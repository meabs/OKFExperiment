---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.catalog"
description: "com.salesmanager.shop.store.api.v1.catalog: CatalogApi; 9 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java"
    sha256: "c9717e480b2a720f0e43afda664419d54b927d7590d36748736800b51f69607f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.catalog

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java`

## Types
- `CatalogApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:27`

## Fields
- `CatalogApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:35`
- `CatalogApi.catalogFacade: CatalogFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:38`

## Functions and methods
- `CatalogApi.getCatalogs(MerchantStore, Language, Optional<String>, Integer, Integer) -> ReadableEntityList<ReadableCatalog>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:41`
- `CatalogApi.exists(String, MerchantStore, Language) -> ResponseEntity<EntityExists>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:59`
- `CatalogApi.createCatalog(PersistableCatalog, MerchantStore, Language) -> ReadableCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:76`
- `CatalogApi.updateCatalog(Long, PersistableCatalog, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:91`
- `CatalogApi.getCatalog(Long, MerchantStore, Language) -> ReadableCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:108`
- `CatalogApi.deleteCatalog(Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:125`
- `CatalogApi.addCatalogEntry(Long, PersistableCatalogCategoryEntry, MerchantStore, Language) -> ReadableCatalogCategoryEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:139`
- `CatalogApi.removeCatalogEntry(Long, Long, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:165`
- `CatalogApi.getCatalogEntry(Long, MerchantStore, Language, Integer, Integer, HttpServletRequest) -> ReadableEntityList<ReadableCatalogCategoryEntry>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:184`
- `CatalogApi.catalogFilter(HttpServletRequest) -> Optional<String>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:204`
- `CatalogApi.catalogEntryFilter(HttpServletRequest) -> Optional<String>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:209`

## HTTP routes
- `POST /api/v1/private/catalog` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#createCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:76`
- `GET /api/v1/private/catalog/unique` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#exists` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:59`
- `DELETE /api/v1/private/catalog/{id}` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#deleteCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:125`
- `GET /api/v1/private/catalog/{id}` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#getCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:108`
- `PATCH /api/v1/private/catalog/{id}` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#updateCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:91`
- `POST /api/v1/private/catalog/{id}` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#addCatalogEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:139`
- `GET /api/v1/private/catalog/{id}/entry` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#getCatalogEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:184`
- `DELETE /api/v1/private/catalog/{id}/entry/{entryId}` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#removeCatalogEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:165`
- `GET /api/v1/private/catalogs` handled by `com.salesmanager.shop.store.api.v1.catalog.CatalogApi#getCatalogs` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:41`

## Depends on
- [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:37`

## Calls
- `CatalogApi.addCatalogEntry` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.addCatalogEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:160`
- `CatalogApi.createCatalog` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.saveCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:87`
- `CatalogApi.deleteCatalog` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.deleteCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:136`
- `CatalogApi.exists` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.uniqueCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:71`
- `CatalogApi.getCatalogEntry` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.listCatalogEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:199`
- `CatalogApi.removeCatalogEntry` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.removeCatalogEntry` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:178`
- `CatalogApi.updateCatalog` calls [com.salesmanager.shop.store.controller.catalog.facade.CatalogFacade](/modules/com.salesmanager.shop.store.controller.catalog.facade.md) `CatalogFacade.updateCatalog` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/catalog/CatalogApi.java:104`
