---
type: Code Module
title: "com.salesmanager.shop.populator.order.transaction"
description: "com.salesmanager.shop.populator.order.transaction: PersistablePaymentPopulator, PersistableTransactionPopulator, ReadableTransactionPopulator"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java"
    sha256: "732c5087ba0e0e257d585608574b64889f28672728d1f64fe38b07124b713247"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java"
    sha256: "1d7cd801fad37722c9c73c5a90861aadd3b3a9eac0a98fd9588e754780e3871a"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java"
    sha256: "a2d1c018abf661b53203e95a03b40ad32e5f114651f4472addc82a8f1f70e7eb"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.populator.order.transaction

Source: `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java`, `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java`

## Types
- `PersistablePaymentPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:18`
- `PersistableTransactionPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:18`
- `ReadableTransactionPopulator` (class) extends [com.salesmanager.core.business.utils.AbstractDataPopulator](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:16`

## Fields
- `PersistablePaymentPopulator.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:21`
- `PersistableTransactionPopulator.orderService: OrderService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:20`
- `PersistableTransactionPopulator.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:21`
- `ReadableTransactionPopulator.orderService: OrderService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:19`
- `ReadableTransactionPopulator.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:20`

## Functions and methods
- `PersistablePaymentPopulator.populate(PersistablePayment, Payment, MerchantStore, Language) -> Payment` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:25`
- `PersistablePaymentPopulator.createTarget() -> Payment` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:53`
- `PersistablePaymentPopulator.getPricingService() -> PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:59`
- `PersistablePaymentPopulator.setPricingService(PricingService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:63`
- `PersistableTransactionPopulator.populate(PersistableTransaction, Transaction, MerchantStore, Language) -> Transaction` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:23`
- `PersistableTransactionPopulator.createTarget() -> Transaction` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:67`
- `PersistableTransactionPopulator.getOrderService() -> OrderService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:73`
- `PersistableTransactionPopulator.setOrderService(OrderService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:77`
- `PersistableTransactionPopulator.getPricingService() -> PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:81`
- `PersistableTransactionPopulator.setPricingService(PricingService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:85`
- `ReadableTransactionPopulator.populate(Transaction, ReadableTransaction, MerchantStore, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:22`
- `ReadableTransactionPopulator.createTarget() -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:61`
- `ReadableTransactionPopulator.getOrderService() -> OrderService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:67`
- `ReadableTransactionPopulator.setOrderService(OrderService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:71`
- `ReadableTransactionPopulator.getPricingService() -> PricingService` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:75`
- `ReadableTransactionPopulator.setPricingService(PricingService) -> void` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:79`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:21`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:20`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:20`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:19`

## Calls
- `PersistablePaymentPopulator.populate` calls [com.salesmanager.core.model.payments.PaymentType](/modules/com.salesmanager.core.model.payments.md) `PaymentType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:39`
- `PersistablePaymentPopulator.populate` calls [com.salesmanager.core.model.payments.TransactionType](/modules/com.salesmanager.core.model.payments.md) `TransactionType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistablePaymentPopulator.java:40`
- `PersistableTransactionPopulator.populate` calls [com.salesmanager.core.model.payments.PaymentType](/modules/com.salesmanager.core.model.payments.md) `PaymentType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:41`
- `PersistableTransactionPopulator.populate` calls [com.salesmanager.core.model.payments.TransactionType](/modules/com.salesmanager.core.model.payments.md) `TransactionType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/PersistableTransactionPopulator.java:42`
- `ReadableTransactionPopulator.populate` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.formatDate` `sm-shop/src/main/java/com/salesmanager/shop/populator/order/transaction/ReadableTransactionPopulator.java:43`
