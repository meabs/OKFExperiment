---
type: Code Module
title: "com.salesmanager.core.model.catalog.product.price"
description: "com.salesmanager.core.model.catalog.product.price: FinalPrice, ProductPrice, ProductPriceDescription"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java"
    sha256: "af1b885d51876f3814a2ef6693be5d9533f93d59a4523c075f1bbd1dc681ade2"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java"
    sha256: "a92bc35c1ed06e337e0f9682dfd259002bcea14fe0d19bc3a4cc6605ff9b3bfc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java"
    sha256: "af775351e7bfcac12dd0afdfcb5381b558ac632279968b85e442884bd88d3287"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceType.java"
    sha256: "10141fed9c765a4f1210b4668b1ca6092533178404ac1ee5aefb55bcdce74d94"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.catalog.product.price

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceType.java`

## Types
- `FinalPrice` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:14`
- `ProductPrice` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:32`
- `ProductPriceDescription` (class) extends [com.salesmanager.core.model.common.description.Description](/modules/com.salesmanager.core.model.common.description.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:15`
- `ProductPriceType` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceType.java:3`

## Fields
- `FinalPrice.discountedPrice: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:20`
- `FinalPrice.originalPrice: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:21`
- `FinalPrice.finalPrice: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:22`
- `FinalPrice.discounted: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:23`
- `FinalPrice.discountPercent: int` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:24`
- `FinalPrice.stringPrice: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:25`
- `FinalPrice.stringDiscountedPrice: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:26`
- `FinalPrice.discountEndDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:28`
- `FinalPrice.defaultPrice: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:30`
- `FinalPrice.productPrice: ProductPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:31`
- `FinalPrice.additionalPrices: List<FinalPrice>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:32`
- `ProductPrice.DEFAULT_PRICE_CODE: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:37`
- `ProductPrice.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:43`
- `ProductPrice.descriptions: Set<ProductPriceDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:46`
- `ProductPrice.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:51`
- `ProductPrice.productPriceAmount: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:54`
- `ProductPrice.productPriceType: ProductPriceType` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:58`
- `ProductPrice.defaultPrice: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:61`
- `ProductPrice.productPriceSpecialStartDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:65`
- `ProductPrice.productPriceSpecialEndDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:69`
- `ProductPrice.productPriceSpecialAmount: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:72`
- `ProductPrice.productAvailability: ProductAvailability` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:77`
- `ProductPrice.productIdentifierId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:80`
- `ProductPriceDescription.DEFAULT_PRICE_DESCRIPTION: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:33`
- `ProductPriceDescription.productPrice: ProductPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:38`
- `ProductPriceDescription.priceAppender: String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:42`

## Functions and methods
- `FinalPrice.getAdditionalPrices() -> List<FinalPrice>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:34`
- `FinalPrice.setAdditionalPrices(List<FinalPrice>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:38`
- `FinalPrice.getOriginalPrice() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:42`
- `FinalPrice.setOriginalPrice(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:46`
- `FinalPrice.getDiscountPercent() -> int` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:52`
- `FinalPrice.setDiscountPercent(int) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:56`
- `FinalPrice.getDiscountEndDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:60`
- `FinalPrice.setDiscountEndDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:64`
- `FinalPrice.isDiscounted() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:68`
- `FinalPrice.setDiscounted(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:72`
- `FinalPrice.setDiscountedPrice(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:76`
- `FinalPrice.getDiscountedPrice() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:80`
- `FinalPrice.setFinalPrice(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:85`
- `FinalPrice.getFinalPrice() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:89`
- `FinalPrice.setDefaultPrice(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:93`
- `FinalPrice.isDefaultPrice() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:97`
- `FinalPrice.setProductPrice(ProductPrice) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:101`
- `FinalPrice.getProductPrice() -> ProductPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:105`
- `FinalPrice.getStringPrice() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:109`
- `FinalPrice.setStringPrice(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:113`
- `FinalPrice.getStringDiscountedPrice() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:117`
- `FinalPrice.setStringDiscountedPrice(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/FinalPrice.java:121`
- `ProductPrice.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:85`
- `ProductPrice.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:90`
- `ProductPrice.getProductPriceAmount() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:95`
- `ProductPrice.setProductPriceAmount(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:99`
- `ProductPrice.getProductPriceSpecialStartDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:103`
- `ProductPrice.setProductPriceSpecialStartDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:107`
- `ProductPrice.getProductPriceSpecialEndDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:111`
- `ProductPrice.setProductPriceSpecialEndDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:115`
- `ProductPrice.getProductPriceSpecialAmount() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:119`
- `ProductPrice.setProductPriceSpecialAmount(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:123`
- `ProductPrice.getDescriptions() -> Set<ProductPriceDescription>` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:127`
- `ProductPrice.setDescriptions(Set<ProductPriceDescription>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:131`
- `ProductPrice.isDefaultPrice() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:135`
- `ProductPrice.setDefaultPrice(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:139`
- `ProductPrice.setProductAvailability(ProductAvailability) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:143`
- `ProductPrice.getProductAvailability() -> ProductAvailability` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:147`
- `ProductPrice.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:151`
- `ProductPrice.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:155`
- `ProductPrice.setProductPriceType(ProductPriceType) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:159`
- `ProductPrice.getProductPriceType() -> ProductPriceType` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:163`
- `ProductPriceDescription.getPriceAppender() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:44`
- `ProductPriceDescription.setPriceAppender(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:48`
- `ProductPriceDescription.getProductPrice() -> ProductPrice` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:55`
- `ProductPriceDescription.setProductPrice(ProductPrice) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPriceDescription.java:59`

## Depends on
- [com.salesmanager.core.model.catalog.product.availability.ProductAvailability](/modules/com.salesmanager.core.model.catalog.product.availability.md) `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:74`

## Calls
- `ProductPrice.getProductPriceSpecialEndDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:112`
- `ProductPrice.getProductPriceSpecialStartDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:104`
- `ProductPrice.setProductPriceSpecialEndDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:116`
- `ProductPrice.setProductPriceSpecialStartDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/catalog/product/price/ProductPrice.java:108`
