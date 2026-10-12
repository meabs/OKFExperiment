---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.type"
description: "com.salesmanager.core.model.catalog.product.type: ProductType, ProductTypeDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java"
    sha256: "6b4f803a4214e5d1e2764c324646eac455ff3a844ebfc9ac8eebb351ae7870bc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductTypeDescription.java"
    sha256: "a67dc92ed2bea2622ff8ea8efb97ed91ff22729f2518ab6fb5ede658e9c9c125"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.type

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductTypeDescription.java`

## Types
- `ProductType` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:27`
- `ProductTypeDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductTypeDescription.java:13`

## Fields
- `ProductType.GENERAL_TYPE: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:33`
- `ProductType.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:40`
- `ProductType.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:43`
- `ProductType.descriptions: Set<ProductTypeDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:46`
- `ProductType.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:49`
- `ProductType.allowAddToCart: Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:52`
- `ProductType.visible: Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:55`
- `ProductType.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:59`
- `ProductTypeDescription.productType: ProductType` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductTypeDescription.java:27`

## Functions and methods
- `ProductType.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:63`
- `ProductType.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:68`
- `ProductType.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:73`
- `ProductType.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:78`
- `ProductType.isAllowAddToCart() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:83`
- `ProductType.setAllowAddToCart(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:87`
- `ProductType.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:91`
- `ProductType.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:95`
- `ProductType.getAllowAddToCart() -> Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:99`
- `ProductType.setAllowAddToCart(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:103`
- `ProductType.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:107`
- `ProductType.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:111`
- `ProductType.getDescriptions() -> Set<ProductTypeDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:115`
- `ProductType.setDescriptions(Set<ProductTypeDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:119`
- `ProductType.getVisible() -> Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:123`
- `ProductType.setVisible(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:127`
- `ProductTypeDescription.getProductType() -> ProductType` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductTypeDescription.java:29`
- `ProductTypeDescription.setProductType(ProductType) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductTypeDescription.java:33`

## Depends on
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:42`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/type/ProductType.java:57`
