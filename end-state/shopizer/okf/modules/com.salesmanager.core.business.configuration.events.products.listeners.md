---
type: Code Module
title: "com.salesmanager.core.business.configuration.events.products.listeners"
description: "com.salesmanager.core.business.configuration.events.products.listeners: IndexProductEventListener"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java"
    sha256: "44a6e8c04674a34858d6e6b15206c1c28f137ade89f67a49610094ba437f0e33"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.configuration.events.products.listeners

Source: `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java`

## Types
- `IndexProductEventListener` (class) `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:39`

## Fields
- `IndexProductEventListener.searchService: SearchService` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:43`
- `IndexProductEventListener.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:46`
- `IndexProductEventListener.noIndex: boolean` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:49`

## Functions and methods
- `IndexProductEventListener.onApplicationEvent(ProductEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:54`
- `IndexProductEventListener.productOfEvent(ProductEvent) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:98`
- `IndexProductEventListener.saveProduct(SaveProductEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:124`
- `IndexProductEventListener.deleteProduct(DeleteProductEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:136`
- `IndexProductEventListener.saveProductVariant(SaveProductVariantEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:148`
- `IndexProductEventListener.deleteProductVariant(DeleteProductVariantEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:176`
- `IndexProductEventListener.saveProductImage(SaveProductImageEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:203`
- `IndexProductEventListener.deleteProductImage(DeleteProductImageEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:232`
- `IndexProductEventListener.saveProductAttribute(SaveProductAttributeEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:261`
- `IndexProductEventListener.deleteProductAttribute(DeleteProductAttributeEvent) -> void` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:289`

## Depends on
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:45`
- [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:42`

## Calls
- `IndexProductEventListener.deleteProduct` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.deleteDocument` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:142`
- `IndexProductEventListener.deleteProductAttribute` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:306`
- `IndexProductEventListener.deleteProductVariant` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:195`
- `IndexProductEventListener.productOfEvent` calls [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `ProductService.findOne` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:108`
- `IndexProductEventListener.saveProduct` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:130`
- `IndexProductEventListener.saveProductAttribute` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:282`
- `IndexProductEventListener.saveProductImage` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:225`
- `IndexProductEventListener.saveProductVariant` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-core/src/main/java/com/salesmanager/core/business/configuration/events/products/listeners/IndexProductEventListener.java:169`
