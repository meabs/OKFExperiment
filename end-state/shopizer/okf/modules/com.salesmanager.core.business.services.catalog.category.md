---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.category"
description: "com.salesmanager.core.business.services.catalog.category: CategoryServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java"
    sha256: "28b6625f2eacc859588aedd1f2f6d19e9d84b3e157e2358d5f037c7699aea1bf"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java"
    sha256: "80163590868dd610c4945745282fda2de5268abc564400e219dbc9c8ecca3b49"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.category

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java`

## Types
- `CategoryService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:12`
- `CategoryServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:31`

## Fields
- `CategoryServiceImpl.categoryRepository: CategoryRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:35`
- `CategoryServiceImpl.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:38`
- `CategoryServiceImpl.pageableCategoryRepository: PageableCategoryRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:41`
- `CategoryServiceImpl.categoryDescriptionRepository: CategoryDescriptionRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:44`

## Functions and methods
- `CategoryService.getListByLineage(MerchantStore, String) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:14`
- `CategoryService.listBySeUrl(MerchantStore, String) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:16`
- `CategoryService.getDescription(Category, Language) -> CategoryDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:18`
- `CategoryService.addCategoryDescription(Category, CategoryDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:20`
- `CategoryService.addChild(Category, Category) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:22`
- `CategoryService.listByParent(Category) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:24`
- `CategoryService.listByStoreAndParent(MerchantStore, Category) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:26`
- `CategoryService.getByName(MerchantStore, String, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:29`
- `CategoryService.listByStore(MerchantStore) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:31`
- `CategoryService.getByCode(MerchantStore, String) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:33`
- `CategoryService.listByStore(MerchantStore, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:36`
- `CategoryService.saveOrUpdate(Category) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:39`
- `CategoryService.getListByDepth(MerchantStore, int) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:41`
- `CategoryService.getById(Long, int) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:43`
- `CategoryService.getById(Long, int, int) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:45`
- `CategoryService.getListByDepth(MerchantStore, Language, String, int, int, int) -> Page<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:47`
- `CategoryService.getListByDepth(MerchantStore, int, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:56`
- `CategoryService.getListByDepthFilterByFeatured(MerchantStore, int, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:65`
- `CategoryService.getListByLineage(String, String) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:67`
- `CategoryService.getByCode(String, String) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:70`
- `CategoryService.getById(MerchantStore, Long) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:72`
- `CategoryService.getBySeUrl(MerchantStore, String, Language) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:74`
- `CategoryService.listByParent(Category, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:76`
- `CategoryService.getOneByLanguage(long, Language) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:78`
- `CategoryService.countProductsByCategories(MerchantStore, List<Long>) -> List<Object[]>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:92`
- `CategoryService.getByProductId(Long, MerchantStore) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:95`
- `CategoryService.listByCodes(MerchantStore, List<String>, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:104`
- `CategoryService.listByIds(MerchantStore, List<Long>, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:114`
- `CategoryService.findById(Long) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:123`
- `CategoryService.count(MerchantStore) -> int` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryService.java:125`
- `CategoryServiceImpl.create(Category) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:54`
- `CategoryServiceImpl.countProductsByCategories(MerchantStore, List<Long>) -> List<Object[]>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:75`
- `CategoryServiceImpl.listByCodes(MerchantStore, List<String>, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:84`
- `CategoryServiceImpl.listByIds(MerchantStore, List<Long>, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:89`
- `CategoryServiceImpl.getOneByLanguage(long, Language) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:94`
- `CategoryServiceImpl.saveOrUpdate(Category) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:99`
- `CategoryServiceImpl.getListByLineage(MerchantStore, String) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:111`
- `CategoryServiceImpl.getListByLineage(String, String) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:121`
- `CategoryServiceImpl.listBySeUrl(MerchantStore, String) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:131`
- `CategoryServiceImpl.getBySeUrl(MerchantStore, String, Language) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:142`
- `CategoryServiceImpl.getByCode(MerchantStore, String) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:147`
- `CategoryServiceImpl.getByCode(String, String) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:158`
- `CategoryServiceImpl.getById(Long, int) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:169`
- `CategoryServiceImpl.listByParent(Category) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:186`
- `CategoryServiceImpl.listByStoreAndParent(MerchantStore, Category) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:197`
- `CategoryServiceImpl.listByParent(Category, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:208`
- `CategoryServiceImpl.addCategoryDescription(Category, CategoryDescription) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:217`
- `CategoryServiceImpl.delete(Category) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:231`
- `CategoryServiceImpl.getDescription(Category, Language) -> CategoryDescription` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:287`
- `CategoryServiceImpl.addChild(Category, Category) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:298`
- `CategoryServiceImpl.getListByDepth(MerchantStore, int) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:350`
- `CategoryServiceImpl.getListByDepthFilterByFeatured(MerchantStore, int, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:355`
- `CategoryServiceImpl.getByName(MerchantStore, String, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:360`
- `CategoryServiceImpl.listByStore(MerchantStore) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:371`
- `CategoryServiceImpl.listByStore(MerchantStore, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:381`
- `CategoryServiceImpl.getById(MerchantStore, Long) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:391`
- `CategoryServiceImpl.findById(Long) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:396`
- `CategoryServiceImpl.getListByDepth(MerchantStore, Language, String, int, int, int) -> Page<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:402`
- `CategoryServiceImpl.getListByDepth(MerchantStore, int, Language) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:411`
- `CategoryServiceImpl.count(MerchantStore) -> int` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:416`
- `CategoryServiceImpl.getById(Long, int, int) -> Category` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:421`
- `CategoryServiceImpl.getByProductId(Long, MerchantStore) -> List<Category>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:426`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.category.CategoryDescriptionRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:43`
- [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:35`
- [com.salesmanager.core.business.repositories.catalog.category.PageableCategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:40`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:37`

## Calls
- `CategoryServiceImpl.count` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.count` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:418`
- `CategoryServiceImpl.countProductsByCategories` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepositoryCustom.countProductsByCategories` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:79`
- `CategoryServiceImpl.delete` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:281`
- `CategoryServiceImpl.delete` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete`, `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:271`
- `CategoryServiceImpl.findById` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findById` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:398`
- `CategoryServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:151`
- `CategoryServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryDescriptionRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryDescriptionRepository.listByCategoryId` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:178`
- `CategoryServiceImpl.getById` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findById`, `CategoryRepository.findByIdAndStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:393`
- `CategoryServiceImpl.getByName` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByName` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:364`
- `CategoryServiceImpl.getByProductId` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepositoryCustom.listByProduct` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:428`
- `CategoryServiceImpl.getBySeUrl` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByFriendlyUrl` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:144`
- `CategoryServiceImpl.getListByDepth` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.find`, `CategoryRepository.findByDepth` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:413`
- `CategoryServiceImpl.getListByDepth` calls [com.salesmanager.core.business.repositories.catalog.category.PageableCategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `PageableCategoryRepository.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:408`
- `CategoryServiceImpl.getListByDepthFilterByFeatured` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByDepthFilterByFeatured` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:357`
- `CategoryServiceImpl.getListByLineage` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByLineage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:114`
- `CategoryServiceImpl.getOneByLanguage` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByIdAndLanguage` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:96`
- `CategoryServiceImpl.listByCodes` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByCodes` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:86`
- `CategoryServiceImpl.listByIds` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByIds` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:91`
- `CategoryServiceImpl.listByParent` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByParent` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:214`
- `CategoryServiceImpl.listByParent` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepositoryCustom.listByStoreAndParent` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:190`
- `CategoryServiceImpl.listBySeUrl` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.listByFriendlyUrl` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:135`
- `CategoryServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepository](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepository.findByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:375`
- `CategoryServiceImpl.listByStoreAndParent` calls [com.salesmanager.core.business.repositories.catalog.category.CategoryRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.category.md) `CategoryRepositoryCustom.listByStoreAndParent` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/category/CategoryServiceImpl.java:201`
