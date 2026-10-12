---
type: Code Module
title: "com.salesmanager.core.model.order.orderstatus"
description: "com.salesmanager.core.model.order.orderstatus: OrderStatusHistory"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatus.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatus.java"
    sha256: "62836526c530e04f64f251063257c5619d65941674817e767e2582371e7955d9"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java"
    sha256: "5c36ecaec90dc2be1b5f55635ebcb2ed3db2876fa70db1721a90701a4bbaee96"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.order.orderstatus

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatus.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java`

## Types
- `OrderStatus` (enum) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatus.java:3`
- `OrderStatusHistory` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:27`

## Fields
- `OrderStatusHistory.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:37`
- `OrderStatusHistory.order: Order` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:42`
- `OrderStatusHistory.status: OrderStatus` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:45`
- `OrderStatusHistory.dateAdded: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:49`
- `OrderStatusHistory.customerNotified: java.lang.Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:52`
- `OrderStatusHistory.comments: String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:56`

## Functions and methods
- `OrderStatusHistory.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:61`
- `OrderStatusHistory.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:65`
- `OrderStatusHistory.getOrder() -> Order` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:69`
- `OrderStatusHistory.setOrder(Order) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:73`
- `OrderStatusHistory.getStatus() -> OrderStatus` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:77`
- `OrderStatusHistory.setStatus(OrderStatus) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:81`
- `OrderStatusHistory.getDateAdded() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:85`
- `OrderStatusHistory.setDateAdded(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:89`
- `OrderStatusHistory.getCustomerNotified() -> java.lang.Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:93`
- `OrderStatusHistory.setCustomerNotified(java.lang.Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:97`
- `OrderStatusHistory.getComments() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:101`
- `OrderStatusHistory.setComments(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:105`

## Depends on
- [com.salesmanager.core.model.order.Order](/modules/com.salesmanager.core.model.order.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:39`

## Calls
- `OrderStatusHistory.getDateAdded` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:86`
- `OrderStatusHistory.setDateAdded` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/orderstatus/OrderStatusHistory.java:90`
