---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.manufacturer"
description: "com.salesmanager.core.business.services.catalog.product.manufacturer: ManufacturerServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java"
    sha256: "38bf01856b3764def0855a06d54cd3ffff05a118fb13f5d8990efd87396c92b5"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java"
    sha256: "1715255f9f5ed0ef3fed850b88f74f56b44c74c21d485e9e4b8ed3da51fecc63"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.manufacturer

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java`

## Types
- `ManufacturerService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:13`
- `ManufacturerServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:27`

## Fields
- `ManufacturerServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:31`
- `ManufacturerServiceImpl.pageableManufacturerRepository: PageableManufacturerRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:34`
- `ManufacturerServiceImpl.manufacturerRepository: ManufacturerRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:36`

## Functions and methods
- `ManufacturerService.listByStore(MerchantStore, Language) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:15`
- `ManufacturerService.listByStore(MerchantStore) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:18`
- `ManufacturerService.listByStore(MerchantStore, Language, int, int) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:20`
- `ManufacturerService.listByStore(MerchantStore, Language, String, int, int) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:22`
- `ManufacturerService.saveOrUpdate(Manufacturer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:24`
- `ManufacturerService.addManufacturerDescription(Manufacturer, ManufacturerDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:26`
- `ManufacturerService.getCountManufAttachedProducts(Manufacturer) -> Long` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:28`
- `ManufacturerService.delete(Manufacturer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:30`
- `ManufacturerService.getByCode(MerchantStore, String) -> Manufacturer` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:32`
- `ManufacturerService.listByProductsByCategoriesId(MerchantStore, List<Long>, Language) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:42`
- `ManufacturerService.listByProductsInCategory(MerchantStore, Category, Language) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:53`
- `ManufacturerService.listByStore(MerchantStore, String, int, int) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:56`
- `ManufacturerService.count(MerchantStore) -> int` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerService.java:59`
- `ManufacturerServiceImpl.delete(Manufacturer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:44`
- `ManufacturerServiceImpl.getCountManufAttachedProducts(Manufacturer) -> Long` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:50`
- `ManufacturerServiceImpl.listByStore(MerchantStore, Language) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:57`
- `ManufacturerServiceImpl.listByStore(MerchantStore) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:63`
- `ManufacturerServiceImpl.listByProductsByCategoriesId(MerchantStore, List<Long>, Language) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:68`
- `ManufacturerServiceImpl.addManufacturerDescription(Manufacturer, ManufacturerDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:74`
- `ManufacturerServiceImpl.saveOrUpdate(Manufacturer) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:88`
- `ManufacturerServiceImpl.getByCode(com.salesmanager.core.model.merchant.MerchantStore, String) -> Manufacturer` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:102`
- `ManufacturerServiceImpl.getById(Long) -> Manufacturer` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:108`
- `ManufacturerServiceImpl.listByProductsInCategory(MerchantStore, Category, Language) -> List<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:113`
- `ManufacturerServiceImpl.listByStore(MerchantStore, Language, int, int) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:122`
- `ManufacturerServiceImpl.count(MerchantStore) -> int` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:130`
- `ManufacturerServiceImpl.listByStore(MerchantStore, Language, String, int, int) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:136`
- `ManufacturerServiceImpl.listByStore(MerchantStore, String, int, int) -> Page<Manufacturer>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:144`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:36`
- [com.salesmanager.core.business.repositories.catalog.product.manufacturer.PageableManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:33`

## Calls
- `ManufacturerServiceImpl.count` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.count` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:133`
- `ManufacturerServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.findByCodeAndMerchandStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:105`
- `ManufacturerServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:110`
- `ManufacturerServiceImpl.getCountManufAttachedProducts` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.countByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:52`
- `ManufacturerServiceImpl.listByProductsByCategoriesId` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.findByCategoriesAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:71`
- `ManufacturerServiceImpl.listByProductsInCategory` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.findByProductInCategoryId` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:119`
- `ManufacturerServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.ManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `ManufacturerRepository.findByStore`, `ManufacturerRepository.findByStoreAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:65`
- `ManufacturerServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.catalog.product.manufacturer.PageableManufacturerRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.manufacturer.md) `PageableManufacturerRepository.findByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/manufacturer/ManufacturerServiceImpl.java:127`
