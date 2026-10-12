---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.search"
description: "com.salesmanager.shop.store.api.v1.search: SearchApi; 2 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java"
    sha256: "bf8e942a02150bab8d7c331e603328488247fcfa0e3b83386d3eb05ea7e91b15"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.search

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java`

## Types
- `SearchApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:33`

## Fields
- `SearchApi.searchFacade: SearchFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:41`

## Functions and methods
- `SearchApi.search(SearchProductRequest, MerchantStore, Language) -> List<SearchItem>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:47`
- `SearchApi.autocomplete(SearchProductRequest, MerchantStore, Language) -> ValueList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:62`

## HTTP routes
- `POST /api/v1/search` handled by `com.salesmanager.shop.store.api.v1.search.SearchApi#search` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:47`
- `POST /api/v1/search/autocomplete` handled by `com.salesmanager.shop.store.api.v1.search.SearchApi#autocomplete` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:62`

## Depends on
- [com.salesmanager.shop.store.controller.search.facade.SearchFacade](/modules/com.salesmanager.shop.store.controller.search.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:41`

## Calls
- `SearchApi.autocomplete` calls [com.salesmanager.shop.store.controller.search.facade.SearchFacade](/modules/com.salesmanager.shop.store.controller.search.facade.md) `SearchFacade.autocompleteRequest` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:71`
- `SearchApi.search` calls [com.salesmanager.shop.store.controller.search.facade.SearchFacade](/modules/com.salesmanager.shop.store.controller.search.facade.md) `SearchFacade.search` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/search/SearchApi.java:59`

## Tests
- `com.salesmanager.test.shop.integration.search.SearchApiIntegrationTest`
