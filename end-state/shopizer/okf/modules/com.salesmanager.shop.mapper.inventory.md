---
type: Code Module
title: "com.salesmanager.shop.mapper.inventory"
description: "com.salesmanager.shop.mapper.inventory: PersistableInventoryMapper, PersistableProductPriceMapper, ReadableInventoryMapper"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java"
    sha256: "1fa2779a5462cbf77f114312517ed32ed5c8c3d7d4bd96f5fbbde4e786de7e70"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java"
    sha256: "a86a1894031e77671b56f66223d60dfbfe5403de19f68105f22ad890c52efca4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java"
    sha256: "465237a271cdb1956ffe27a083e4698bd6a55bf31960626e1a43eaa62918561a"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.mapper.inventory

Source: `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java`

## Types
- `PersistableInventoryMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:40`
- `PersistableProductPriceMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:32`
- `ReadableInventoryMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:29`

## Fields
- `PersistableInventoryMapper.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:44`
- `PersistableInventoryMapper.productVariantService: ProductVariantService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:47`
- `PersistableInventoryMapper.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:50`
- `PersistableProductPriceMapper.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:36`
- `PersistableProductPriceMapper.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:39`
- `PersistableProductPriceMapper.productAvailabilityService: ProductAvailabilityService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:42`
- `ReadableInventoryMapper.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:33`
- `ReadableInventoryMapper.readableMerchantStorePopulator: ReadableMerchantStorePopulator` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:36`

## Functions and methods
- `PersistableInventoryMapper.convert(PersistableInventory, MerchantStore, Language) -> ProductAvailability` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:52`
- `PersistableInventoryMapper.merge(PersistableInventory, ProductAvailability, MerchantStore, Language) -> ProductAvailability` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:60`
- `PersistableInventoryMapper.getProductPriceDescriptions(ProductPrice, List<com.salesmanager.shop.model.catalog.product.ProductPriceDescription>) -> Set<ProductPriceDescription>` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:203`
- `PersistableInventoryMapper.getRegion(PersistableInventory) -> String` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:226`
- `PersistableInventoryMapper.getDescription(com.salesmanager.shop.model.catalog.product.ProductPriceDescription) -> ProductPriceDescription` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:230`
- `PersistableInventoryMapper.getLanguage(com.salesmanager.shop.model.catalog.product.ProductPriceDescription) -> Language` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:246`
- `PersistableProductPriceMapper.convert(PersistableProductPrice, MerchantStore, Language) -> ProductPrice` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:44`
- `PersistableProductPriceMapper.merge(PersistableProductPrice, ProductPrice, MerchantStore, Language) -> ProductPrice` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:49`
- `PersistableProductPriceMapper.getProductPriceDescriptions(ProductPrice, List<com.salesmanager.shop.model.catalog.product.ProductPriceDescription>, MerchantStore) -> Set<ProductPriceDescription>` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:152`
- `PersistableProductPriceMapper.getDescription(com.salesmanager.shop.model.catalog.product.ProductPriceDescription) -> ProductPriceDescription` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:175`
- `PersistableProductPriceMapper.getLanguage(com.salesmanager.shop.model.catalog.product.ProductPriceDescription) -> Language` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:191`
- `ReadableInventoryMapper.convert(ProductAvailability, MerchantStore, Language) -> ReadableInventory` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:38`
- `ReadableInventoryMapper.merge(ProductAvailability, ReadableInventory, MerchantStore, Language) -> ReadableInventory` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:44`
- `ReadableInventoryMapper.store(MerchantStore, Language) -> ReadableMerchantStore` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:104`
- `ReadableInventoryMapper.prices(ProductAvailability, MerchantStore, Language) -> List<ReadableProductPrice>` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:117`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:32`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:49`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:38`
- [com.salesmanager.core.business.services.catalog.product.availability.ProductAvailabilityService](/modules/com.salesmanager.core.business.services.catalog.product.availability.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:41`
- [com.salesmanager.core.business.services.catalog.product.variant.ProductVariantService](/modules/com.salesmanager.core.business.services.catalog.product.variant.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:46`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:43`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableProductPriceMapper.java:35`
- [com.salesmanager.shop.populator.store.ReadableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:35`

## Calls
- `PersistableInventoryMapper.merge` calls [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `ProductService.findOne` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/PersistableInventoryMapper.java:68`
- `ReadableInventoryMapper.merge` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculateProductPrice` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:91`
- `ReadableInventoryMapper.merge` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.formatDate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:64`
- `ReadableInventoryMapper.prices` calls [com.salesmanager.shop.populator.catalog.ReadableProductPricePopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableProductPricePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:127`
- `ReadableInventoryMapper.store` calls [com.salesmanager.shop.populator.store.ReadableMerchantStorePopulator](/modules/com.salesmanager.shop.populator.store.md) `ReadableMerchantStorePopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/mapper/inventory/ReadableInventoryMapper.java:114`
