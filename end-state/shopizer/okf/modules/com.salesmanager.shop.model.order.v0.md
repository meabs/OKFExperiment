---
type: Code Module
title: "com.salesmanager.shop.model.order.v0"
description: "com.salesmanager.shop.model.order.v0: Order, PersistableOrder, ReadableOrder, ReadableOrderList"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/Order.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/Order.java"
    sha256: "cb9f330a95386c6cb15a3b494e51b1bc0eef2a77d440928f0bde91514633c9ab"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java"
    sha256: "295861d64f2503f7eaa59595753718f3def19a8aa1a4064a864f98ca2cbe53df"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java"
    sha256: "10b3dafe3183e095da376482a20cba9df007ad69d7209ebacf651e5649fdfedc"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrderList.java"
    sha256: "bb8f57e75d112e4a61520738572d01c480a6d860ad0c027038fea36fc5e0ba41"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.order.v0

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/Order.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrderList.java`

## Types
- `Order` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/Order.java:7`
- `PersistableOrder` (class) extends [com.salesmanager.shop.model.order.OrderEntity](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:10`
- `ReadableOrder` (class) extends [com.salesmanager.shop.model.order.OrderEntity](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:16`
- `ReadableOrderList` (class) extends [com.salesmanager.shop.model.entity.ReadableList](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrderList.java:8`

## Fields
- `PersistableOrder.customer: PersistableCustomer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:17`
- `PersistableOrder.orderProductItems: List<PersistableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:18`
- `PersistableOrder.shipToBillingAdress: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:19`
- `PersistableOrder.shipToDeliveryAddress: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:20`
- `ReadableOrder.customer: ReadableCustomer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:23`
- `ReadableOrder.products: List<ReadableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:24`
- `ReadableOrder.currencyModel: Currency` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:25`
- `ReadableOrder.billing: ReadableBilling` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:27`
- `ReadableOrder.delivery: ReadableDelivery` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:28`
- `ReadableOrder.store: ReadableMerchantStore` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:29`
- `ReadableOrder.total: OrderTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:93`
- `ReadableOrder.tax: OrderTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:94`
- `ReadableOrder.shipping: OrderTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:95`
- `ReadableOrderList.orders: List<ReadableOrder>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrderList.java:15`

## Functions and methods
- `PersistableOrder.setOrderProductItems(List<PersistableOrderProduct>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:23`
- `PersistableOrder.getOrderProductItems() -> List<PersistableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:26`
- `PersistableOrder.setCustomer(PersistableCustomer) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:29`
- `PersistableOrder.getCustomer() -> PersistableCustomer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:32`
- `PersistableOrder.isShipToBillingAdress() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:35`
- `PersistableOrder.setShipToBillingAdress(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:38`
- `PersistableOrder.isShipToDeliveryAddress() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:41`
- `PersistableOrder.setShipToDeliveryAddress(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:44`
- `ReadableOrder.setCustomer(ReadableCustomer) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:33`
- `ReadableOrder.getCustomer() -> ReadableCustomer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:36`
- `ReadableOrder.getTotal() -> OrderTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:39`
- `ReadableOrder.setTotal(OrderTotal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:42`
- `ReadableOrder.getTax() -> OrderTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:45`
- `ReadableOrder.setTax(OrderTotal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:48`
- `ReadableOrder.getShipping() -> OrderTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:51`
- `ReadableOrder.setShipping(OrderTotal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:54`
- `ReadableOrder.getProducts() -> List<ReadableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:58`
- `ReadableOrder.setProducts(List<ReadableOrderProduct>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:61`
- `ReadableOrder.setCurrencyModel(Currency) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:68`
- `ReadableOrder.getBilling() -> ReadableBilling` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:72`
- `ReadableOrder.setBilling(ReadableBilling) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:75`
- `ReadableOrder.getDelivery() -> Address` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:79`
- `ReadableOrder.setDelivery(ReadableDelivery) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:82`
- `ReadableOrder.getStore() -> ReadableMerchantStore` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:86`
- `ReadableOrder.setStore(ReadableMerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:89`
- `ReadableOrderList.getOrders() -> List<ReadableOrder>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrderList.java:19`
- `ReadableOrderList.setOrders(List<ReadableOrder>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrderList.java:22`

## Depends on
- [com.salesmanager.core.model.reference.currency.Currency](/modules/com.salesmanager.core.model.reference.currency.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:25`
- [com.salesmanager.shop.model.customer.PersistableCustomer](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:17`
- [com.salesmanager.shop.model.customer.ReadableBilling](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:27`
- [com.salesmanager.shop.model.customer.ReadableCustomer](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:23`
- [com.salesmanager.shop.model.customer.ReadableDelivery](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:28`
- [com.salesmanager.shop.model.order.PersistableOrderProduct](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/PersistableOrder.java:18`
- [com.salesmanager.shop.model.order.ReadableOrderProduct](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:24`
- [com.salesmanager.shop.model.order.total.OrderTotal](/modules/com.salesmanager.shop.model.order.total.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:93`
- [com.salesmanager.shop.model.store.ReadableMerchantStore](/modules/com.salesmanager.shop.model.store.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v0/ReadableOrder.java:29`
