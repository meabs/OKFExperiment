---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.variation"
description: "com.salesmanager.core.model.catalog.product.variation: ProductVariation"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java"
    sha256: "369585c44ad08764d67f9fa6f1255ef48661067d36ec6d1289ecbe56257d2406"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.variation

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java`

## Types
- `ProductVariation` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:37`

## Fields
- `ProductVariation.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:49`
- `ProductVariation.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:55`
- `ProductVariation.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:60`
- `ProductVariation.productOption: ProductOption` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:64`
- `ProductVariation.productOptionValue: ProductOptionValue` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:68`
- `ProductVariation.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:72`
- `ProductVariation.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:75`
- `ProductVariation.variantDefault: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:78`

## Functions and methods
- `ProductVariation.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:81`
- `ProductVariation.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:86`
- `ProductVariation.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:92`
- `ProductVariation.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:97`
- `ProductVariation.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:103`
- `ProductVariation.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:107`
- `ProductVariation.getProductOption() -> ProductOption` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:111`
- `ProductVariation.setProductOption(ProductOption) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:115`
- `ProductVariation.getProductOptionValue() -> ProductOptionValue` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:119`
- `ProductVariation.setProductOptionValue(ProductOptionValue) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:123`
- `ProductVariation.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:127`
- `ProductVariation.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:131`
- `ProductVariation.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:135`
- `ProductVariation.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:139`
- `ProductVariation.isVariantDefault() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:143`
- `ProductVariation.setVariantDefault(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:147`

## Depends on
- [com.salesmanager.core.model.catalog.product.attribute.ProductOption](/modules/com.salesmanager.core.model.catalog.product.attribute.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:62`
- [com.salesmanager.core.model.catalog.product.attribute.ProductOptionValue](/modules/com.salesmanager.core.model.catalog.product.attribute.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:66`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:48`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variation/ProductVariation.java:58`
