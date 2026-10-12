---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.order"
description: "com.salesmanager.shop.store.api.v1.order: OrderApi, OrderPaymentApi, OrderShippingApi, OrderStatusHistoryApi; 23 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java"
    sha256: "c5a9b9669f6b185713d5e762bf494b1cf2f495830098c1b372b39678be5a4b1e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java"
    sha256: "e924df91e68b214bb0277f260460d344073eb2447aff27cff37f08da07f3dd95"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java"
    sha256: "52d06da88f98fcc3474d7c11074934ff6659a60b614a2d125d3f83b3c370dd25"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java"
    sha256: "9aaa38f4ea97fb7bac7cf1a0dab14a9fbd9d5bee90068d7c73113f9d175ff48b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java"
    sha256: "ef37e28c1b7da9a26b00423338d7ba3477c75155ecd2edbf83c46839c5fd78ac"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.order

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java`

## Types
- `OrderApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:66`
- `OrderPaymentApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:59`
- `OrderShippingApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:48`
- `OrderStatusHistoryApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:32`
- `OrderTotalApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:42`

## Fields
- `OrderApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:72`
- `OrderApi.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:75`
- `OrderApi.orderFacade: OrderFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:78`
- `OrderApi.orderService: OrderService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:81`
- `OrderApi.orderFacadeV1: com.salesmanager.shop.store.controller.order.facade.v1.OrderFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:84`
- `OrderApi.shoppingCartService: ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:87`
- `OrderApi.customerFacade: CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:90`
- `OrderApi.customerFacadev1: CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:93`
- `OrderApi.authorizationUtils: AuthorizationUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:96`
- `OrderApi.credentialsService: CredentialsService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:99`
- `OrderApi.DEFAULT_ORDER_LIST_COUNT: String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:101`
- `OrderPaymentApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:65`
- `OrderPaymentApi.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:68`
- `OrderPaymentApi.orderService: OrderService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:71`
- `OrderPaymentApi.shoppingCartService: ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:74`
- `OrderPaymentApi.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:77`
- `OrderPaymentApi.paymentService: PaymentService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:80`
- `OrderPaymentApi.orderFacade: OrderFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:83`
- `OrderPaymentApi.authorizationUtils: AuthorizationUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:86`
- `OrderShippingApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:56`
- `OrderShippingApi.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:58`
- `OrderShippingApi.orderFacade: OrderFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:60`
- `OrderShippingApi.shoppingCartFacade: ShoppingCartFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:62`
- `OrderShippingApi.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:64`
- `OrderShippingApi.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:66`
- `OrderShippingApi.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:68`
- `OrderStatusHistoryApi.orderFacade: OrderFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:40`
- `OrderStatusHistoryApi.authorizationUtils: AuthorizationUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:43`
- `OrderTotalApi.shoppingCartFacade: ShoppingCartFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:50`
- `OrderTotalApi.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:52`
- `OrderTotalApi.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:54`
- `OrderTotalApi.customerService: CustomerService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:56`
- `OrderTotalApi.shippingQuoteService: ShippingQuoteService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:58`
- `OrderTotalApi.orderService: OrderService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:60`
- `OrderTotalApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:62`

## Functions and methods
- `OrderApi.list(Long, Integer, Integer, MerchantStore, Language, HttpServletResponse) -> ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:112`
- `OrderApi.list(Integer, Integer, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:165`
- `OrderApi.list(Integer, Integer, String, Long, String, String, String, MerchantStore, Language) -> ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:220`
- `OrderApi.get(Long, MerchantStore, Language) -> ReadableOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:263`
- `OrderApi.getOrder(Long, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:292`
- `OrderApi.checkout(String, PersistableOrder, MerchantStore, Language, HttpServletRequest, HttpServletResponse, Locale) -> ReadableOrderConfirmation` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:343`
- `OrderApi.checkout(String, PersistableAnonymousOrder, MerchantStore, Language) -> ReadableOrderConfirmation` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:402`
- `OrderApi.updateOrderCustomer(Long, PersistableCustomer, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:473`
- `OrderApi.updateOrderStatus(Long, String, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:494`
- `OrderPaymentApi.init(PersistablePayment, String, MerchantStore, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:88`
- `OrderPaymentApi.init(PersistablePayment, String, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:120`
- `OrderPaymentApi.nextTransaction(Long, MerchantStore, Language) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:183`
- `OrderPaymentApi.listTransactions(Long, MerchantStore, Language) -> List<ReadableTransaction>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:204`
- `OrderPaymentApi.listCapturableOrders(LocalDate, LocalDate, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:236`
- `OrderPaymentApi.capturePayment(Long, MerchantStore, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:292`
- `OrderPaymentApi.refundPayment(Long, MerchantStore, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:335`
- `OrderPaymentApi.authorizePayment(Long, MerchantStore, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:353`
- `OrderShippingApi.shipping(String, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableShippingSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:79`
- `OrderShippingApi.shipping(String, AddressLocation, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableShippingSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:190`
- `OrderStatusHistoryApi.list(Long, MerchantStore, Language) -> List<ReadableOrderStatusHistory>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:45`
- `OrderStatusHistoryApi.create(Long, PersistableOrderStatusHistory, MerchantStore, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:59`
- `OrderTotalApi.payment(Long, Long, MerchantStore, Language, HttpServletRequest, HttpServletResponse) -> ReadableOrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:75`
- `OrderTotalApi.calculateTotal(String, Long, MerchantStore, Language, HttpServletResponse) -> ReadableOrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:165`

## HTTP routes
- `POST /api/v1/auth/cart/{code}/checkout` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#checkout` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:343`
- `POST /api/v1/auth/cart/{code}/payment/init` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#init` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:120`
- `GET /api/v1/auth/cart/{code}/shipping` handled by `com.salesmanager.shop.store.api.v1.order.OrderShippingApi#shipping` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:79`
- `GET /api/v1/auth/cart/{id}/total` handled by `com.salesmanager.shop.store.api.v1.order.OrderTotalApi#payment` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:75`
- `GET /api/v1/auth/orders` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:165`
- `GET /api/v1/auth/orders/{id}` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#getOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:292`
- `POST /api/v1/cart/{code}/checkout` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#checkout` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:402`
- `POST /api/v1/cart/{code}/payment/init` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#init` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:88`
- `POST /api/v1/cart/{code}/shipping` handled by `com.salesmanager.shop.store.api.v1.order.OrderShippingApi#shipping` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:190`
- `GET /api/v1/cart/{code}/total` handled by `com.salesmanager.shop.store.api.v1.order.OrderTotalApi#calculateTotal` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:165`
- `GET /api/v1/private/orders` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:220`
- `GET /api/v1/private/orders/customers/{id}` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:112`
- `GET /api/v1/private/orders/payment/capturable` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#listCapturableOrders` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:236`
- `GET /api/v1/private/orders/{id}` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#get` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:263`
- `POST /api/v1/private/orders/{id}/authorize` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#authorizePayment` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:353`
- `POST /api/v1/private/orders/{id}/capture` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#capturePayment` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:292`
- `PATCH /api/v1/private/orders/{id}/customer` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#updateOrderCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:473`
- `GET /api/v1/private/orders/{id}/history` handled by `com.salesmanager.shop.store.api.v1.order.OrderStatusHistoryApi#list` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:45`
- `POST /api/v1/private/orders/{id}/history` handled by `com.salesmanager.shop.store.api.v1.order.OrderStatusHistoryApi#create` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:59`
- `GET /api/v1/private/orders/{id}/payment/nextTransaction` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#nextTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:183`
- `GET /api/v1/private/orders/{id}/payment/transactions` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#listTransactions` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:204`
- `POST /api/v1/private/orders/{id}/refund` handled by `com.salesmanager.shop.store.api.v1.order.OrderPaymentApi#refundPayment` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:335`
- `PUT /api/v1/private/orders/{id}/status` handled by `com.salesmanager.shop.store.api.v1.order.OrderApi#updateOrderStatus` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:494`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:76`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:66`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:54`
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:74`
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:67`
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:58`
- [com.salesmanager.core.business.services.customer.CustomerService](/modules/com.salesmanager.core.business.services.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:56`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:80`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:70`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:60`
- [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:79`
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:68`
- [com.salesmanager.core.business.services.shipping.ShippingQuoteService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:58`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:86`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:73`
- [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:89`
- [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:77`
- [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:82`
- [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:60`
- [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:39`
- [com.salesmanager.shop.store.controller.order.facade.v1.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.v1.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:77`
- [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:62`
- [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:50`
- [com.salesmanager.shop.store.security.services.CredentialsService](/modules/com.salesmanager.shop.store.security.services.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:98`
- [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:95`
- [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:85`
- [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:42`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:64`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:52`

## Calls
- `OrderApi.checkout` calls [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `CustomerFacade.checkIfUserExists`, `CustomerFacade.populateCustomerModel` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:437`
- `OrderApi.checkout` calls [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `OrderFacade.processOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:375`
- `OrderApi.checkout` calls [com.salesmanager.shop.store.controller.order.facade.v1.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.v1.md) `OrderFacade.orderConfirmation` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:380`
- `OrderApi.checkout` calls [com.salesmanager.shop.store.security.services.CredentialsService](/modules/com.salesmanager.shop.store.security.services.md) `CredentialsService.validateCredentials` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:427`
- `OrderApi.get` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:273`
- `OrderApi.list` calls [com.salesmanager.shop.populator.customer.ReadableCustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `ReadableCustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:139`
- `OrderApi.list` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:245`
- `OrderApi.updateOrderCustomer` calls [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `OrderFacade.updateOrderCustomre` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:490`
- `OrderApi.updateOrderCustomer` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:485`
- `OrderApi.updateOrderStatus` calls [com.salesmanager.core.model.order.orderstatus.OrderStatus](/modules/com.salesmanager.core.model.order.orderstatus.md) `OrderStatus.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:515`
- `OrderApi.updateOrderStatus` calls [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `OrderFacade.updateOrderStatus` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:517`
- `OrderApi.updateOrderStatus` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderApi.java:506`
- `OrderPaymentApi.init` calls [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `PaymentService.initTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:107`
- `OrderPaymentApi.init` calls [com.salesmanager.shop.populator.order.transaction.PersistablePaymentPopulator](/modules/com.salesmanager.shop.populator.order.transaction.md) `PersistablePaymentPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:105`
- `OrderPaymentApi.init` calls [com.salesmanager.shop.populator.order.transaction.ReadableTransactionPopulator](/modules/com.salesmanager.shop.populator.order.transaction.md) `ReadableTransactionPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:114`
- `OrderPaymentApi.listTransactions` calls [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `OrderFacade.listTransactions` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:221`
- `OrderPaymentApi.listTransactions` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:216`
- `OrderPaymentApi.nextTransaction` calls [com.salesmanager.core.model.payments.TransactionType](/modules/com.salesmanager.core.model.payments.md) `TransactionType.name` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:200`
- `OrderPaymentApi.nextTransaction` calls [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `OrderFacade.nextTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:199`
- `OrderPaymentApi.nextTransaction` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderPaymentApi.java:195`
- `OrderShippingApi.shipping` calls [com.salesmanager.shop.populator.order.ReadableShippingSummaryPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableShippingSummaryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderShippingApi.java:127`
- `OrderStatusHistoryApi.create` calls [com.salesmanager.shop.store.controller.order.facade.OrderFacade](/modules/com.salesmanager.shop.store.controller.order.facade.md) `OrderFacade.createOrderStatus` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:72`
- `OrderStatusHistoryApi.create` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:66`
- `OrderStatusHistoryApi.list` calls [com.salesmanager.shop.utils.AuthorizationUtils](/modules/com.salesmanager.shop.utils.md) `AuthorizationUtils.authenticatedUser`, `AuthorizationUtils.authorizeUser` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderStatusHistoryApi.java:51`
- `OrderTotalApi.calculateTotal` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.caculateOrderTotal` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:205`
- `OrderTotalApi.calculateTotal` calls [com.salesmanager.shop.populator.order.ReadableOrderSummaryPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderSummaryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:211`
- `OrderTotalApi.payment` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.caculateOrderTotal` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:136`
- `OrderTotalApi.payment` calls [com.salesmanager.shop.populator.order.ReadableOrderSummaryPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderSummaryPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/order/OrderTotalApi.java:142`

## Tests
- `com.salesmanager.test.shop.integration.order.OrderApiIntegrationTest`
