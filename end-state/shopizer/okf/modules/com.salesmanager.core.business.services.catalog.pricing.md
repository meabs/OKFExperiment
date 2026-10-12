---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.pricing"
description: "com.salesmanager.core.business.services.catalog.pricing: PricingServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java"
    sha256: "ad374c101b6bb5131b304f3ae50244ecb0d776dd1f8ca91b3495adc25faddea7"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java"
    sha256: "169edc98192ce47e82c5d02d2d87f912e2b5124c1ccc96d72bc2f1cfc0a1f56b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.pricing

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java`

## Types
- `PricingService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:23`
- `PricingServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:29`

## Fields
- `PricingServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:32`
- `PricingServiceImpl.priceUtil: ProductPriceUtils` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:36`

## Functions and methods
- `PricingService.calculateProductPrice(Product) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:32`
- `PricingService.calculateProductPrice(ProductVariant) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:40`
- `PricingService.calculateProductPrice(ProductAvailability) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:48`
- `PricingService.calculateProductPrice(Product, Customer) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:59`
- `PricingService.calculateProductPrice(Product, List<ProductAttribute>) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:71`
- `PricingService.calculateProductPrice(Product, List<ProductAttribute>, Customer) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:85`
- `PricingService.getDisplayAmount(BigDecimal, MerchantStore) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:96`
- `PricingService.getDisplayAmount(BigDecimal, Locale, Currency, MerchantStore) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:108`
- `PricingService.getAmount(String) -> BigDecimal` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:118`
- `PricingService.getStringAmount(BigDecimal, MerchantStore) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:127`
- `PricingService.calculatePriceQuantity(BigDecimal, int) -> BigDecimal` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingService.java:136`
- `PricingServiceImpl.calculateProductPrice(Product) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:38`
- `PricingServiceImpl.calculateProductPrice(Product, Customer) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:43`
- `PricingServiceImpl.calculateProductPrice(Product, List<ProductAttribute>) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:49`
- `PricingServiceImpl.calculateProductPrice(Product, List<ProductAttribute>, Customer) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:54`
- `PricingServiceImpl.calculatePriceQuantity(BigDecimal, int) -> BigDecimal` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:60`
- `PricingServiceImpl.getDisplayAmount(BigDecimal, MerchantStore) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:65`
- `PricingServiceImpl.getDisplayAmount(BigDecimal, Locale, Currency, MerchantStore) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:75`
- `PricingServiceImpl.getStringAmount(BigDecimal, MerchantStore) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:86`
- `PricingServiceImpl.getAmount(String) -> BigDecimal` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:97`
- `PricingServiceImpl.calculateProductPrice(ProductAvailability) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:109`
- `PricingServiceImpl.calculateProductPrice(ProductVariant) -> FinalPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:115`

## Depends on
- [com.salesmanager.core.business.utils.ProductPriceUtils](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:35`

## Calls
- `PricingServiceImpl.getDisplayAmount` calls [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `SalesManagerEntity.toString` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/pricing/PricingServiceImpl.java:81`
