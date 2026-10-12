---
type: Code Module
title: "com.salesmanager.core.model.catalog.marketplace"
description: "com.salesmanager.core.model.catalog.marketplace: Catalog, CatalogDescription, MarketPlace"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java"
    sha256: "1df53f8a33f2737ffaf6f7fe5d01d900f71358e7a05bf96a2f2cde2706bc03fb"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java"
    sha256: "0e0812e41913451095cac0e6965c5dd6529222e0510c67b8c2fcd665fa9e89be"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java"
    sha256: "83cd65081b3ed19b85934a2442edf22319426ce8dec9a4f0a2de6b51cc4e3a66"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.marketplace

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java`

## Types
- `Catalog` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:19`
- `CatalogDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java:16`
- `MarketPlace` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:25`

## Fields
- `Catalog.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:26`
- `Catalog.store: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:28`
- `Catalog.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:30`
- `Catalog.descriptions: List<CatalogDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:32`
- `Catalog.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:35`
- `CatalogDescription.catalog: Catalog` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java:26`
- `MarketPlace.store: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:33`
- `MarketPlace.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:35`
- `MarketPlace.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:37`
- `MarketPlace.catalogs: Set<Catalog>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:39`
- `MarketPlace.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:42`

## Functions and methods
- `Catalog.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:37`
- `Catalog.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:42`
- `Catalog.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:48`
- `Catalog.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:53`
- `Catalog.getStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:58`
- `Catalog.setStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:62`
- `Catalog.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:66`
- `Catalog.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:70`
- `Catalog.getDescriptions() -> List<CatalogDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:74`
- `Catalog.setDescriptions(List<CatalogDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:78`
- `CatalogDescription.getCatalog() -> Catalog` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java:39`
- `CatalogDescription.setCatalog(Catalog) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java:43`
- `MarketPlace.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:44`
- `MarketPlace.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:49`
- `MarketPlace.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:54`
- `MarketPlace.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:59`
- `MarketPlace.getStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:64`
- `MarketPlace.setStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:68`
- `MarketPlace.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:74`
- `MarketPlace.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:78`

## Depends on
- [com.salesmanager.core.model.catalog.catalog.Catalog](/modules/com.salesmanager.core.model.catalog.catalog.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:39`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:34`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:41`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/Catalog.java:28`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/MarketPlace.java:33`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/marketplace/CatalogDescription.java:33`
