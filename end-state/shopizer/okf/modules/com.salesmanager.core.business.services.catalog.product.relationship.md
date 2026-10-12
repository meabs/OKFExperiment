---
type: Code Module
title: "com.salesmanager.core.business.services.catalog.product.relationship"
description: "com.salesmanager.core.business.services.catalog.product.relationship: ProductRelationshipServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java"
    sha256: "ff445f9cee21d946354510281d1a307a2313bf26b023835ec8dbbfb717485799"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java"
    sha256: "5ea37d81ec97ee1a16a7761d9a811a4997f8d297660e7f34e3f398537a4411de"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.catalog.product.relationship

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java`

## Types
- `ProductRelationshipService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:13`
- `ProductRelationshipServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:18`

## Fields
- `ProductRelationshipServiceImpl.productRelationshipRepository: ProductRelationshipRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:24`

## Functions and methods
- `ProductRelationshipService.saveOrUpdate(ProductRelationship) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:16`
- `ProductRelationshipService.getByType(MerchantStore, Product, ProductRelationshipType, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:28`
- `ProductRelationshipService.getByType(MerchantStore, Product, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:39`
- `ProductRelationshipService.getByType(MerchantStore, Product, ProductRelationshipType) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:50`
- `ProductRelationshipService.getByType(MerchantStore, ProductRelationshipType) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:61`
- `ProductRelationshipService.listByProduct(Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:64`
- `ProductRelationshipService.getByType(MerchantStore, ProductRelationshipType, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:67`
- `ProductRelationshipService.getGroups(MerchantStore) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:76`
- `ProductRelationshipService.getGroupDefinition(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:84`
- `ProductRelationshipService.addGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:91`
- `ProductRelationshipService.getByGroup(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:93`
- `ProductRelationshipService.deleteGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:96`
- `ProductRelationshipService.deactivateGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:99`
- `ProductRelationshipService.deleteRelationship(ProductRelationship) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:102`
- `ProductRelationshipService.activateGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:104`
- `ProductRelationshipService.getByGroup(MerchantStore, String, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipService.java:107`
- `ProductRelationshipServiceImpl.saveOrUpdate(ProductRelationship) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:33`
- `ProductRelationshipServiceImpl.addGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:47`
- `ProductRelationshipServiceImpl.getGroups(MerchantStore) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:56`
- `ProductRelationshipServiceImpl.deleteGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:61`
- `ProductRelationshipServiceImpl.deactivateGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:69`
- `ProductRelationshipServiceImpl.activateGroup(MerchantStore, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:78`
- `ProductRelationshipServiceImpl.deleteRelationship(ProductRelationship) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:87`
- `ProductRelationshipServiceImpl.listByProduct(Product) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:99`
- `ProductRelationshipServiceImpl.getByType(MerchantStore, Product, ProductRelationshipType, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:107`
- `ProductRelationshipServiceImpl.getByType(MerchantStore, ProductRelationshipType, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:114`
- `ProductRelationshipServiceImpl.getByType(MerchantStore, ProductRelationshipType) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:119`
- `ProductRelationshipServiceImpl.getByGroup(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:126`
- `ProductRelationshipServiceImpl.getByGroup(MerchantStore, String, Language) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:133`
- `ProductRelationshipServiceImpl.getByType(MerchantStore, Product, ProductRelationshipType) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:140`
- `ProductRelationshipServiceImpl.getGroupDefinition(MerchantStore, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:149`
- `ProductRelationshipServiceImpl.getByType(MerchantStore, Product, String) -> List<ProductRelationship>` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:154`

## Depends on
- [com.salesmanager.core.business.repositories.catalog.product.relationship.ProductRelationshipRepository](/modules/com.salesmanager.core.business.repositories.catalog.product.relationship.md) `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:24`

## Calls
- `ProductRelationshipServiceImpl.getByType` calls [com.salesmanager.core.model.catalog.product.relationship.ProductRelationshipType](/modules/com.salesmanager.core.model.catalog.product.relationship.md) `ProductRelationshipType.name` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:110`
- `ProductRelationshipServiceImpl.listByProduct` calls [com.salesmanager.core.business.repositories.catalog.product.relationship.ProductRelationshipRepositoryCustom](/modules/com.salesmanager.core.business.repositories.catalog.product.relationship.md) `ProductRelationshipRepositoryCustom.listByProducts` `sm-core/src/main/java/com/salesmanager/core/business/services/catalog/product/relationship/ProductRelationshipServiceImpl.java:102`
