---
type: Code Module
title: "com.salesmanager.shop.store.facade.category"
description: "com.salesmanager.shop.store.facade.category: CategoryFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java"
    sha256: "b83eae9f9623cd527d9eb1a3b877e843fa99b66b05224100703868569695eb40"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.category

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java`

## Types
- `CategoryFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:49`

## Fields
- `CategoryFacadeImpl.categoryService: CategoryService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:53`
- `CategoryFacadeImpl.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:56`
- `CategoryFacadeImpl.persistableCatagoryPopulator: PersistableCategoryPopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:59`
- `CategoryFacadeImpl.readableCategoryMapper: ReadableCategoryMapper` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:62`
- `CategoryFacadeImpl.productAttributeService: ProductAttributeService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:65`
- `CategoryFacadeImpl.FEATURED_CATEGORY: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:67`
- `CategoryFacadeImpl.VISIBLE_CATEGORY: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:68`
- `CategoryFacadeImpl.ADMIN_CATEGORY: String` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:69`

## Functions and methods
- `CategoryFacadeImpl.getCategoryHierarchy(MerchantStore, ListCriteria, int, Language, List<String>, int, int) -> ReadableCategoryList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:71`
- `CategoryFacadeImpl.existByCode(MerchantStore, String) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:149`
- `CategoryFacadeImpl.saveCategory(MerchantStore, PersistableCategory) -> PersistableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:159`
- `CategoryFacadeImpl.populateCategory(MerchantStore, PersistableCategory, Category) -> Category` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:181`
- `CategoryFacadeImpl.saveCategory(MerchantStore, Category, Category) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:189`
- `CategoryFacadeImpl.getById(MerchantStore, Long, Language) -> ReadableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:243`
- `CategoryFacadeImpl.addChildToParent(ReadableCategory, List<ReadableCategory>) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:273`
- `CategoryFacadeImpl.getListByLineage(MerchantStore, String) -> List<Category>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:291`
- `CategoryFacadeImpl.getCategoryById(Long, Language) -> Category` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:299`
- `CategoryFacadeImpl.deleteCategory(Category) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:304`
- `CategoryFacadeImpl.getByCode(MerchantStore, String, Language) -> ReadableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:313`
- `CategoryFacadeImpl.getCategoryByFriendlyUrl(MerchantStore, String, Language) -> ReadableCategory` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:326`
- `CategoryFacadeImpl.getById(MerchantStore, Long) -> Category` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:346`
- `CategoryFacadeImpl.deleteCategory(Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:359`
- `CategoryFacadeImpl.getOne(Long, int) -> Category` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:365`
- `CategoryFacadeImpl.categoryProductVariants(Long, MerchantStore, Language) -> List<ReadableProductVariant>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:370`
- `CategoryFacadeImpl.move(Long, Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:469`
- `CategoryFacadeImpl.getByCode(String, MerchantStore) -> Category` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:523`
- `CategoryFacadeImpl.setVisible(PersistableCategory, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:532`
- `CategoryFacadeImpl.listByProduct(MerchantStore, Long, Language) -> ReadableCategoryList` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:545`

## Depends on
- [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:52`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductAttributeService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:64`
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:55`
- [com.salesmanager.shop.mapper.catalog.ReadableCategoryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:61`
- [com.salesmanager.shop.populator.catalog.PersistableCategoryPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:58`

## Calls
- `CategoryFacadeImpl.deleteCategory` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:307`
- `CategoryFacadeImpl.getByCode` calls [com.salesmanager.shop.populator.catalog.ReadableCategoryPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableCategoryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:321`
- `CategoryFacadeImpl.getById` calls [com.salesmanager.shop.mapper.catalog.ReadableCategoryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCategoryMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:258`
- `CategoryFacadeImpl.getCategoryByFriendlyUrl` calls [com.salesmanager.shop.populator.catalog.ReadableCategoryPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `ReadableCategoryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:341`
- `CategoryFacadeImpl.getCategoryHierarchy` calls [com.salesmanager.shop.mapper.catalog.ReadableCategoryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCategoryMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:105`
- `CategoryFacadeImpl.listByProduct` calls [com.salesmanager.shop.mapper.catalog.ReadableCategoryMapper](/modules/com.salesmanager.shop.mapper.catalog.md) `ReadableCategoryMapper.convert` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:555`
- `CategoryFacadeImpl.move` calls [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `CategoryService.addChild` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:486`
- `CategoryFacadeImpl.populateCategory` calls [com.salesmanager.shop.populator.catalog.PersistableCategoryPopulator](/modules/com.salesmanager.shop.populator.catalog.md) `PersistableCategoryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:183`
- `CategoryFacadeImpl.saveCategory` calls [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `CategoryService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:228`
- `CategoryFacadeImpl.setVisible` calls [com.salesmanager.core.business.services.catalog.category.CategoryService](/modules/com.salesmanager.core.business.services.catalog.category.md) `CategoryService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/category/CategoryFacadeImpl.java:539`
