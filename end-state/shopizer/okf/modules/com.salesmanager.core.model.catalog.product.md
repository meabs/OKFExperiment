---
type: Code Module
title: "com.salesmanager.core.model.catalog.product"
description: "com.salesmanager.core.model.catalog.product: Product, ProductCriteria, ProductDimensions, ProductList"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java"
    sha256: "05263e824aa697b73ae41fa877a9fc945da848d9c2c895d946a3eaa90f1408a8"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCondition.java"
    sha256: "4dbce88ce810c03f6af9bf5f62e2aa29537f0eeef307f14309721018924f46a3"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java"
    sha256: "2877ea59b23ecfe467bbb355da24907bdcf3a4680f666f4d51471455effa5d82"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java"
    sha256: "1cd72a63de7e1bcf07038ef497df2f022fbb552c20148c7c3c668f278440e4e1"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductList.java"
    sha256: "41f1240fe7780cd79e16de6f6d933e00663a20a807b94adfe8f168a1e67e3013"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/RentalStatus.java"
    sha256: "5fa075537d89f1710e44b16b0cf634e61af6eac36a4e77e2c147c3fab6fdad87"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCondition.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductList.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/RentalStatus.java`

## Types
- `Product` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:50`
- `ProductCondition` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCondition.java:3`
- `ProductCriteria` (class) extends [com.salesmanager.core.model.common.Criteria](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:8`
- `ProductDimensions` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:7`
- `ProductList` (class) extends [com.salesmanager.core.model.common.EntityList](/modules/com.salesmanager.core.model.common.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductList.java:8`
- `RentalStatus` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/RentalStatus.java:3`

## Fields
- `Product.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:66`
- `Product.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:69`
- `Product.descriptions: Set<ProductDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:72`
- `Product.availabilities: Set<ProductAvailability>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:78`
- `Product.attributes: Set<ProductAttribute>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:85`
- `Product.images: Set<ProductImage>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:91`
- `Product.relationships: Set<ProductRelationship>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:97`
- `Product.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:101`
- `Product.categories: Set<Category>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:120`
- `Product.variants: Set<ProductVariant>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:128`
- `Product.dateAvailable: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:132`
- `Product.available: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:136`
- `Product.preOrder: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:140`
- `Product.manufacturer: Manufacturer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:145`
- `Product.type: ProductType` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:149`
- `Product.taxClass: TaxClass` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:153`
- `Product.productVirtual: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:156`
- `Product.productShipeable: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:159`
- `Product.productIsFree: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:162`
- `Product.productLength: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:165`
- `Product.productWidth: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:168`
- `Product.productHeight: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:171`
- `Product.productWeight: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:174`
- `Product.productReviewAvg: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:177`
- `Product.productReviewCount: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:180`
- `Product.productOrdered: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:183`
- `Product.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:186`
- `Product.sku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:191`
- `Product.refSku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:197`
- `Product.condition: ProductCondition` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:200`
- `Product.rentalStatus: RentalStatus` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:207`
- `Product.rentalDuration: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:211`
- `Product.rentalPeriod: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:214`
- `Product.owner: Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:239`
- `ProductCriteria.ORIGIN_SHOP: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:10`
- `ProductCriteria.ORIGIN_ADMIN: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:11`
- `ProductCriteria.productName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:13`
- `ProductCriteria.attributeCriteria: List<AttributeCriteria>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:14`
- `ProductCriteria.origin: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:15`
- `ProductCriteria.available: Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:18`
- `ProductCriteria.categoryIds: List<Long>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:20`
- `ProductCriteria.availabilities: List<String>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:21`
- `ProductCriteria.productIds: List<Long>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:22`
- `ProductCriteria.optionValueIds: List<Long>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:23`
- `ProductCriteria.sku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:24`
- `ProductCriteria.optionValueCodes: List<String>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:27`
- `ProductCriteria.option: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:28`
- `ProductCriteria.status: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:30`
- `ProductCriteria.manufacturerId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:32`
- `ProductCriteria.ownerId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:34`
- `ProductDimensions.length: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:12`
- `ProductDimensions.width: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:15`
- `ProductDimensions.height: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:18`
- `ProductDimensions.weight: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:21`
- `ProductList.products: List<Product>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductList.java:16`

## Functions and methods
- `Product.getRentalPeriod() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:217`
- `Product.setRentalPeriod(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:221`
- `Product.getRentalDuration() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:225`
- `Product.setRentalDuration(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:229`
- `Product.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:244`
- `Product.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:249`
- `Product.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:254`
- `Product.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:259`
- `Product.isProductVirtual() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:265`
- `Product.getProductLength() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:271`
- `Product.setProductLength(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:275`
- `Product.getProductWidth() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:279`
- `Product.setProductWidth(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:283`
- `Product.getProductHeight() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:287`
- `Product.setProductHeight(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:291`
- `Product.getProductWeight() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:295`
- `Product.setProductWeight(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:299`
- `Product.getProductReviewAvg() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:303`
- `Product.setProductReviewAvg(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:307`
- `Product.getProductReviewCount() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:311`
- `Product.setProductReviewCount(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:315`
- `Product.getProductOrdered() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:320`
- `Product.setProductOrdered(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:324`
- `Product.getSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:328`
- `Product.setSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:332`
- `Product.getDescriptions() -> Set<ProductDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:336`
- `Product.setDescriptions(Set<ProductDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:340`
- `Product.getProductVirtual() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:345`
- `Product.setProductVirtual(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:349`
- `Product.getProductIsFree() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:353`
- `Product.setProductIsFree(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:357`
- `Product.getAttributes() -> Set<ProductAttribute>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:363`
- `Product.setAttributes(Set<ProductAttribute>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:367`
- `Product.getManufacturer() -> Manufacturer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:373`
- `Product.setManufacturer(Manufacturer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:377`
- `Product.getType() -> ProductType` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:381`
- `Product.setType(ProductType) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:385`
- `Product.getAvailabilities() -> Set<ProductAvailability>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:391`
- `Product.setAvailabilities(Set<ProductAvailability>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:395`
- `Product.getTaxClass() -> TaxClass` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:399`
- `Product.setTaxClass(TaxClass) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:403`
- `Product.getImages() -> Set<ProductImage>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:407`
- `Product.setImages(Set<ProductImage>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:411`
- `Product.getRelationships() -> Set<ProductRelationship>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:415`
- `Product.setRelationships(Set<ProductRelationship>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:419`
- `Product.getCategories() -> Set<Category>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:424`
- `Product.setCategories(Set<Category>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:428`
- `Product.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:432`
- `Product.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:436`
- `Product.getDateAvailable() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:442`
- `Product.setDateAvailable(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:446`
- `Product.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:450`
- `Product.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:454`
- `Product.setAvailable(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:460`
- `Product.isAvailable() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:464`
- `Product.isProductShipeable() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:468`
- `Product.setProductShipeable(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:472`
- `Product.getProductDescription() -> ProductDescription` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:477`
- `Product.getProductImage() -> ProductImage` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:484`
- `Product.isPreOrder() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:497`
- `Product.setPreOrder(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:501`
- `Product.getRefSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:505`
- `Product.setRefSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:509`
- `Product.getCondition() -> ProductCondition` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:513`
- `Product.setCondition(ProductCondition) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:517`
- `Product.getRentalStatus() -> RentalStatus` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:521`
- `Product.setRentalStatus(RentalStatus) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:525`
- `Product.getOwner() -> Customer` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:529`
- `Product.setOwner(Customer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:533`
- `Product.getVariants() -> Set<ProductVariant>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:537`
- `Product.setVariants(Set<ProductVariant>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:541`
- `Product.setAvailable(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:545`
- `Product.setProductShipeable(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:549`
- `ProductCriteria.getProductName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:36`
- `ProductCriteria.setProductName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:40`
- `ProductCriteria.getCategoryIds() -> List<Long>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:45`
- `ProductCriteria.setCategoryIds(List<Long>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:49`
- `ProductCriteria.getAvailabilities() -> List<String>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:53`
- `ProductCriteria.setAvailabilities(List<String>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:57`
- `ProductCriteria.getAvailable() -> Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:61`
- `ProductCriteria.setAvailable(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:65`
- `ProductCriteria.setAttributeCriteria(List<AttributeCriteria>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:69`
- `ProductCriteria.getAttributeCriteria() -> List<AttributeCriteria>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:73`
- `ProductCriteria.setProductIds(List<Long>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:77`
- `ProductCriteria.getProductIds() -> List<Long>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:81`
- `ProductCriteria.setManufacturerId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:85`
- `ProductCriteria.getManufacturerId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:89`
- `ProductCriteria.getStatus() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:93`
- `ProductCriteria.setStatus(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:97`
- `ProductCriteria.getOwnerId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:101`
- `ProductCriteria.setOwnerId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:105`
- `ProductCriteria.getOptionValueIds() -> List<Long>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:109`
- `ProductCriteria.setOptionValueIds(List<Long>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:113`
- `ProductCriteria.getOrigin() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:117`
- `ProductCriteria.setOrigin(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:121`
- `ProductCriteria.getOptionValueCodes() -> List<String>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:125`
- `ProductCriteria.setOptionValueCodes(List<String>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:129`
- `ProductCriteria.getOption() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:133`
- `ProductCriteria.setOption(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:137`
- `ProductCriteria.getSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:141`
- `ProductCriteria.setSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:145`
- `ProductDimensions.getLength() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:23`
- `ProductDimensions.setLength(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:27`
- `ProductDimensions.getWidth() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:31`
- `ProductDimensions.setWidth(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:35`
- `ProductDimensions.getWeight() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:39`
- `ProductDimensions.setWeight(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductDimensions.java:43`
- `ProductList.getProducts() -> List<Product>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductList.java:17`
- `ProductList.setProducts(List<Product>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductList.java:20`

## Depends on
- [com.salesmanager.core.model.catalog.category.Category](/modules/com.salesmanager.core.model.catalog.category.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:106`
- [com.salesmanager.core.model.catalog.product.attribute.AttributeCriteria](/modules/com.salesmanager.core.model.catalog.product.attribute.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/ProductCriteria.java:14`
- [com.salesmanager.core.model.catalog.product.attribute.ProductAttribute](/modules/com.salesmanager.core.model.catalog.product.attribute.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:84`
- [com.salesmanager.core.model.catalog.product.availability.ProductAvailability](/modules/com.salesmanager.core.model.catalog.product.availability.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:77`
- [com.salesmanager.core.model.catalog.product.description.ProductDescription](/modules/com.salesmanager.core.model.catalog.product.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:71`
- [com.salesmanager.core.model.catalog.product.image.ProductImage](/modules/com.salesmanager.core.model.catalog.product.image.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:90`
- [com.salesmanager.core.model.catalog.product.manufacturer.Manufacturer](/modules/com.salesmanager.core.model.catalog.product.manufacturer.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:143`
- [com.salesmanager.core.model.catalog.product.relationship.ProductRelationship](/modules/com.salesmanager.core.model.catalog.product.relationship.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:96`
- [com.salesmanager.core.model.catalog.product.type.ProductType](/modules/com.salesmanager.core.model.catalog.product.type.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:147`
- [com.salesmanager.core.model.catalog.product.variant.ProductVariant](/modules/com.salesmanager.core.model.catalog.product.variant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:127`
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:68`
- [com.salesmanager.core.model.customer.Customer](/modules/com.salesmanager.core.model.customer.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:237`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:99`
- [com.salesmanager.core.model.tax.taxclass.TaxClass](/modules/com.salesmanager.core.model.tax.taxclass.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/Product.java:151`

## Tests
- `com.salesmanager.test.catalog.ProductTest`
