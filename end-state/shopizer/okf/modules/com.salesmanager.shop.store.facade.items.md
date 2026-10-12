---
type: Code Module
title: "com.salesmanager.shop.store.facade.items"
description: "com.salesmanager.shop.store.facade.items: ProductItemsFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java"
    sha256: "c762e4b11ff790a7ea2a9b106ecc6fa72a42496e917829eb6854a64740a7a12f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.items

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java`

## Types
- `ProductItemsFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:34`

## Fields
- `ProductItemsFacadeImpl.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:39`
- `ProductItemsFacadeImpl.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:42`
- `ProductItemsFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:46`
- `ProductItemsFacadeImpl.productRelationshipService: ProductRelationshipService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:49`

## Functions and methods
- `ProductItemsFacadeImpl.listItemsByManufacturer(MerchantStore, Language, Long, int, int) -> ReadableProductList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:51`
- `ProductItemsFacadeImpl.listItemsByIds(MerchantStore, Language, List<Long>, int, int) -> ReadableProductList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:85`
- `ProductItemsFacadeImpl.listItemsByGroup(String, MerchantStore, Language) -> ReadableProductList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:123`
- `ProductItemsFacadeImpl.addItemToGroup(Product, String, MerchantStore, Language) -> ReadableProductList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:147`
- `ProductItemsFacadeImpl.removeItemFromGroup(Product, String, MerchantStore, Language) -> ReadableProductList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:187`
- `ProductItemsFacadeImpl.deleteGroup(String, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:202`
- `ProductItemsFacadeImpl.createProductGroup(ProductGroup, MerchantStore) -> ProductGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:216`
- `ProductItemsFacadeImpl.updateProductGroup(String, ProductGroup, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:229`
- `ProductItemsFacadeImpl.listProductGroups(MerchantStore, Language) -> List<ProductGroup>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:249`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:41`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:38`
- [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:48`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:44`

## Calls
- `ProductItemsFacadeImpl.addItemToGroup` calls [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `ProductRelationshipService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:176`
- `ProductItemsFacadeImpl.createProductGroup` calls [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `ProductRelationshipService.addGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:222`
- `ProductItemsFacadeImpl.deleteGroup` calls [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `ProductRelationshipService.deleteGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:209`
- `ProductItemsFacadeImpl.listItemsByIds` calls [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `ProductService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:100`
- `ProductItemsFacadeImpl.listItemsByIds` calls [com.salesmanager.shop.populator.catalog.ReadableProductPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableProductPopulator.populate`, `ReadableProductPopulator.setimageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:112`
- `ProductItemsFacadeImpl.listItemsByManufacturer` calls [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `ProductService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:62`
- `ProductItemsFacadeImpl.listItemsByManufacturer` calls [com.salesmanager.shop.populator.catalog.ReadableProductPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableProductPopulator.populate`, `ReadableProductPopulator.setimageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:74`
- `ProductItemsFacadeImpl.removeItemFromGroup` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:196`
- `ProductItemsFacadeImpl.updateProductGroup` calls [com.salesmanager.core.business.services.catalog.product.relationship.ProductRelationshipService](/modules/com.salesmanager.core.business.services.catalog.product.relationship.md) `ProductRelationshipService.activateGroup`, `ProductRelationshipService.deactivateGroup` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/items/ProductItemsFacadeImpl.java:238`
