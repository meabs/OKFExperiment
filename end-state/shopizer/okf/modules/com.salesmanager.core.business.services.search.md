---
type: Code Module
title: "com.salesmanager.core.business.services.search"
description: "com.salesmanager.core.business.services.search: SearchServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java"
    sha256: "bc6246eda1e6604f621396df4781d38d3e63b4b96643dcc2290cf20414282a71"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java"
    sha256: "3ae78ff74d6ab22c34152955c01718fd5340d771ae6bfd5ca45d9ec650ea3571"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.search

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java`

## Types
- `SearchService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java:14`
- `SearchServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:56`

## Fields
- `SearchServiceImpl.noIndex: boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:62`
- `SearchServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:64`
- `SearchServiceImpl.INDEX_PRODUCTS: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:66`
- `SearchServiceImpl.SETTINGS: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:68`
- `SearchServiceImpl.PRODUCT_MAPPING_DEFAULT: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:70`
- `SearchServiceImpl.QTY: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:72`
- `SearchServiceImpl.PRICE: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:73`
- `SearchServiceImpl.DISCOUNT_PRICE: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:74`
- `SearchServiceImpl.SKU: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:75`
- `SearchServiceImpl.VSKU: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:76`
- `SearchServiceImpl.KEYWORDS_MAPPING_DEFAULT: String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:83`
- `SearchServiceImpl.configuration: CoreConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:93`
- `SearchServiceImpl.applicationSearchConfiguration: ApplicationSearchConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:96`
- `SearchServiceImpl.productInventoryService: ProductInventoryService` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:99`
- `SearchServiceImpl.searchModule: SearchModule` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:102`

## Functions and methods
- `SearchService.index(MerchantStore, Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java:23`
- `SearchService.deleteDocument(MerchantStore, Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java:31`
- `SearchService.searchKeywords(MerchantStore, String, SearchRequest, int) -> SearchResponse` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java:37`
- `SearchService.search(MerchantStore, String, SearchRequest, int, int) -> SearchResponse` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java:43`
- `SearchService.getDocument(String, MerchantStore, Long) -> Optional<Document>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchService.java:47`
- `SearchServiceImpl.init() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:104`
- `SearchServiceImpl.index(MerchantStore, Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:122`
- `SearchServiceImpl.document(Long, List<String>, RequestOptions) -> List<Document>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:163`
- `SearchServiceImpl.indexProduct(MerchantStore, ProductDescription, Product, List<Map<String, String>>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:184`
- `SearchServiceImpl.config() -> SearchConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:256`
- `SearchServiceImpl.inventory(Product) -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:305`
- `SearchServiceImpl.inventory(ProductVariant) -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:326`
- `SearchServiceImpl.variants(ProductVariant) -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:347`
- `SearchServiceImpl.deleteDocument(MerchantStore, Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:377`
- `SearchServiceImpl.searchKeywords(MerchantStore, String, SearchRequest, int) -> SearchResponse` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:395`
- `SearchServiceImpl.search(MerchantStore, String, SearchRequest, int, int) -> SearchResponse` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:411`
- `SearchServiceImpl.getDocument(String, MerchantStore, Long) -> Optional<Document>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:428`
- `SearchServiceImpl.languages(Product) -> List<String>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:443`
- `SearchServiceImpl.manufacturer(Manufacturer, String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:447`
- `SearchServiceImpl.category(Category, String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:453`
- `SearchServiceImpl.attributes(Product, String) -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:459`
- `SearchServiceImpl.attribute(ProductAttribute, String) -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:476`
- `SearchServiceImpl.settings(SearchConfiguration, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:490`
- `SearchServiceImpl.mappings(SearchConfiguration, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:502`
- `SearchServiceImpl.loadClassPathResource(String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:511`

## Depends on
- [com.salesmanager.core.business.configuration.ApplicationSearchConfiguration](/modules/com.salesmanager.core.business.configuration.md) `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:95`
- [com.salesmanager.core.business.services.catalog.inventory.ProductInventoryService](/modules/com.salesmanager.core.business.services.catalog.inventory.md) `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:98`
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:92`

## Calls
- `SearchServiceImpl.inventory` calls [com.salesmanager.core.business.services.catalog.inventory.ProductInventoryService](/modules/com.salesmanager.core.business.services.catalog.inventory.md) `ProductInventoryService.inventory` `sm-core/src/main/java/com/salesmanager/core/business/services/search/SearchServiceImpl.java:312`
