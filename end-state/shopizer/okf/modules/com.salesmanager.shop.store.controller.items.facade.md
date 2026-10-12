---
type: Code Module
title: "com.salesmanager.shop.store.controller.items.facade"
description: "com.salesmanager.shop.store.controller.items.facade: listItemsByManufacturer, createProductGroup, listProductGroups, updateProductGroup"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java"
    sha256: "c2f9ba43c07bcf967a2fe8686c746a49d2cc01bad3c55b9f0c9177956a21b815"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.items.facade

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java`

## Types
- `ProductItemsFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:11`

## Functions and methods
- `ProductItemsFacade.listItemsByManufacturer(MerchantStore, Language, Long, int, int) -> ReadableProductList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:19`
- `ProductItemsFacade.createProductGroup(ProductGroup, MerchantStore) -> ProductGroup` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:21`
- `ProductItemsFacade.listProductGroups(MerchantStore, Language) -> List<ProductGroup>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:23`
- `ProductItemsFacade.updateProductGroup(String, ProductGroup, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:31`
- `ProductItemsFacade.listItemsByIds(MerchantStore, Language, List<Long>, int, int) -> ReadableProductList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:43`
- `ProductItemsFacade.listItemsByGroup(String, MerchantStore, Language) -> ReadableProductList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:54`
- `ProductItemsFacade.addItemToGroup(Product, String, MerchantStore, Language) -> ReadableProductList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:65`
- `ProductItemsFacade.removeItemFromGroup(Product, String, MerchantStore, Language) -> ReadableProductList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:76`
- `ProductItemsFacade.deleteGroup(String, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/items/facade/ProductItemsFacade.java:78`
