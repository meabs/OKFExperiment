---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product"
description: "com.salesmanager.core.business.services.catalog.product: ProductServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java"
    sha256: "c9362d1031668cffe53e41677d81d778fd272d7b24abcc52889f4070cdeae30c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java"
    sha256: "d317e5c3692c48fb9566fa80864663e9e00f1964e1137f99ef1ac711750ec508"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java`

## Types
- `ProductService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:22`
- `ProductServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:52`

## Fields
- `ProductServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:55`
- `ProductServiceImpl.productRepository: ProductRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:57`
- `ProductServiceImpl.categoryService: CategoryService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:60`
- `ProductServiceImpl.productAvailabilityService: ProductAvailabilityService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:63`
- `ProductServiceImpl.productPriceService: ProductPriceService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:66`
- `ProductServiceImpl.productOptionService: ProductOptionService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:69`
- `ProductServiceImpl.productOptionValueService: ProductOptionValueService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:72`
- `ProductServiceImpl.productAttributeService: ProductAttributeService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:75`
- `ProductServiceImpl.productRelationshipService: ProductRelationshipService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:78`
- `ProductServiceImpl.productImageService: ProductImageService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:81`
- `ProductServiceImpl.configuration: CoreConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:84`
- `ProductServiceImpl.productReviewService: ProductReviewService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:87`

## Functions and methods
- `ProductService.retrieveById(Long, MerchantStore) -> Optional<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:24`
- `ProductService.addProductDescription(Product, ProductDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:26`
- `ProductService.getProductDescription(Product, Language) -> ProductDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:28`
- `ProductService.getProductForLocale(long, Language, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:30`
- `ProductService.getProductsForLocale(Category, Language, Locale) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:32`
- `ProductService.getProducts(List<Long>) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:34`
- `ProductService.getProductsByIds(List<Long>) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:36`
- `ProductService.saveProduct(Product) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:44`
- `ProductService.getProductWithOnlyMerchantStoreById(Long) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:51`
- `ProductService.listByStore(MerchantStore, Language, ProductCriteria) -> ProductList` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:53`
- `ProductService.exists(String, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:56`
- `ProductService.listByStore(MerchantStore, Language, ProductCriteria, int, int) -> Page<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:68`
- `ProductService.listByStore(MerchantStore) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:71`
- `ProductService.listByTaxClass(TaxClass) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:73`
- `ProductService.getProducts(List<Long>, Language) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:75`
- `ProductService.getBySeUrl(MerchantStore, String, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:78`
- `ProductService.getBySku(String, MerchantStore, Language) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:86`
- `ProductService.getBySku(String, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:89`
- `ProductService.findOne(Long, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductService.java:97`
- `ProductServiceImpl.retrieveById(Long, MerchantStore) -> Optional<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:95`
- `ProductServiceImpl.addProductDescription(Product, ProductDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:100`
- `ProductServiceImpl.getProducts(List<Long>) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:113`
- `ProductServiceImpl.getProductsByIds(List<Long>) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:122`
- `ProductServiceImpl.getProductWithOnlyMerchantStoreById(Long) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:128`
- `ProductServiceImpl.getProducts(List<Long>, Language) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:133`
- `ProductServiceImpl.getProductDescription(Product, Language) -> ProductDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:142`
- `ProductServiceImpl.getBySeUrl(MerchantStore, String, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:152`
- `ProductServiceImpl.getProductForLocale(long, Language, Locale) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:157`
- `ProductServiceImpl.getProductsForLocale(Category, Language, Locale) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:169`
- `ProductServiceImpl.listByStore(MerchantStore, Language, ProductCriteria) -> ProductList` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:196`
- `ProductServiceImpl.listByStore(MerchantStore) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:202`
- `ProductServiceImpl.listByTaxClass(TaxClass) -> List<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:208`
- `ProductServiceImpl.delete(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:214`
- `ProductServiceImpl.create(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:247`
- `ProductServiceImpl.update(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:252`
- `ProductServiceImpl.saveOrUpdate(Product) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:259`
- `ProductServiceImpl.findOne(Long, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:338`
- `ProductServiceImpl.listByStore(MerchantStore, Language, ProductCriteria, int, int) -> Page<Product>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:345`
- `ProductServiceImpl.saveProduct(Product) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:363`
- `ProductServiceImpl.getBySku(String, MerchantStore, Language) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:373`
- `ProductServiceImpl.getBySku(String, MerchantStore) -> Product` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:391`
- `ProductServiceImpl.exists(String, MerchantStore) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:408`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.ProductRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:57`
- [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:59`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductAttributeService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:74`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductOptionService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:68`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductOptionValueService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:71`
- [com.salesmanager.core.business.services.catalog.product.availability.ProductAvailabilityService](/modules/com.salesmanager.core.business.services.catalog.product.availability.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:62`
- [com.salesmanager.core.business.services.catalog.product.image.ProductImageService](/modules/com.salesmanager.core.business.services.catalog.product.image.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:80`
- [com.salesmanager.core.business.services.catalog.product.price.ProductPriceService](/modules/com.salesmanager.core.business.services.catalog.product.price.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:65`
- [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:77`
- [com.salesmanager.core.business.services.catalog.product.review.ProductReviewService](/modules/com.salesmanager.core.business.services.catalog.product.review.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:86`
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:83`

## Calls
- `ProductServiceImpl.delete` calls [com.salesmanager.core.business.services.catalog.product.image.ProductImageService](/modules/com.salesmanager.core.business.services.catalog.product.image.md) `ProductImageService.removeProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:225`
- `ProductServiceImpl.delete` calls [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `ProductRelationshipService.deleteRelationship`, `ProductRelationshipService.listByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:239`
- `ProductServiceImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:233`
- `ProductServiceImpl.exists` calls [com.salesmanager.core.business.repositories.catalog.product.ProductRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.md) `ProductRepository.existsBySku` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:410`
- `ProductServiceImpl.getBySku` calls [com.salesmanager.core.business.repositories.catalog.product.ProductRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.md) `ProductRepository.findBySku` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:377`
- `ProductServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.catalog.product.ProductRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.product.md) `ProductRepositoryCustom.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:199`
- `ProductServiceImpl.listByTaxClass` calls [com.salesmanager.core.business.repositories.catalog.product.ProductRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.product.md) `ProductRepositoryCustom.listByTaxClass` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:210`
- `ProductServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.services.catalog.product.image.ProductImageService](/modules/com.salesmanager.core.business.services.catalog.product.image.md) `ProductImageService.addProductImage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:294`
- `ProductServiceImpl.saveOrUpdate` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete`, `SalesManagerEntityService.save` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/ProductServiceImpl.java:322`
