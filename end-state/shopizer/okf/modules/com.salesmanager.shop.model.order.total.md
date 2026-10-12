---
type: Code Module
title: "com.salesmanager.shop.model.order.total"
description: "com.salesmanager.shop.model.order.total: OrderTotal, ReadableOrderTotal, ReadableTotal"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java"
    sha256: "b0061f7d535becd833971f09af0b973be6c5a78a5ced4daa664a2ea2ae66db40"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java"
    sha256: "97be7c2ca6ab20476680418a4d5f6da3f2624b676c653baad11f8fe6f7ff776a"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java"
    sha256: "24dee537af557bfb3fcaaebf652f90b33f9c22fef541bfe8b9046f3baf442620"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.order.total

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java`

## Types
- `OrderTotal` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:9`
- `ReadableOrderTotal` (class) extends [com.salesmanager.shop.model.order.total.OrderTotal](/modules/com.salesmanager.shop.model.order.total.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:5`
- `ReadableTotal` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:11`

## Fields
- `OrderTotal.title: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:15`
- `OrderTotal.text: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:16`
- `OrderTotal.code: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:17`
- `OrderTotal.order: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:18`
- `OrderTotal.module: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:19`
- `OrderTotal.value: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:20`
- `ReadableOrderTotal.total: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:11`
- `ReadableOrderTotal.discounted: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:12`
- `ReadableTotal.totals: List<ReadableOrderTotal>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:18`
- `ReadableTotal.grandTotal: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:19`

## Functions and methods
- `OrderTotal.getTitle() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:23`
- `OrderTotal.setTitle(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:26`
- `OrderTotal.getCode() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:29`
- `OrderTotal.setCode(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:32`
- `OrderTotal.getOrder() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:35`
- `OrderTotal.setOrder(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:38`
- `OrderTotal.getModule() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:41`
- `OrderTotal.setModule(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:44`
- `OrderTotal.getValue() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:47`
- `OrderTotal.setValue(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:50`
- `OrderTotal.getText() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:53`
- `OrderTotal.setText(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/OrderTotal.java:56`
- `ReadableOrderTotal.getTotal() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:13`
- `ReadableOrderTotal.setTotal(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:16`
- `ReadableOrderTotal.isDiscounted() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:19`
- `ReadableOrderTotal.setDiscounted(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableOrderTotal.java:22`
- `ReadableTotal.getTotals() -> List<ReadableOrderTotal>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:20`
- `ReadableTotal.setTotals(List<ReadableOrderTotal>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:23`
- `ReadableTotal.getGrandTotal() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:26`
- `ReadableTotal.setGrandTotal(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/total/ReadableTotal.java:29`
