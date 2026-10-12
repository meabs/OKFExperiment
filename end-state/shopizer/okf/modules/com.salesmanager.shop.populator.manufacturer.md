---
type: Code Module
title: "com.salesmanager.shop.populator.manufacturer"
description: "com.salesmanager.shop.populator.manufacturer: PersistableManufacturerPopulator, ReadableManufacturerPopulator"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java"
    sha256: "ff6f32af630c2fe25b58fd4393fc883e821fa288577ef82684baa67cd71d9776"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/ReadableManufacturerPopulator.java"
    sha256: "9bbfd55b00641038c908a4351cadad5dbafd4d7b074bc824e2040b8444880b1a"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.populator.manufacturer

Source: `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/ReadableManufacturerPopulator.java`

## Types
- `PersistableManufacturerPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:26`
- `ReadableManufacturerPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/ReadableManufacturerPopulator.java:14`

## Fields
- `PersistableManufacturerPopulator.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:30`

## Functions and methods
- `PersistableManufacturerPopulator.populate(PersistableManufacturer, Manufacturer, MerchantStore, Language) -> Manufacturer` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:32`
- `PersistableManufacturerPopulator.createTarget() -> Manufacturer` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:81`
- `PersistableManufacturerPopulator.setLanguageService(LanguageService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:87`
- `PersistableManufacturerPopulator.getLanguageService() -> LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:91`
- `ReadableManufacturerPopulator.populate(com.salesmanager.core.model.catalog.product.manufacturer.Manufacturer, ReadableManufacturer, MerchantStore, Language) -> ReadableManufacturer` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/ReadableManufacturerPopulator.java:19`
- `ReadableManufacturerPopulator.createTarget() -> ReadableManufacturer` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/ReadableManufacturerPopulator.java:67`
- `ReadableManufacturerPopulator.populateDescription(ManufacturerDescription) -> com.salesmanager.shop.model.catalog.manufacturer.ManufacturerDescription` `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/ReadableManufacturerPopulator.java:72`

## Depends on
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/manufacturer/PersistableManufacturerPopulator.java:30`
