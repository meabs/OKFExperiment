---
type: Code Module
title: "com.salesmanager.shop.store.controller.category.facade"
description: "com.salesmanager.shop.store.controller.category.facade: getCategoryHierarchy, saveCategory, getById, getByCode"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java"
    sha256: "dd969840f92d4e7876da9e43c518474b89840b1d0aee5ca7521a579547bd9e05"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.category.facade

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java`

## Types
- `CategoryFacade` (interface) `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:13`

## Functions and methods
- `CategoryFacade.getCategoryHierarchy(MerchantStore, ListCriteria, int, Language, List<String>, int, int) -> ReadableCategoryList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:26`
- `CategoryFacade.saveCategory(MerchantStore, PersistableCategory) -> PersistableCategory` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:34`
- `CategoryFacade.getById(MerchantStore, Long, Language) -> ReadableCategory` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:43`
- `CategoryFacade.getByCode(MerchantStore, String, Language) -> ReadableCategory` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:53`
- `CategoryFacade.getCategoryByFriendlyUrl(MerchantStore, String, Language) -> ReadableCategory` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:63`
- `CategoryFacade.getByCode(String, MerchantStore) -> Category` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:65`
- `CategoryFacade.deleteCategory(Long, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:67`
- `CategoryFacade.deleteCategory(Category) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:69`
- `CategoryFacade.categoryProductVariants(Long, MerchantStore, Language) -> List<ReadableProductVariant>` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:79`
- `CategoryFacade.existByCode(MerchantStore, String) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:88`
- `CategoryFacade.move(Long, Long, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:96`
- `CategoryFacade.setVisible(PersistableCategory, MerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:103`
- `CategoryFacade.listByProduct(MerchantStore, Long, Language) -> ReadableCategoryList` `sm-shop-model/src/main/java/com/salesmanager/shop/store/controller/category/facade/CategoryFacade.java:112`
