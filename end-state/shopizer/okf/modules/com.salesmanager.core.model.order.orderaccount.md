---
type: Code Module
title: "com.salesmanager.core.model.order.orderaccount"
description: "com.salesmanager.core.model.order.orderaccount: OrderAccount, OrderAccountProduct"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java"
    sha256: "d465178804f041b527df1082776c03dc05d4e9b583ceb8c47cd0771ba3ebb888"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java"
    sha256: "4e4fdd38217af2ede64acf98cc82291e050e3cffd974f2fc7cf1a38ff39ddd50"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.order.orderaccount

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java`

## Types
- `OrderAccount` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:26`
- `OrderAccountProduct` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:23`

## Fields
- `OrderAccount.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:35`
- `OrderAccount.order: Order` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:39`
- `OrderAccount.orderAccountStartDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:43`
- `OrderAccount.orderAccountEndDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:47`
- `OrderAccount.orderAccountBillDay: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:50`
- `OrderAccount.orderAccountProducts: Set<OrderAccountProduct>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:53`
- `OrderAccountProduct.orderAccountProductId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:33`
- `OrderAccountProduct.orderAccount: OrderAccount` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:37`
- `OrderAccountProduct.orderProduct: OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:41`
- `OrderAccountProduct.orderAccountProductStartDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:45`
- `OrderAccountProduct.orderAccountProductEndDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:49`
- `OrderAccountProduct.orderAccountProductEot: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:53`
- `OrderAccountProduct.orderAccountProductAccountedDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:57`
- `OrderAccountProduct.orderAccountProductLastStatusDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:61`
- `OrderAccountProduct.orderAccountProductLastTransactionStatus: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:64`
- `OrderAccountProduct.orderAccountProductPaymentFrequencyType: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:67`
- `OrderAccountProduct.orderAccountProductStatus: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:70`

## Functions and methods
- `OrderAccount.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:58`
- `OrderAccount.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:62`
- `OrderAccount.getOrder() -> Order` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:66`
- `OrderAccount.setOrder(Order) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:70`
- `OrderAccount.getOrderAccountStartDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:74`
- `OrderAccount.setOrderAccountStartDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:78`
- `OrderAccount.getOrderAccountEndDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:82`
- `OrderAccount.setOrderAccountEndDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:86`
- `OrderAccount.getOrderAccountBillDay() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:90`
- `OrderAccount.setOrderAccountBillDay(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:94`
- `OrderAccount.getOrderAccountProducts() -> Set<OrderAccountProduct>` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:98`
- `OrderAccount.setOrderAccountProducts(Set<OrderAccountProduct>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:102`
- `OrderAccountProduct.getOrderAccountProductId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:75`
- `OrderAccountProduct.setOrderAccountProductId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:79`
- `OrderAccountProduct.getOrderAccount() -> OrderAccount` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:83`
- `OrderAccountProduct.setOrderAccount(OrderAccount) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:87`
- `OrderAccountProduct.getOrderProduct() -> OrderProduct` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:91`
- `OrderAccountProduct.setOrderProduct(OrderProduct) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:95`
- `OrderAccountProduct.getOrderAccountProductStartDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:99`
- `OrderAccountProduct.setOrderAccountProductStartDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:103`
- `OrderAccountProduct.getOrderAccountProductEndDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:107`
- `OrderAccountProduct.setOrderAccountProductEndDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:111`
- `OrderAccountProduct.getOrderAccountProductEot() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:115`
- `OrderAccountProduct.setOrderAccountProductEot(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:119`
- `OrderAccountProduct.getOrderAccountProductAccountedDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:123`
- `OrderAccountProduct.setOrderAccountProductAccountedDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:127`
- `OrderAccountProduct.getOrderAccountProductLastStatusDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:132`
- `OrderAccountProduct.setOrderAccountProductLastStatusDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:136`
- `OrderAccountProduct.getOrderAccountProductLastTransactionStatus() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:141`
- `OrderAccountProduct.setOrderAccountProductLastTransactionStatus(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:145`
- `OrderAccountProduct.getOrderAccountProductPaymentFrequencyType() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:150`
- `OrderAccountProduct.setOrderAccountProductPaymentFrequencyType(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:154`
- `OrderAccountProduct.getOrderAccountProductStatus() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:159`
- `OrderAccountProduct.setOrderAccountProductStatus(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:163`

## Depends on
- [com.salesmanager.core.model.order.Order](/modules/com.salesmanager.core.model.order.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:37`
- [com.salesmanager.core.model.order.orderproduct.OrderProduct](/modules/com.salesmanager.core.model.order.orderproduct.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:39`

## Calls
- `OrderAccount.getOrderAccountEndDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:83`
- `OrderAccount.getOrderAccountStartDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:75`
- `OrderAccount.setOrderAccountEndDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:87`
- `OrderAccount.setOrderAccountStartDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccount.java:79`
- `OrderAccountProduct.getOrderAccountProductAccountedDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:124`
- `OrderAccountProduct.getOrderAccountProductEndDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:108`
- `OrderAccountProduct.getOrderAccountProductEot` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:116`
- `OrderAccountProduct.getOrderAccountProductLastStatusDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:133`
- `OrderAccountProduct.getOrderAccountProductStartDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:100`
- `OrderAccountProduct.setOrderAccountProductAccountedDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:129`
- `OrderAccountProduct.setOrderAccountProductEndDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:112`
- `OrderAccountProduct.setOrderAccountProductEot` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:120`
- `OrderAccountProduct.setOrderAccountProductLastStatusDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:138`
- `OrderAccountProduct.setOrderAccountProductStartDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderaccount/OrderAccountProduct.java:104`
