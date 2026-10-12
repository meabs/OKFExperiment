---
type: Code Module
title: "com.salesmanager.core.model.catalog.catalog"
description: "com.salesmanager.core.model.catalog.catalog: Catalog, CatalogCategoryEntry"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java"
    sha256: "a87c7fddb132a7f21456109dca634fddac9308656d0d69c01340c77cc5441296"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java"
    sha256: "2434d1d78fb4f0e7a599e40b03d8f497ca8f0e29896b01cb4583d85073947e16"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.catalog

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java`

## Types
- `Catalog` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:47`
- `CatalogCategoryEntry` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:22`

## Fields
- `Catalog.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:65`
- `Catalog.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:68`
- `Catalog.entry: Set<CatalogCategoryEntry>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:72`
- `Catalog.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:76`
- `Catalog.visible: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:80`
- `Catalog.defaultCatalog: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:83`
- `Catalog.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:87`
- `Catalog.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:90`
- `CatalogCategoryEntry.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:30`
- `CatalogCategoryEntry.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:48`
- `CatalogCategoryEntry.category: Category` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:52`
- `CatalogCategoryEntry.catalog: Catalog` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:56`
- `CatalogCategoryEntry.visible: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:61`

## Functions and methods
- `Catalog.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:92`
- `Catalog.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:96`
- `Catalog.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:108`
- `Catalog.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:113`
- `Catalog.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:118`
- `Catalog.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:123`
- `Catalog.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:129`
- `Catalog.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:133`
- `Catalog.isVisible() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:137`
- `Catalog.setVisible(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:141`
- `Catalog.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:145`
- `Catalog.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:149`
- `Catalog.getEntry() -> Set<CatalogCategoryEntry>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:153`
- `Catalog.setEntry(Set<CatalogCategoryEntry>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:157`
- `Catalog.isDefaultCatalog() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:161`
- `Catalog.setDefaultCatalog(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:165`
- `CatalogCategoryEntry.getCategory() -> Category` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:63`
- `CatalogCategoryEntry.setCategory(Category) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:67`
- `CatalogCategoryEntry.getCatalog() -> Catalog` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:71`
- `CatalogCategoryEntry.setCatalog(Catalog) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:75`
- `CatalogCategoryEntry.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:79`
- `CatalogCategoryEntry.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:83`
- `CatalogCategoryEntry.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:89`
- `CatalogCategoryEntry.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:94`
- `CatalogCategoryEntry.isVisible() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:100`
- `CatalogCategoryEntry.setVisible(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:104`

## Depends on
- [com.salesmanager.core.model.catalog.category.Category](/modules/com.salesmanager.core.model.catalog.category.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:50`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:67`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/CatalogCategoryEntry.java:29`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/catalog/Catalog.java:74`
