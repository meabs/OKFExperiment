---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.relationship"
description: "com.salesmanager.core.model.catalog.product.relationship: ProductRelationship"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java"
    sha256: "abc15623f4e6e31ba6ecddad73cef2bacb72dfa5929fcd21aaf374f349dcf86c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationshipType.java"
    sha256: "047f6cff56c374e0b513d972621ec831a005bf396e75a23c3ed4bd5a18456fd9"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.relationship

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationshipType.java`

## Types
- `ProductRelationship` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:19`
- `ProductRelationshipType` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationshipType.java:3`

## Fields
- `ProductRelationship.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:28`
- `ProductRelationship.store: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:32`
- `ProductRelationship.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:36`
- `ProductRelationship.relatedProduct: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:40`
- `ProductRelationship.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:43`
- `ProductRelationship.active: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:46`

## Functions and methods
- `ProductRelationship.getProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:48`
- `ProductRelationship.setProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:54`
- `ProductRelationship.getRelatedProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:60`
- `ProductRelationship.setRelatedProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:66`
- `ProductRelationship.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:72`
- `ProductRelationship.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:78`
- `ProductRelationship.isActive() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:84`
- `ProductRelationship.setActive(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:90`
- `ProductRelationship.getStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:101`
- `ProductRelationship.setStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:105`
- `ProductRelationship.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:109`
- `ProductRelationship.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:113`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:34`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/relationship/ProductRelationship.java:30`
