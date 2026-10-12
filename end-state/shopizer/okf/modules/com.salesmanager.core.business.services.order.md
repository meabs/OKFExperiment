---
type: Code Module
title: "com.salesmanager.core.business.services.order"
description: "com.salesmanager.core.business.services.order: OrderServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java"
    sha256: "b1bbe501d2890671992f860d429b07d77705aef88856a19f2736a50a6690e264"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java"
    sha256: "9bfb499fd7784c31548df502946bc4c773ecc9e7e3cfc88cd6d5475ecee5dba2"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.order

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java`

## Types
- `OrderService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:25`
- `OrderServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:69`

## Fields
- `OrderServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:72`
- `OrderServiceImpl.invoiceModule: InvoiceModule` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:75`
- `OrderServiceImpl.shippingService: ShippingService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:78`
- `OrderServiceImpl.paymentService: PaymentService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:81`
- `OrderServiceImpl.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:84`
- `OrderServiceImpl.taxService: TaxService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:87`
- `OrderServiceImpl.customerService: CustomerService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:90`
- `OrderServiceImpl.shoppingCartService: ShoppingCartService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:93`
- `OrderServiceImpl.transactionService: TransactionService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:96`
- `OrderServiceImpl.orderTotalService: OrderTotalService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:99`
- `OrderServiceImpl.orderRepository: OrderRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:101`

## Functions and methods
- `OrderService.addOrderStatusHistory(Order, OrderStatusHistory) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:27`
- `OrderService.caculateOrderTotal(OrderSummary, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:39`
- `OrderService.caculateOrderTotal(OrderSummary, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:51`
- `OrderService.calculateShoppingCartTotal(ShoppingCart, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:64`
- `OrderService.calculateShoppingCartTotal(ShoppingCart, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:74`
- `OrderService.generateInvoice(MerchantStore, Order, Language) -> ByteArrayOutputStream` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:76`
- `OrderService.getOrder(Long, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:79`
- `OrderService.listByStore(MerchantStore, OrderCriteria) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:88`
- `OrderService.getOrders(OrderCriteria, MerchantStore) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:96`
- `OrderService.saveOrUpdate(Order) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:98`
- `OrderService.processOrder(Order, Customer, List<ShoppingCartItem>, OrderTotalSummary, Payment, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:100`
- `OrderService.processOrder(Order, Customer, List<ShoppingCartItem>, OrderTotalSummary, Payment, Transaction, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:104`
- `OrderService.hasDownloadFiles(Order) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:118`
- `OrderService.getCapturableOrders(MerchantStore, Date, Date) -> List<Order>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderService.java:128`
- `OrderServiceImpl.addOrderStatusHistory(Order, OrderStatusHistory) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:109`
- `OrderServiceImpl.processOrder(Order, Customer, List<ShoppingCartItem>, OrderTotalSummary, Payment, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:116`
- `OrderServiceImpl.processOrder(Order, Customer, List<ShoppingCartItem>, OrderTotalSummary, Payment, Transaction, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:122`
- `OrderServiceImpl.process(Order, Customer, List<ShoppingCartItem>, OrderTotalSummary, Payment, Transaction, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:127`
- `OrderServiceImpl.caculateOrder(OrderSummary, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:217`
- `OrderServiceImpl.caculateOrderTotal(OrderSummary, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:399`
- `OrderServiceImpl.caculateOrderTotal(OrderSummary, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:416`
- `OrderServiceImpl.caculateShoppingCart(ShoppingCart, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:430`
- `OrderServiceImpl.calculateShoppingCartTotal(ShoppingCart, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:478`
- `OrderServiceImpl.calculateShoppingCartTotal(ShoppingCart, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:508`
- `OrderServiceImpl.delete(Order) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:523`
- `OrderServiceImpl.generateInvoice(MerchantStore, Order, Language) -> ByteArrayOutputStream` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:531`
- `OrderServiceImpl.getOrder(Long, MerchantStore) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:547`
- `OrderServiceImpl.listByStore(MerchantStore, OrderCriteria) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:556`
- `OrderServiceImpl.getOrders(OrderCriteria, MerchantStore) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:561`
- `OrderServiceImpl.saveOrUpdate(Order) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:567`
- `OrderServiceImpl.hasDownloadFiles(Order) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:581`
- `OrderServiceImpl.getCapturableOrders(MerchantStore, Date, Date) -> List<Order>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:600`

## Depends on
- [com.salesmanager.core.business.modules.order.InvoiceModule](/modules/com.salesmanager.core.business.modules.order.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:74`
- [com.salesmanager.core.business.repositories.order.OrderRepository](/modules/com.salesmanager.core.business.repositories.order.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:101`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:83`
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:89`
- [com.salesmanager.core.business.services.order.ordertotal.OrderTotalService](/modules/com.salesmanager.core.business.services.order.ordertotal.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:98`
- [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:80`
- [com.salesmanager.core.business.services.payments.TransactionService](/modules/com.salesmanager.core.business.services.payments.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:95`
- [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:77`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:92`
- [com.salesmanager.core.business.services.tax.TaxService](/modules/com.salesmanager.core.business.services.tax.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:86`

## Calls
- `OrderServiceImpl.caculateOrder` calls [com.salesmanager.core.business.services.order.ordertotal.OrderTotalService](/modules/com.salesmanager.core.business.services.order.ordertotal.md) `OrderTotalService.findOrderTotalVariation` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:285`
- `OrderServiceImpl.caculateOrder` calls [com.salesmanager.core.business.services.tax.TaxService](/modules/com.salesmanager.core.business.services.tax.md) `TaxService.calculateTax` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:354`
- `OrderServiceImpl.caculateShoppingCart` calls [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `ShoppingCartService.saveOrUpdate` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:451`
- `OrderServiceImpl.generateInvoice` calls [com.salesmanager.core.business.modules.order.InvoiceModule](/modules/com.salesmanager.core.business.modules.order.md) `InvoiceModule.createInvoice` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:538`
- `OrderServiceImpl.getCapturableOrders` calls [com.salesmanager.core.business.services.payments.TransactionService](/modules/com.salesmanager.core.business.services.payments.md) `TransactionService.listTransactions` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:603`
- `OrderServiceImpl.getOrder` calls [com.salesmanager.core.business.repositories.order.OrderRepository](/modules/com.salesmanager.core.business.repositories.order.md) `OrderRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:551`
- `OrderServiceImpl.getOrders` calls [com.salesmanager.core.business.repositories.order.OrderRepositoryCustom](/modules/com.salesmanager.core.business.repositories.order.md) `OrderRepositoryCustom.listOrders` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:563`
- `OrderServiceImpl.listByStore` calls [com.salesmanager.core.business.repositories.order.OrderRepositoryCustom](/modules/com.salesmanager.core.business.repositories.order.md) `OrderRepositoryCustom.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:558`
- `OrderServiceImpl.process` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create`, `SalesManagerEntityService.update` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:166`
- `OrderServiceImpl.process` calls [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `PaymentService.processPayment` `sm-core/src/main/java/com/salesmanager/core/business/services/order/OrderServiceImpl.java:147`
