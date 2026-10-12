---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.manufacturer"
description: "com.salesmanager.core.model.catalog.product.manufacturer: Manufacturer, ManufacturerDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java"
    sha256: "7a4e398aa6193bd71c7c73440ff638efcd93a5b224ee2e5756064badb9856ed2"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java"
    sha256: "0dd14a64648c52dc5e35ead366bb0b386031920dd09128d08b4a98c97139b6d4"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.manufacturer

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java`

## Types
- `Manufacturer` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:31`
- `ManufacturerDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:17`

## Fields
- `Manufacturer.DEFAULT_MANUFACTURER: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:38`
- `Manufacturer.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:44`
- `Manufacturer.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:47`
- `Manufacturer.descriptions: Set<ManufacturerDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:50`
- `Manufacturer.image: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:53`
- `Manufacturer.order: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:56`
- `Manufacturer.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:60`
- `Manufacturer.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:64`
- `ManufacturerDescription.manufacturer: Manufacturer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:33`
- `ManufacturerDescription.url: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:36`
- `ManufacturerDescription.urlClicked: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:39`
- `ManufacturerDescription.dateLastClick: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:42`

## Functions and methods
- `Manufacturer.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:69`
- `Manufacturer.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:74`
- `Manufacturer.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:79`
- `Manufacturer.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:84`
- `Manufacturer.getImage() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:89`
- `Manufacturer.setImage(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:93`
- `Manufacturer.getDescriptions() -> Set<ManufacturerDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:97`
- `Manufacturer.setDescriptions(Set<ManufacturerDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:101`
- `Manufacturer.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:105`
- `Manufacturer.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:109`
- `Manufacturer.setOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:113`
- `Manufacturer.getOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:117`
- `Manufacturer.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:121`
- `Manufacturer.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:125`
- `ManufacturerDescription.getUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:47`
- `ManufacturerDescription.setUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:51`
- `ManufacturerDescription.getUrlClicked() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:55`
- `ManufacturerDescription.setUrlClicked(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:59`
- `ManufacturerDescription.getDateLastClick() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:63`
- `ManufacturerDescription.setDateLastClick(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:67`
- `ManufacturerDescription.getManufacturer() -> Manufacturer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:71`
- `ManufacturerDescription.setManufacturer(Manufacturer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/ManufacturerDescription.java:75`

## Depends on
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:46`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/manufacturer/Manufacturer.java:58`

## Tests
- `com.salesmanager.test.catalog.ManufacturerTest`
