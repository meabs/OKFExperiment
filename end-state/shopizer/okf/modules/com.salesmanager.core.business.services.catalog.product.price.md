---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.price"
description: "com.salesmanager.core.business.services.catalog.product.price: ProductPriceServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java"
    sha256: "58370a445adac1c2a94d78fce241d5d42008eaf3fe6ec003c6f1437ccc88e09e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java"
    sha256: "9132273405a693d1e4d33da27bf51f174b4d1551f2387bf8f7499b5f059643d9"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.price

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java`

## Types
- `ProductPriceService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java:11`
- `ProductPriceServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:18`

## Fields
- `ProductPriceServiceImpl.productPriceRepository: ProductPriceRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:22`

## Functions and methods
- `ProductPriceService.addDescription(ProductPrice, ProductPriceDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java:13`
- `ProductPriceService.saveOrUpdate(ProductPrice) -> ProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java:15`
- `ProductPriceService.findByProductSku(String, MerchantStore) -> List<ProductPrice>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java:17`
- `ProductPriceService.findById(Long, String, MerchantStore) -> ProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java:19`
- `ProductPriceService.findByInventoryId(Long, String, MerchantStore) -> List<ProductPrice>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceService.java:21`
- `ProductPriceServiceImpl.addDescription(ProductPrice, ProductPriceDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:30`
- `ProductPriceServiceImpl.saveOrUpdate(ProductPrice) -> ProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:38`
- `ProductPriceServiceImpl.delete(ProductPrice) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:49`
- `ProductPriceServiceImpl.findByProductSku(String, MerchantStore) -> List<ProductPrice>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:58`
- `ProductPriceServiceImpl.findById(Long, String, MerchantStore) -> ProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:64`
- `ProductPriceServiceImpl.findByInventoryId(Long, String, MerchantStore) -> List<ProductPrice>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:70`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.price.ProductPriceRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.price.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:22`

## Calls
- `ProductPriceServiceImpl.findById` calls [com.salesmanager.core.business.repositories.catalog.product.price.ProductPriceRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.price.md) `ProductPriceRepository.findByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:67`
- `ProductPriceServiceImpl.findByInventoryId` calls [com.salesmanager.core.business.repositories.catalog.product.price.ProductPriceRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.price.md) `ProductPriceRepository.findByProductInventoty` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:73`
- `ProductPriceServiceImpl.findByProductSku` calls [com.salesmanager.core.business.repositories.catalog.product.price.ProductPriceRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.price.md) `ProductPriceRepository.findByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:61`
- `ProductPriceServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.repositories.catalog.product.price.ProductPriceRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.price.md) `ProductPriceRepository.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/price/ProductPriceServiceImpl.java:42`
