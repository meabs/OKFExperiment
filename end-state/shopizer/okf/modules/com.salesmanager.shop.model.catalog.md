---
type: Code Module
title: "com.salesmanager.shop.model.catalog"
description: "com.salesmanager.shop.model.catalog: NamedEntity, ProductList, SearchProductList, SearchProductRequest"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java"
    sha256: "ff94cff40aef6fa9a7d55afb217a22f0e3b0982bcb3f6ace7c3fb84a1627c063"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java"
    sha256: "9d26c8281ba0dbf8d56666d62c95dc6fc893d604676141bd2abc3b905909ed4b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java"
    sha256: "2ab78cc95d04d498331b76ed08ddd121f9a3727771f8976119639555a5b586f7"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java"
    sha256: "c4bb47041b1a5c55afe420c9f75a5a01eb4b2800f4b5f931bea8b2aea28b02a2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java`

## Types
- `NamedEntity` (class) extends [com.salesmanager.shop.model.entity.ShopEntity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:8`
- `ProductList` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:10`
- `SearchProductList` (class) extends [com.salesmanager.shop.model.catalog.ProductList](/modules/com.salesmanager.shop.model.catalog.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java:14`
- `SearchProductRequest` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:12`

## Fields
- `NamedEntity.name: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:14`
- `NamedEntity.description: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:15`
- `NamedEntity.friendlyUrl: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:16`
- `NamedEntity.keyWords: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:17`
- `NamedEntity.highlights: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:18`
- `NamedEntity.metaDescription: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:19`
- `NamedEntity.title: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:20`
- `ProductList.productCount: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:17`
- `ProductList.minPrice: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:18`
- `ProductList.maxPrice: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:19`
- `ProductList.products: List<ReadableProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:20`
- `SearchProductList.categoryFacets: List<ReadableCategory>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java:18`
- `SearchProductRequest.DEFAULT_COUNT: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:18`
- `SearchProductRequest.START_COUNT: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:19`
- `SearchProductRequest.query: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:21`
- `SearchProductRequest.count: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:22`
- `SearchProductRequest.start: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:23`

## Functions and methods
- `NamedEntity.getName() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:23`
- `NamedEntity.setName(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:26`
- `NamedEntity.getDescription() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:29`
- `NamedEntity.setDescription(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:32`
- `NamedEntity.getFriendlyUrl() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:35`
- `NamedEntity.setFriendlyUrl(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:38`
- `NamedEntity.getKeyWords() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:41`
- `NamedEntity.setKeyWords(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:44`
- `NamedEntity.getHighlights() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:47`
- `NamedEntity.setHighlights(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:50`
- `NamedEntity.getMetaDescription() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:53`
- `NamedEntity.setMetaDescription(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:56`
- `NamedEntity.getTitle() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:59`
- `NamedEntity.setTitle(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/NamedEntity.java:62`
- `ProductList.setProducts(List<ReadableProduct>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:21`
- `ProductList.getProducts() -> List<ReadableProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:24`
- `ProductList.getProductCount() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:27`
- `ProductList.setProductCount(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:30`
- `ProductList.getMinPrice() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:33`
- `ProductList.setMinPrice(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:36`
- `ProductList.getMaxPrice() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:39`
- `ProductList.setMaxPrice(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:42`
- `SearchProductList.getCategoryFacets() -> List<ReadableCategory>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java:19`
- `SearchProductList.setCategoryFacets(List<ReadableCategory>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java:22`
- `SearchProductRequest.getQuery() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:25`
- `SearchProductRequest.setQuery(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:29`
- `SearchProductRequest.getStart() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:33`
- `SearchProductRequest.setStart(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:37`
- `SearchProductRequest.getCount() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:41`
- `SearchProductRequest.setCount(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductRequest.java:45`

## Depends on
- [com.salesmanager.shop.model.catalog.category.ReadableCategory](/modules/com.salesmanager.shop.model.catalog.category.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/SearchProductList.java:18`
- [com.salesmanager.shop.model.catalog.product.ReadableProduct](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/ProductList.java:20`
