---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.type"
description: "com.salesmanager.core.business.services.catalog.product.type: ProductTypeServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java"
    sha256: "70b5689255ea2efca68084c8f46c447f30b3530013214dfda54f14f2710c8cc6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java"
    sha256: "bb8ce1a622d0a74864a2eafd67077fc617107af754781800abbae14e22e89a94"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.type

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java`

## Types
- `ProductTypeService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:13`
- `ProductTypeServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:21`

## Fields
- `ProductTypeServiceImpl.productTypeRepository: ProductTypeRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:25`
- `ProductTypeServiceImpl.pageableProductTypeRepository: PageableProductTypeRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:28`

## Functions and methods
- `ProductTypeService.getProductType(String) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:15`
- `ProductTypeService.getByMerchant(MerchantStore, Language, int, int) -> Page<ProductType>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:16`
- `ProductTypeService.getByCode(String, MerchantStore, Language) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:17`
- `ProductTypeService.getById(Long, MerchantStore, Language) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:18`
- `ProductTypeService.getById(Long, MerchantStore) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:19`
- `ProductTypeService.update(String, MerchantStore, ProductType) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:20`
- `ProductTypeService.saveOrUpdate(ProductType) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:21`
- `ProductTypeService.listProductTypes(List<Long>, MerchantStore, Language) -> List<ProductType>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeService.java:22`
- `ProductTypeServiceImpl.getByCode(String, MerchantStore, Language) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:36`
- `ProductTypeServiceImpl.update(String, MerchantStore, ProductType) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:41`
- `ProductTypeServiceImpl.getProductType(String) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:47`
- `ProductTypeServiceImpl.getByMerchant(MerchantStore, Language, int, int) -> Page<ProductType>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:52`
- `ProductTypeServiceImpl.getById(Long, MerchantStore, Language) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:58`
- `ProductTypeServiceImpl.saveOrUpdate(ProductType) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:63`
- `ProductTypeServiceImpl.listProductTypes(List<Long>, MerchantStore, Language) -> List<ProductType>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:74`
- `ProductTypeServiceImpl.getById(Long, MerchantStore) -> ProductType` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:80`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.type.PageableProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:27`
- [com.salesmanager.core.business.repositories.catalog.product.type.ProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:25`

## Calls
- `ProductTypeServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.catalog.product.type.ProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `ProductTypeRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:38`
- `ProductTypeServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.product.type.ProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `ProductTypeRepository.findById` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:60`
- `ProductTypeServiceImpl.getByMerchant` calls [com.salesmanager.core.business.repositories.catalog.product.type.PageableProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `PageableProductTypeRepository.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:55`
- `ProductTypeServiceImpl.getProductType` calls [com.salesmanager.core.business.repositories.catalog.product.type.ProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `ProductTypeRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:49`
- `ProductTypeServiceImpl.listProductTypes` calls [com.salesmanager.core.business.repositories.catalog.product.type.ProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `ProductTypeRepository.findByIds` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:77`
- `ProductTypeServiceImpl.update` calls [com.salesmanager.core.business.repositories.catalog.product.type.ProductTypeRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.type.md) `ProductTypeRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/type/ProductTypeServiceImpl.java:43`
