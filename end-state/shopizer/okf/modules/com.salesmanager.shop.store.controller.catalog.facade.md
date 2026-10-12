---
type: Code Module
title: "com.salesmanager.shop.store.controller.catalog.facade"
description: "com.salesmanager.shop.store.controller.catalog.facade: saveCatalog, updateCatalog, deleteCatalog, uniqueCatalog"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java"
    sha256: "33342f76c84b2af4550acb6eab531381d464cf16690dbb7bdca92db7c738e546"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.catalog.facade

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java`

## Types
- `CatalogFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:11`

## Functions and methods
- `CatalogFacade.saveCatalog(PersistableCatalog, MerchantStore, Language) -> ReadableCatalog` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:13`
- `CatalogFacade.updateCatalog(Long, PersistableCatalog, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:15`
- `CatalogFacade.deleteCatalog(Long, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:17`
- `CatalogFacade.uniqueCatalog(String, MerchantStore) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:19`
- `CatalogFacade.getCatalog(String, MerchantStore, Language) -> ReadableCatalog` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:21`
- `CatalogFacade.getCatalog(String, MerchantStore) -> Catalog` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:23`
- `CatalogFacade.getCatalog(Long, MerchantStore, Language) -> ReadableCatalog` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:25`
- `CatalogFacade.getListCatalogs(Optional<String>, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableCatalog>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:27`
- `CatalogFacade.listCatalogEntry(Optional<String>, Long, MerchantStore, Language, int, int) -> ReadableEntityList<ReadableCatalogCategoryEntry>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:29`
- `CatalogFacade.getCatalogEntry(Long, MerchantStore, Language) -> ReadableCatalogCategoryEntry` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:31`
- `CatalogFacade.addCatalogEntry(PersistableCatalogCategoryEntry, MerchantStore, Language) -> ReadableCatalogCategoryEntry` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:33`
- `CatalogFacade.removeCatalogEntry(Long, Long, MerchantStore, Language) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/catalog/facade/CatalogFacade.java:35`
