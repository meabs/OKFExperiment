---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.inventory"
description: "com.salesmanager.core.business.services.catalog.inventory: ProductInventoryServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryService.java"
    sha256: "60badbfc11836137230d0dd5f5a7cd98a3bef50642e0aacdc9cf979f0a008dae"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java"
    sha256: "a14d70bcea6a72464154a94fac33b612184e6b1afdb1cddec83f412cf2a16a9b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.inventory

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java`

## Types
- `ProductInventoryService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryService.java:8`
- `ProductInventoryServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:21`

## Fields
- `ProductInventoryServiceImpl.pricingService: PricingService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:26`

## Functions and methods
- `ProductInventoryService.inventory(Product) -> ProductInventory` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryService.java:11`
- `ProductInventoryService.inventory(ProductVariant) -> ProductInventory` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryService.java:12`
- `ProductInventoryServiceImpl.inventory(Product) -> ProductInventory` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:28`
- `ProductInventoryServiceImpl.inventory(ProductVariant) -> ProductInventory` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:40`
- `ProductInventoryServiceImpl.defaultAvailability(Set<ProductAvailability>) -> ProductAvailability` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:62`
- `ProductInventoryServiceImpl.inventory(ProductAvailability, FinalPrice) -> ProductInventory` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:77`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:25`

## Calls
- `ProductInventoryServiceImpl.inventory` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculateProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/inventory/ProductInventoryServiceImpl.java:33`
