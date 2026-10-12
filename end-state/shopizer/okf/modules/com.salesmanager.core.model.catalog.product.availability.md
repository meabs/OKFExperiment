---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.availability"
description: "com.salesmanager.core.model.catalog.product.availability: ProductAvailability"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java"
    sha256: "12d666bd92588233db2be67c511a851d83041fa4ca5399d43f5ed728323dc2d4"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.availability

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java`

## Types
- `ProductAvailability` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:40`

## Fields
- `ProductAvailability.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:70`
- `ProductAvailability.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:76`
- `ProductAvailability.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:81`
- `ProductAvailability.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:86`
- `ProductAvailability.productVariant: ProductVariant` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:93`
- `ProductAvailability.sku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:97`
- `ProductAvailability.dimensions: ProductDimensions` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:100`
- `ProductAvailability.productQuantity: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:104`
- `ProductAvailability.productDateAvailable: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:108`
- `ProductAvailability.region: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:111`
- `ProductAvailability.regionVariant: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:114`
- `ProductAvailability.owner: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:117`
- `ProductAvailability.productStatus: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:120`
- `ProductAvailability.productIsAlwaysFreeShipping: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:123`
- `ProductAvailability.available: Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:126`
- `ProductAvailability.productQuantityOrderMin: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:129`
- `ProductAvailability.productQuantityOrderMax: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:132`
- `ProductAvailability.prices: Set<ProductPrice>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:135`

## Functions and methods
- `ProductAvailability.defaultPrice() -> ProductPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:138`
- `ProductAvailability.getProductQuantity() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:156`
- `ProductAvailability.setProductQuantity(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:160`
- `ProductAvailability.getProductDateAvailable() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:164`
- `ProductAvailability.setProductDateAvailable(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:168`
- `ProductAvailability.getRegion() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:172`
- `ProductAvailability.setRegion(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:176`
- `ProductAvailability.getRegionVariant() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:180`
- `ProductAvailability.setRegionVariant(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:184`
- `ProductAvailability.getProductStatus() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:188`
- `ProductAvailability.setProductStatus(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:192`
- `ProductAvailability.getProductIsAlwaysFreeShipping() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:196`
- `ProductAvailability.setProductIsAlwaysFreeShipping(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:200`
- `ProductAvailability.getProductQuantityOrderMin() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:204`
- `ProductAvailability.setProductQuantityOrderMin(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:208`
- `ProductAvailability.getProductQuantityOrderMax() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:212`
- `ProductAvailability.setProductQuantityOrderMax(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:216`
- `ProductAvailability.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:220`
- `ProductAvailability.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:225`
- `ProductAvailability.getProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:230`
- `ProductAvailability.setProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:234`
- `ProductAvailability.getPrices() -> Set<ProductPrice>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:238`
- `ProductAvailability.setPrices(Set<ProductPrice>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:242`
- `ProductAvailability.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:246`
- `ProductAvailability.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:250`
- `ProductAvailability.getOwner() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:254`
- `ProductAvailability.setOwner(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:258`
- `ProductAvailability.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:262`
- `ProductAvailability.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:267`
- `ProductAvailability.getAvailable() -> Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:273`
- `ProductAvailability.setAvailable(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:277`
- `ProductAvailability.getSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:281`
- `ProductAvailability.setSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:285`
- `ProductAvailability.getDimensions() -> ProductDimensions` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:289`
- `ProductAvailability.setDimensions(ProductDimensions) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:293`
- `ProductAvailability.getProductVariant() -> ProductVariant` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:297`
- `ProductAvailability.setProductVariant(ProductVariant) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:301`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:78`
- [com.salesmanager.core.model.catalog.product.ProductDimensions](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:99`
- [com.salesmanager.core.model.catalog.product.price.ProductPrice](/modules/com.salesmanager.core.model.catalog.product.price.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:134`
- [com.salesmanager.core.model.catalog.product.variant.ProductVariant](/modules/com.salesmanager.core.model.catalog.product.variant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:91`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:69`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:84`

## Calls
- `ProductAvailability.getProductDateAvailable` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:165`
- `ProductAvailability.setProductDateAvailable` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/availability/ProductAvailability.java:169`
