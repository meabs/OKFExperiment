---
type: Code Module
title: "com.salesmanager.core.model.catalog.category"
description: "com.salesmanager.core.model.catalog.category: Category, CategoryDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java"
    sha256: "472d9435578f46119f0db664cb9e57125b88e8ca603e3b85b20958e667fceddc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java"
    sha256: "d30cd2afa63344591ce2b05df45a1c1a0900e871e4981cd3d262d4474fdd2476"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.category

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java`

## Types
- `Category` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:32`
- `CategoryDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:18`

## Fields
- `Category.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:47`
- `Category.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:50`
- `Category.descriptions: Set<CategoryDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:54`
- `Category.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:58`
- `Category.parent: Category` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:62`
- `Category.categories: List<Category>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:65`
- `Category.categoryImage: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:68`
- `Category.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:71`
- `Category.categoryStatus: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:74`
- `Category.visible: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:77`
- `Category.depth: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:80`
- `Category.lineage: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:83`
- `Category.featured: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:86`
- `Category.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:90`
- `CategoryDescription.category: Category` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:33`
- `CategoryDescription.seUrl: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:36`
- `CategoryDescription.categoryHighlight: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:39`
- `CategoryDescription.metatagTitle: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:50`
- `CategoryDescription.metatagKeywords: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:53`
- `CategoryDescription.metatagDescription: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:56`

## Functions and methods
- `Category.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:92`
- `Category.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:96`
- `Category.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:108`
- `Category.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:113`
- `Category.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:118`
- `Category.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:123`
- `Category.getCategoryImage() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:129`
- `Category.setCategoryImage(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:133`
- `Category.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:137`
- `Category.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:141`
- `Category.isCategoryStatus() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:145`
- `Category.setCategoryStatus(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:149`
- `Category.isVisible() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:153`
- `Category.setVisible(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:157`
- `Category.getDepth() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:161`
- `Category.setDepth(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:165`
- `Category.getLineage() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:169`
- `Category.setLineage(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:173`
- `Category.getParent() -> Category` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:177`
- `Category.setParent(Category) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:181`
- `Category.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:188`
- `Category.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:192`
- `Category.getCategories() -> List<Category>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:196`
- `Category.setCategories(List<Category>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:200`
- `Category.getDescription() -> CategoryDescription` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:204`
- `Category.isFeatured() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:212`
- `Category.setFeatured(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:216`
- `Category.getDescriptions() -> Set<CategoryDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:220`
- `Category.setDescriptions(Set<CategoryDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:224`
- `CategoryDescription.getCategoryHighlight() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:41`
- `CategoryDescription.setCategoryHighlight(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:45`
- `CategoryDescription.getSeUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:67`
- `CategoryDescription.setSeUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:71`
- `CategoryDescription.getMetatagTitle() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:75`
- `CategoryDescription.setMetatagTitle(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:79`
- `CategoryDescription.getMetatagKeywords() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:83`
- `CategoryDescription.setMetatagKeywords(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:87`
- `CategoryDescription.getMetatagDescription() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:91`
- `CategoryDescription.setMetatagDescription(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:95`
- `CategoryDescription.getCategory() -> Category` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:99`
- `CategoryDescription.setCategory(Category) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:103`

## Depends on
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:49`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/Category.java:56`
- [com.salesmanager.core.model.reference.language.Language](/modules/com.salesmanager.core.model.reference.language.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/category/CategoryDescription.java:61`

## Tests
- `com.salesmanager.test.catalog.CategoryTest`
