---
type: Code Module
title: "com.salesmanager.shop.store.facade.manufacturer"
description: "com.salesmanager.shop.store.facade.manufacturer: ManufacturerFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java"
    sha256: "64ee0aca7024dcce652769193994761e4783a1207ea3387d73c90b673cfd6949"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.manufacturer

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java`

## Types
- `ManufacturerFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:32`

## Fields
- `ManufacturerFacadeImpl.readableManufacturerConverter: Mapper<Manufacturer, ReadableManufacturer>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:36`
- `ManufacturerFacadeImpl.manufacturerService: ManufacturerService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:40`
- `ManufacturerFacadeImpl.categoryService: CategoryService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:43`
- `ManufacturerFacadeImpl.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:46`

## Functions and methods
- `ManufacturerFacadeImpl.getByProductInCategory(MerchantStore, Language, Long) -> List<ReadableManufacturer>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:48`
- `ManufacturerFacadeImpl.saveOrUpdateManufacturer(PersistableManufacturer, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:85`
- `ManufacturerFacadeImpl.deleteManufacturer(Manufacturer, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:114`
- `ManufacturerFacadeImpl.getManufacturer(Long, MerchantStore, Language) -> ReadableManufacturer` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:121`
- `ManufacturerFacadeImpl.getAllManufacturers(MerchantStore, Language, ListCriteria, int, int) -> ReadableManufacturerList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:145`
- `ManufacturerFacadeImpl.manufacturerExist(MerchantStore, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:199`
- `ManufacturerFacadeImpl.listByStore(MerchantStore, Language, ListCriteria, int, int) -> ReadableManufacturerList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:211`

## Depends on
- [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:42`
- [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:39`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:45`
- [com.salesmanager.core.model.catalog.product.manufacturer.Manufacturer](/modules/com.salesmanager.core.model.catalog.product.manufacturer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:35`
- [com.salesmanager.shop.mapper.Mapper](/modules/com.salesmanager.shop.mapper.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:35`
- [com.salesmanager.shop.model.catalog.manufacturer.ReadableManufacturer](/modules/com.salesmanager.shop.model.catalog.manufacturer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:35`

## Calls
- `ManufacturerFacadeImpl.deleteManufacturer` calls [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `ManufacturerService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:117`
- `ManufacturerFacadeImpl.getAllManufacturers` calls [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `ManufacturerService.count`, `ManufacturerService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:157`
- `ManufacturerFacadeImpl.getAllManufacturers` calls [com.salesmanager.shop.populator.manufacturer.ReadableManufacturerPopulator](/modules/com.salesmanager.shop.populator.manufacturer.md) `ReadableManufacturerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:186`
- `ManufacturerFacadeImpl.getByProductInCategory` calls [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `ManufacturerService.listByProductsInCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:66`
- `ManufacturerFacadeImpl.getByProductInCategory` calls [com.salesmanager.shop.mapper.Mapper](/modules/com.salesmanager.shop.mapper.md) `Mapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:75`
- `ManufacturerFacadeImpl.getManufacturer` calls [com.salesmanager.shop.populator.manufacturer.ReadableManufacturerPopulator](/modules/com.salesmanager.shop.populator.manufacturer.md) `ReadableManufacturerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:139`
- `ManufacturerFacadeImpl.listByStore` calls [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `ManufacturerService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:226`
- `ManufacturerFacadeImpl.listByStore` calls [com.salesmanager.shop.populator.manufacturer.ReadableManufacturerPopulator](/modules/com.salesmanager.shop.populator.manufacturer.md) `ReadableManufacturerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:243`
- `ManufacturerFacadeImpl.saveOrUpdateManufacturer` calls [com.salesmanager.core.business.services.catalog.product.manufacturer.ManufacturerService](/modules/com.salesmanager.core.business.services.catalog.product.manufacturer.md) `ManufacturerService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:108`
- `ManufacturerFacadeImpl.saveOrUpdateManufacturer` calls [com.salesmanager.shop.populator.manufacturer.PersistableManufacturerPopulator](/modules/com.salesmanager.shop.populator.manufacturer.md) `PersistableManufacturerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/manufacturer/ManufacturerFacadeImpl.java:106`
