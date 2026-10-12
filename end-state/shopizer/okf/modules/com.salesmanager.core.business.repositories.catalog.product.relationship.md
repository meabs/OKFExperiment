---
type: Code Module
title: "com.salesmanager.core.business.repositories.catalog.product.relationship"
description: "com.salesmanager.core.business.repositories.catalog.product.relationship: ProductRelationshipRepositoryImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepository.java"
    sha256: "c7ac7c9c25bc3039d157f68f00a18388025bd76b5837689c10691156cacd00ee"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java"
    sha256: "55e7f46ab40a3a8511bee15c9f70de54f93239dbbef77b902fb5ed3becf37648"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java"
    sha256: "ca6546e2c22989a7f0e63afd8ccf923ecda18a80d8c3e470bf72f475808c9e4f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.catalog.product.relationship

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java`

## Types
- `ProductRelationshipRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository`, [com.salesmanager.core.business.repositories.catalog.product.relationship.ProductRelationshipRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.product.relationship.md) `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepository.java:8`
- `ProductRelationshipRepositoryCustom` (interface) `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:11`
- `ProductRelationshipRepositoryImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:15`

## Fields
- `ProductRelationshipRepositoryImpl.HQL_GET_BY_CODE_AND_STORE_ID_AND_PRODUCT_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:17`
- `ProductRelationshipRepositoryImpl.HQL_GET_BY_CODE_AND_STORE_ID_AND_RP_PRODUCT_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:26`
- `ProductRelationshipRepositoryImpl.HQL_GET_BY_PRODUCT_ID_AND_CODE_AVAILABLE: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:33`
- `ProductRelationshipRepositoryImpl.HQL_GET_PRODUCTS_BY_PRODUCT_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:54`
- `ProductRelationshipRepositoryImpl.HQL_GET_PRODUCT_BY_CODE_AND_STORE_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:64`
- `ProductRelationshipRepositoryImpl.HQL_GET_PRODUCT_BY_CODE_AND_STORE_ID_AND_LANG_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:71`
- `ProductRelationshipRepositoryImpl.HQL_GET_GROUP_BY_CODE_AND_STORE_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:95`
- `ProductRelationshipRepositoryImpl.HQL_GET_PRODUCT_RELATIONSHIP_BY_STORE_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:115`
- `ProductRelationshipRepositoryImpl.HQL_GET_PRODUCT_RELATIONSHIP_BY_CODE_AND_STORE_ID: String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:119`
- `ProductRelationshipRepositoryImpl.entityManager: EntityManager` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:129`

## Functions and methods
- `ProductRelationshipRepositoryCustom.getByType(MerchantStore, String, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:13`
- `ProductRelationshipRepositoryCustom.getByType(MerchantStore, String, Product, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:16`
- `ProductRelationshipRepositoryCustom.getByGroup(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:19`
- `ProductRelationshipRepositoryCustom.getGroups(MerchantStore) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:21`
- `ProductRelationshipRepositoryCustom.getByType(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:23`
- `ProductRelationshipRepositoryCustom.getGroupByType(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:25`
- `ProductRelationshipRepositoryCustom.listByProducts(Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:27`
- `ProductRelationshipRepositoryCustom.getByType(MerchantStore, String, Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:29`
- `ProductRelationshipRepositoryCustom.getByTypeAndRelatedProduct(MerchantStore, String, Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryCustom.java:32`
- `ProductRelationshipRepositoryImpl.getByType(MerchantStore, String, Product, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:131`
- `ProductRelationshipRepositoryImpl.getGroupByType(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:143`
- `ProductRelationshipRepositoryImpl.getByType(MerchantStore, String, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:152`
- `ProductRelationshipRepositoryImpl.getByGroup(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:162`
- `ProductRelationshipRepositoryImpl.getGroups(MerchantStore) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:171`
- `ProductRelationshipRepositoryImpl.getByType(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:183`
- `ProductRelationshipRepositoryImpl.listByProducts(Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:192`
- `ProductRelationshipRepositoryImpl.getByType(MerchantStore, String, Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:200`
- `ProductRelationshipRepositoryImpl.getByTypeAndRelatedProduct(MerchantStore, String, Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/catalog/product/relationship/ProductRelationshipRepositoryImpl.java:210`
