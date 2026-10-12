---
type: Code Module
title: "com.salesmanager.shop.model.order.v1"
description: "com.salesmanager.shop.model.order.v1: Order, PersistableAnonymousOrder, PersistableOrder, ReadableOrder"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java"
    sha256: "387f666a217a321c51f745a4fcbdd4ed0add32840cb1b3878158a1544d32cfec"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java"
    sha256: "deefaac1038f56d86f50903e12688b3a7534256c2c94c7da44d2000fe9403c97"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java"
    sha256: "a37bcc61cfaeaa5ce963c72e8c0463bb338aaa20ae2259b51c74b47c8e27bc57"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java"
    sha256: "542c15e4c141f7004773063897fa5b952d40adfe69094eeadc3aeff2543c0dd3"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java"
    sha256: "820e76cadb16a8b80a48e13fc66692ceb7a6be4b00d9831d3e65ab873020a74b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderList.java"
    sha256: "b90ebaec049df47a847c1eda3a3ba2492152d8f047deb4e501d08b6bfb275f92"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.order.v1

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderList.java`

## Types
- `Order` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:9`
- `PersistableAnonymousOrder` (class) extends [com.salesmanager.shop.model.order.v1.PersistableOrder](/modules/com.salesmanager.shop.model.order.v1.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java:5`
- `PersistableOrder` (class) extends [com.salesmanager.shop.model.order.v1.Order](/modules/com.salesmanager.shop.model.order.v1.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:12`
- `ReadableOrder` (class) extends [com.salesmanager.shop.model.order.v1.Order](/modules/com.salesmanager.shop.model.order.v1.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:12`
- `ReadableOrderConfirmation` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:12`
- `ReadableOrderList` (class) extends [com.salesmanager.shop.model.entity.ReadableList](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderList.java:9`

## Fields
- `Order.customerAgreement: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:16`
- `Order.comments: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:17`
- `Order.currency: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:18`
- `Order.attributes: List<OrderAttribute>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:19`
- `PersistableAnonymousOrder.customer: PersistableCustomer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java:12`
- `PersistableOrder.payment: PersistablePayment` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:19`
- `PersistableOrder.shippingQuote: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:20`
- `PersistableOrder.shoppingCartId: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:22`
- `PersistableOrder.customerId: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:24`
- `ReadableOrder.billing: ReadableBilling` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:20`
- `ReadableOrder.delivery: ReadableDelivery` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:21`
- `ReadableOrder.shippingOption: ShippingOption` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:22`
- `ReadableOrder.payment: ReadablePayment` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:23`
- `ReadableOrder.total: ReadableTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:24`
- `ReadableOrder.products: List<ReadableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:25`
- `ReadableOrderConfirmation.billing: Address` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:18`
- `ReadableOrderConfirmation.delivery: Address` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:19`
- `ReadableOrderConfirmation.shipping: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:20`
- `ReadableOrderConfirmation.payment: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:21`
- `ReadableOrderConfirmation.total: ReadableTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:22`
- `ReadableOrderConfirmation.products: List<ReadableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:23`
- `ReadableOrderList.orders: List<ReadableOrder>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderList.java:15`

## Functions and methods
- `Order.isCustomerAgreement() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:22`
- `Order.setCustomerAgreement(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:26`
- `Order.getComments() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:30`
- `Order.setComments(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:34`
- `Order.getCurrency() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:38`
- `Order.setCurrency(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:42`
- `Order.getAttributes() -> List<OrderAttribute>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:46`
- `Order.setAttributes(List<OrderAttribute>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:50`
- `PersistableAnonymousOrder.getCustomer() -> PersistableCustomer` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java:14`
- `PersistableAnonymousOrder.setCustomer(PersistableCustomer) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java:18`
- `PersistableOrder.getShoppingCartId() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:28`
- `PersistableOrder.setShoppingCartId(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:32`
- `PersistableOrder.getCustomerId() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:36`
- `PersistableOrder.setCustomerId(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:40`
- `PersistableOrder.getPayment() -> PersistablePayment` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:44`
- `PersistableOrder.setPayment(PersistablePayment) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:48`
- `PersistableOrder.getShippingQuote() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:52`
- `PersistableOrder.setShippingQuote(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:56`
- `ReadableOrder.getProducts() -> List<ReadableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:27`
- `ReadableOrder.setProducts(List<ReadableOrderProduct>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:30`
- `ReadableOrder.getDelivery() -> ReadableDelivery` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:33`
- `ReadableOrder.setDelivery(ReadableDelivery) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:36`
- `ReadableOrder.getPayment() -> ReadablePayment` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:39`
- `ReadableOrder.setPayment(ReadablePayment) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:42`
- `ReadableOrder.getTotal() -> ReadableTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:45`
- `ReadableOrder.setTotal(ReadableTotal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:48`
- `ReadableOrder.getShippingOption() -> ShippingOption` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:51`
- `ReadableOrder.setShippingOption(ShippingOption) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:54`
- `ReadableOrder.getBilling() -> ReadableBilling` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:57`
- `ReadableOrder.setBilling(ReadableBilling) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:60`
- `ReadableOrderConfirmation.getShipping() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:25`
- `ReadableOrderConfirmation.setShipping(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:28`
- `ReadableOrderConfirmation.getPayment() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:31`
- `ReadableOrderConfirmation.setPayment(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:34`
- `ReadableOrderConfirmation.getTotal() -> ReadableTotal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:37`
- `ReadableOrderConfirmation.setTotal(ReadableTotal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:40`
- `ReadableOrderConfirmation.getProducts() -> List<ReadableOrderProduct>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:43`
- `ReadableOrderConfirmation.setProducts(List<ReadableOrderProduct>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:46`
- `ReadableOrderConfirmation.getBilling() -> Address` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:49`
- `ReadableOrderConfirmation.setBilling(Address) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:52`
- `ReadableOrderConfirmation.getDelivery() -> Address` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:55`
- `ReadableOrderConfirmation.setDelivery(Address) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:58`
- `ReadableOrderList.getOrders() -> List<ReadableOrder>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderList.java:19`
- `ReadableOrderList.setOrders(List<ReadableOrder>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderList.java:22`

## Depends on
- [com.salesmanager.core.model.shipping.ShippingOption](/modules/com.salesmanager.core.model.shipping.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:22`
- [com.salesmanager.shop.model.customer.PersistableCustomer](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableAnonymousOrder.java:12`
- [com.salesmanager.shop.model.customer.ReadableBilling](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:20`
- [com.salesmanager.shop.model.customer.ReadableDelivery](/modules/com.salesmanager.shop.model.customer.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:21`
- [com.salesmanager.shop.model.customer.address.Address](/modules/com.salesmanager.shop.model.customer.address.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:18`
- [com.salesmanager.shop.model.order.OrderAttribute](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/Order.java:19`
- [com.salesmanager.shop.model.order.ReadableOrderProduct](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:25`
- [com.salesmanager.shop.model.order.ReadableOrderProduct](/modules/com.salesmanager.shop.model.order.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:23`
- [com.salesmanager.shop.model.order.total.ReadableTotal](/modules/com.salesmanager.shop.model.order.total.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:24`
- [com.salesmanager.shop.model.order.total.ReadableTotal](/modules/com.salesmanager.shop.model.order.total.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrderConfirmation.java:22`
- [com.salesmanager.shop.model.order.transaction.PersistablePayment](/modules/com.salesmanager.shop.model.order.transaction.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/PersistableOrder.java:19`
- [com.salesmanager.shop.model.order.transaction.ReadablePayment](/modules/com.salesmanager.shop.model.order.transaction.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/order/v1/ReadableOrder.java:23`
