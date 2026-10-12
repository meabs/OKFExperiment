---
type: Code Module
title: "com.salesmanager.shop.store.controller.search.facade"
description: "com.salesmanager.shop.store.controller.search.facade: SearchFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java"
    sha256: "444fb659131f682b4628c1ee79030bbf99ef8b92566e7b0a7993f77d13606d4f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java"
    sha256: "97078efd4af1d72d885eaf8fd05a18c071b6f470e43717e2aea22e847eef4537"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.search.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java`

## Types
- `SearchFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java:19`
- `SearchFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:41`

## Fields
- `SearchFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:44`
- `SearchFacadeImpl.searchService: SearchService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:47`
- `SearchFacadeImpl.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:50`
- `SearchFacadeImpl.categoryService: CategoryService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:53`
- `SearchFacadeImpl.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:56`
- `SearchFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:60`
- `SearchFacadeImpl.CATEGORY_FACET_NAME: String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:62`
- `SearchFacadeImpl.MANUFACTURER_FACET_NAME: String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:63`
- `SearchFacadeImpl.AUTOCOMPLETE_ENTRIES_COUNT: int` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:64`

## Functions and methods
- `SearchFacade.indexAllData(MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java:27`
- `SearchFacade.search(MerchantStore, Language, SearchProductRequest) -> List<SearchItem>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java:35`
- `SearchFacade.autocompleteRequest(String, MerchantStore, Language) -> ValueList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacade.java:52`
- `SearchFacadeImpl.indexAllData(MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:70`
- `SearchFacadeImpl.search(MerchantStore, Language, SearchProductRequest) -> List<SearchItem>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:85`
- `SearchFacadeImpl.search(MerchantStore, String, String, Integer, Integer) -> SearchResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:92`
- `SearchFacadeImpl.getCategoryFacets(MerchantStore, Language, List<Aggregation>) -> List<ReadableCategory>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:118`
- `SearchFacadeImpl.convertCategoryToReadableCategory(MerchantStore, Language, Map<String, Long>, Category) -> ReadableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:145`
- `SearchFacadeImpl.convertProductToReadableProduct(Product, MerchantStore, Language) -> ReadableProduct` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:161`
- `SearchFacadeImpl.autocompleteRequest(String, MerchantStore, Language) -> ValueList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:175`

## Depends on
- [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:52`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:55`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:49`
- [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:46`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:58`

## Calls
- `SearchFacadeImpl.autocompleteRequest` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.searchKeywords` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:189`
- `SearchFacadeImpl.convertCategoryToReadableCategory` calls [com.salesmanager.shop.populator.catalog.ReadableCategoryPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableCategoryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:149`
- `SearchFacadeImpl.convertProductToReadableProduct` calls [com.salesmanager.shop.populator.catalog.ReadableProductPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableProductPopulator.populate`, `ReadableProductPopulator.setimageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:169`
- `SearchFacadeImpl.indexAllData` calls [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `ProductService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:73`
- `SearchFacadeImpl.indexAllData` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.index` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:77`
- `SearchFacadeImpl.search` calls [com.salesmanager.core.business.services.search.SearchService](/modules/com.salesmanager.core.business.services.search.md) `SearchService.search` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/search/facade/SearchFacadeImpl.java:111`
