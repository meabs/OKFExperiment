---
type: Code Module
title: "com.salesmanager.core.model.order.orderproduct"
description: "com.salesmanager.core.model.order.orderproduct: OrderProduct, OrderProductAttribute, OrderProductDownload, OrderProductPrice"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java"
    sha256: "4ba855b225d4979a5cfc0d502c695c855483c963d128c06c95d64a93994e5673"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java"
    sha256: "a27f5e9a60fa7e02cbf00f70df13643b84926cbfbfb780637c6ec6131b4760c4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java"
    sha256: "2ed49372497c18b2343093117d3eedf1985c64f273df54d1fbf2c9acf609dfac"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java"
    sha256: "785e5db0f2dcb77c621a60d1fa54fcff534bf15682903e23a0f95c526ecb3cc0"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.order.orderproduct

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java`

## Types
- `OrderProduct` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:23`
- `OrderProductAttribute` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:19`
- `OrderProductDownload` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:19`
- `OrderProductPrice` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:22`

## Fields
- `OrderProduct.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:32`
- `OrderProduct.sku: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:35`
- `OrderProduct.productName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:38`
- `OrderProduct.productQuantity: int` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:41`
- `OrderProduct.oneTimeCharge: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:44`
- `OrderProduct.order: Order` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:49`
- `OrderProduct.orderAttributes: Set<OrderProductAttribute>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:52`
- `OrderProduct.prices: Set<OrderProductPrice>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:55`
- `OrderProduct.downloads: Set<OrderProductDownload>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:58`
- `OrderProductAttribute.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:28`
- `OrderProductAttribute.productAttributePrice: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:31`
- `OrderProductAttribute.productAttributeIsFree: boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:34`
- `OrderProductAttribute.productAttributeWeight: java.math.BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:37`
- `OrderProductAttribute.orderProduct: OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:42`
- `OrderProductAttribute.productOptionId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:45`
- `OrderProductAttribute.productOptionValueId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:49`
- `OrderProductAttribute.productAttributeName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:52`
- `OrderProductAttribute.productAttributeValueName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:55`
- `OrderProductDownload.DEFAULT_DOWNLOAD_MAX_DAYS: int` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:24`
- `OrderProductDownload.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:30`
- `OrderProductDownload.orderProduct: OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:35`
- `OrderProductDownload.orderProductFilename: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:38`
- `OrderProductDownload.maxdays: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:41`
- `OrderProductDownload.downloadCount: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:44`
- `OrderProductPrice.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:32`
- `OrderProductPrice.orderProduct: OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:37`
- `OrderProductPrice.productPriceCode: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:41`
- `OrderProductPrice.productPrice: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:44`
- `OrderProductPrice.productPriceSpecial: BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:47`
- `OrderProductPrice.productPriceSpecialStartDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:51`
- `OrderProductPrice.productPriceSpecialEndDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:55`
- `OrderProductPrice.defaultPrice: Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:59`
- `OrderProductPrice.productPriceName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:63`

## Functions and methods
- `OrderProduct.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:63`
- `OrderProduct.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:67`
- `OrderProduct.getProductName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:72`
- `OrderProduct.setProductName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:76`
- `OrderProduct.getProductQuantity() -> int` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:80`
- `OrderProduct.setProductQuantity(int) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:84`
- `OrderProduct.getOrder() -> Order` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:90`
- `OrderProduct.setOrder(Order) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:94`
- `OrderProduct.getOrderAttributes() -> Set<OrderProductAttribute>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:99`
- `OrderProduct.setOrderAttributes(Set<OrderProductAttribute>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:103`
- `OrderProduct.getPrices() -> Set<OrderProductPrice>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:107`
- `OrderProduct.setPrices(Set<OrderProductPrice>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:111`
- `OrderProduct.getDownloads() -> Set<OrderProductDownload>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:115`
- `OrderProduct.setDownloads(Set<OrderProductDownload>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:119`
- `OrderProduct.setSku(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:124`
- `OrderProduct.getSku() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:128`
- `OrderProduct.setOneTimeCharge(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:132`
- `OrderProduct.getOneTimeCharge() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:136`
- `OrderProductAttribute.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:60`
- `OrderProductAttribute.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:64`
- `OrderProductAttribute.isProductAttributeIsFree() -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:69`
- `OrderProductAttribute.setProductAttributeIsFree(boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:73`
- `OrderProductAttribute.getProductAttributeWeight() -> java.math.BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:77`
- `OrderProductAttribute.setProductAttributeWeight(java.math.BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:81`
- `OrderProductAttribute.getOrderProduct() -> OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:86`
- `OrderProductAttribute.setOrderProduct(OrderProduct) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:90`
- `OrderProductAttribute.getProductAttributeName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:94`
- `OrderProductAttribute.setProductAttributeName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:98`
- `OrderProductAttribute.getProductAttributeValueName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:102`
- `OrderProductAttribute.setProductAttributeValueName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:106`
- `OrderProductAttribute.getProductAttributePrice() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:110`
- `OrderProductAttribute.setProductAttributePrice(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:114`
- `OrderProductAttribute.getProductOptionId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:118`
- `OrderProductAttribute.setProductOptionId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:122`
- `OrderProductAttribute.getProductOptionValueId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:126`
- `OrderProductAttribute.setProductOptionValueId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductAttribute.java:130`
- `OrderProductDownload.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:51`
- `OrderProductDownload.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:55`
- `OrderProductDownload.getOrderProduct() -> OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:59`
- `OrderProductDownload.setOrderProduct(OrderProduct) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:63`
- `OrderProductDownload.getOrderProductFilename() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:67`
- `OrderProductDownload.setOrderProductFilename(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:71`
- `OrderProductDownload.getMaxdays() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:75`
- `OrderProductDownload.setMaxdays(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:79`
- `OrderProductDownload.getDownloadCount() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:83`
- `OrderProductDownload.setDownloadCount(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductDownload.java:87`
- `OrderProductPrice.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:68`
- `OrderProductPrice.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:72`
- `OrderProductPrice.getDefaultPrice() -> Boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:76`
- `OrderProductPrice.setDefaultPrice(Boolean) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:80`
- `OrderProductPrice.getProductPriceName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:84`
- `OrderProductPrice.setProductPriceName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:88`
- `OrderProductPrice.getOrderProduct() -> OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:92`
- `OrderProductPrice.setOrderProduct(OrderProduct) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:96`
- `OrderProductPrice.setProductPriceCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:100`
- `OrderProductPrice.getProductPriceCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:104`
- `OrderProductPrice.setProductPriceSpecialStartDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:108`
- `OrderProductPrice.getProductPriceSpecialStartDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:113`
- `OrderProductPrice.setProductPriceSpecialEndDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:117`
- `OrderProductPrice.getProductPriceSpecialEndDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:121`
- `OrderProductPrice.setProductPriceSpecial(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:125`
- `OrderProductPrice.getProductPriceSpecial() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:129`
- `OrderProductPrice.setProductPrice(BigDecimal) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:133`
- `OrderProductPrice.getProductPrice() -> BigDecimal` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProductPrice.java:137`

## Depends on
- [com.salesmanager.core.model.order.Order](/modules/com.salesmanager.core.model.order.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderproduct/OrderProduct.java:46`
