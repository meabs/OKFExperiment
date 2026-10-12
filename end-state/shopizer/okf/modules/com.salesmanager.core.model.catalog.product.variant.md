---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.variant"
description: "com.salesmanager.core.model.catalog.product.variant: ProductVariant, ProductVariantGroup, ProductVariantImage, ProductVariantImageDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java"
    sha256: "7670592128c86479dded8120caeec03de4c46ed28720fb704adc2eed9e233518"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java"
    sha256: "eb02c6e2f3a5eb1636458a62e1bb2b66f7c93df6fd1e2c6f1290007e3ca57ee6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java"
    sha256: "7e759520d6011ad3cbd7cf7c1f3390f42e999b181109d381b8a1f3c1e36d3a4c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java"
    sha256: "fc073d3de40ea9ba468a7c368f0171c03fb60655674ed768cdcbcb996efdeb70"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.variant

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java`

## Types
- `ProductVariant` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:37`
- `ProductVariantGroup` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:31`
- `ProductVariantImage` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:21`
- `ProductVariantImageDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:16`

## Fields
- `ProductVariant.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:56`
- `ProductVariant.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:60`
- `ProductVariant.dateAvailable: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:64`
- `ProductVariant.available: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:67`
- `ProductVariant.defaultSelection: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:70`
- `ProductVariant.variation: ProductVariation` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:74`
- `ProductVariant.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:78`
- `ProductVariant.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:81`
- `ProductVariant.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:84`
- `ProductVariant.variationValue: ProductVariation` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:88`
- `ProductVariant.sku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:93`
- `ProductVariant.productVariantGroup: ProductVariantGroup` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:97`
- `ProductVariant.availabilities: Set<ProductAvailability>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:100`
- `ProductVariantGroup.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:46`
- `ProductVariantGroup.images: List<ProductVariantImage>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:50`
- `ProductVariantGroup.productVariants: Set<ProductVariant>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:53`
- `ProductVariantGroup.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:57`
- `ProductVariantImage.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:36`
- `ProductVariantImage.productImage: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:39`
- `ProductVariantImage.defaultImage: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:42`
- `ProductVariantImage.productVariantGroup: ProductVariantGroup` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:46`
- `ProductVariantImage.descriptions: Set<ProductVariantImageDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:49`
- `ProductVariantImageDescription.productVariantImage: ProductVariantImage` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:30`
- `ProductVariantImageDescription.product: Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:35`
- `ProductVariantImageDescription.altTag: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:39`

## Functions and methods
- `ProductVariant.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:103`
- `ProductVariant.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:108`
- `ProductVariant.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:114`
- `ProductVariant.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:119`
- `ProductVariant.getDateAvailable() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:125`
- `ProductVariant.setDateAvailable(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:129`
- `ProductVariant.isAvailable() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:133`
- `ProductVariant.setAvailable(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:137`
- `ProductVariant.getVariation() -> ProductVariation` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:141`
- `ProductVariant.setVariation(ProductVariation) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:145`
- `ProductVariant.getProduct() -> Product` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:149`
- `ProductVariant.setProduct(Product) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:153`
- `ProductVariant.getVariationValue() -> ProductVariation` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:157`
- `ProductVariant.setVariationValue(ProductVariation) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:161`
- `ProductVariant.isDefaultSelection() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:165`
- `ProductVariant.setDefaultSelection(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:169`
- `ProductVariant.getSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:173`
- `ProductVariant.setSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:177`
- `ProductVariant.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:181`
- `ProductVariant.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:185`
- `ProductVariant.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:190`
- `ProductVariant.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:192`
- `ProductVariant.getProductVariantGroup() -> ProductVariantGroup` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:194`
- `ProductVariant.setProductVariantGroup(ProductVariantGroup) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:198`
- `ProductVariant.getAvailabilities() -> Set<ProductAvailability>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:202`
- `ProductVariant.setAvailabilities(Set<ProductAvailability>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:206`
- `ProductVariantGroup.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:59`
- `ProductVariantGroup.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:64`
- `ProductVariantGroup.getImages() -> List<ProductVariantImage>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:70`
- `ProductVariantGroup.setImages(List<ProductVariantImage>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:74`
- `ProductVariantGroup.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:79`
- `ProductVariantGroup.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:83`
- `ProductVariantGroup.getProductVariants() -> Set<ProductVariant>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:87`
- `ProductVariantGroup.setProductVariants(Set<ProductVariant>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:91`
- `ProductVariantImage.getProductImage() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:54`
- `ProductVariantImage.setProductImage(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:58`
- `ProductVariantImage.isDefaultImage() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:62`
- `ProductVariantImage.setDefaultImage(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:66`
- `ProductVariantImage.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:70`
- `ProductVariantImage.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:75`
- `ProductVariantImage.getDescriptions() -> Set<ProductVariantImageDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:80`
- `ProductVariantImage.setDescriptions(Set<ProductVariantImageDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:84`
- `ProductVariantImage.getProductVariantGroup() -> ProductVariantGroup` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:88`
- `ProductVariantImage.setProductVariantGroup(ProductVariantGroup) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImage.java:92`
- `ProductVariantImageDescription.getAltTag() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:42`
- `ProductVariantImageDescription.setAltTag(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:46`
- `ProductVariantImageDescription.getProductVariantImage() -> ProductVariantImage` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:50`
- `ProductVariantImageDescription.setProductVariantImage(ProductVariantImage) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:54`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:76`
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantImageDescription.java:32`
- [com.salesmanager.core.model.catalog.product.availability.ProductAvailability](/modules/com.salesmanager.core.model.catalog.product.availability.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:99`
- [com.salesmanager.core.model.catalog.product.variation.ProductVariation](/modules/com.salesmanager.core.model.catalog.product.variation.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:72`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariant.java:59`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/variant/ProductVariantGroup.java:55`
