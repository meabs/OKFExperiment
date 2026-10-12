---
type: Code Module
title: "com.salesmanager.shop.store.controller.order.facade"
description: "com.salesmanager.shop.store.controller.order.facade: OrderFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java"
    sha256: "74696f7af0dbe9df3cf36bc19ad7941ca52e765ccc4b45bc92b8788b51420740"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java"
    sha256: "622bc6bf33f68fea6c0a151d9bd9034cece4dcb2fb4feaa559ea1620ed3322a4"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.controller.order.facade

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java`

## Types
- `OrderFacade` (interface) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:31`
- `OrderFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:113`

## Fields
- `OrderFacadeImpl.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:116`
- `OrderFacadeImpl.orderService: OrderService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:119`
- `OrderFacadeImpl.productService: ProductService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:121`
- `OrderFacadeImpl.productAttributeService: ProductAttributeService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:123`
- `OrderFacadeImpl.shoppingCartService: ShoppingCartService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:125`
- `OrderFacadeImpl.digitalProductService: DigitalProductService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:127`
- `OrderFacadeImpl.shippingService: ShippingService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:129`
- `OrderFacadeImpl.customerFacade: CustomerFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:131`
- `OrderFacadeImpl.pricingService: PricingService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:133`
- `OrderFacadeImpl.shoppingCartFacade: ShoppingCartFacade` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:135`
- `OrderFacadeImpl.shippingQuoteService: ShippingQuoteService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:137`
- `OrderFacadeImpl.coreConfiguration: CoreConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:139`
- `OrderFacadeImpl.paymentService: PaymentService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:141`
- `OrderFacadeImpl.countryService: CountryService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:143`
- `OrderFacadeImpl.zoneService: ZoneService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:145`
- `OrderFacadeImpl.persistableOrderApiPopulator: PersistableOrderApiPopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:149`
- `OrderFacadeImpl.readableOrderPopulator: ReadableOrderPopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:152`
- `OrderFacadeImpl.customerPopulator: CustomerPopulator` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:155`
- `OrderFacadeImpl.transactionService: TransactionService` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:158`
- `OrderFacadeImpl.emailTemplatesUtils: EmailTemplatesUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:161`
- `OrderFacadeImpl.messages: LabelUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:164`
- `OrderFacadeImpl.productPriceUtils: ProductPriceUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:167`
- `OrderFacadeImpl.imageUtils: ImageFilePath` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:171`

## Functions and methods
- `OrderFacade.initializeOrder(MerchantStore, Customer, ShoppingCart, Language) -> ShopOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:33`
- `OrderFacade.refreshOrder(ShopOrder, MerchantStore, Customer, ShoppingCart, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:34`
- `OrderFacade.calculateOrderTotal(MerchantStore, ShopOrder, Language) -> OrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:36`
- `OrderFacade.calculateOrderTotal(MerchantStore, com.salesmanager.shop.model.order.v0.PersistableOrder, Language) -> OrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:38`
- `OrderFacade.processOrder(ShopOrder, Customer, MerchantStore, Language) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:41`
- `OrderFacade.processOrder(ShopOrder, Customer, Transaction, MerchantStore, Language) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:43`
- `OrderFacade.processOrder(com.salesmanager.shop.model.order.v1.PersistableOrder, Customer, MerchantStore, Language, Locale) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:45`
- `OrderFacade.initEmptyCustomer(MerchantStore) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:50`
- `OrderFacade.getShipToCountry(MerchantStore, Language) -> List<Country>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:51`
- `OrderFacade.getShippingQuote(PersistableCustomer, ShoppingCart, ShopOrder, MerchantStore, Language) -> ShippingQuote` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:63`
- `OrderFacade.getShippingQuote(Customer, ShoppingCart, com.salesmanager.shop.model.order.v0.PersistableOrder, MerchantStore, Language) -> ShippingQuote` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:66`
- `OrderFacade.getShippingQuote(Customer, ShoppingCart, MerchantStore, Language) -> ShippingQuote` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:69`
- `OrderFacade.getShippingSummary(ShippingQuote, MerchantStore, Language) -> ShippingSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:79`
- `OrderFacade.validateOrder(ShopOrder, BindingResult, Map<String, String>, MerchantStore, Locale) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:90`
- `OrderFacade.getReadableOrder(Long, MerchantStore, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:102`
- `OrderFacade.getReadableOrderHistory(Long, MerchantStore, Language) -> List<ReadableOrderStatusHistory>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:111`
- `OrderFacade.getReadableOrderList(MerchantStore, Customer, int, int, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:125`
- `OrderFacade.getReadableOrderList(OrderCriteria, MerchantStore) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:138`
- `OrderFacade.getCapturableOrderList(MerchantStore, Date, Date, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:150`
- `OrderFacade.captureOrder(MerchantStore, Order, Customer, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:162`
- `OrderFacade.nextTransaction(Long, MerchantStore) -> TransactionType` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:167`
- `OrderFacade.getReadableOrderList(MerchantStore, int, int, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:178`
- `OrderFacade.createOrderStatus(PersistableOrderStatusHistory, Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:187`
- `OrderFacade.updateOrderCustomre(Long, PersistableCustomer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:197`
- `OrderFacade.listTransactions(Long, MerchantStore) -> List<ReadableTransaction>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:199`
- `OrderFacade.updateOrderStatus(Order, OrderStatus, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacade.java:204`
- `OrderFacadeImpl.initializeOrder(MerchantStore, Customer, ShoppingCart, Language) -> ShopOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:173`
- `OrderFacadeImpl.calculateOrderTotal(MerchantStore, ShopOrder, Language) -> OrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:198`
- `OrderFacadeImpl.calculateOrderTotal(MerchantStore, com.salesmanager.shop.model.order.v0.PersistableOrder, Language) -> OrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:208`
- `OrderFacadeImpl.calculateOrderTotal(MerchantStore, Customer, com.salesmanager.shop.model.order.v0.PersistableOrder, Language) -> OrderTotalSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:232`
- `OrderFacadeImpl.persistableCustomer(Customer, MerchantStore, Language) -> PersistableCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:283`
- `OrderFacadeImpl.customer(PersistableCustomer, MerchantStore, Language) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:293`
- `OrderFacadeImpl.setOrderTotals(OrderEntity, OrderTotalSummary) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:300`
- `OrderFacadeImpl.processOrder(ShopOrder, Customer, MerchantStore, Language) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:319`
- `OrderFacadeImpl.processOrder(ShopOrder, Customer, Transaction, MerchantStore, Language) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:327`
- `OrderFacadeImpl.processOrderModel(ShopOrder, Customer, Transaction, MerchantStore, Language) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:345`
- `OrderFacadeImpl.orderCustomer(Customer, Order, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:567`
- `OrderFacadeImpl.initEmptyCustomer(MerchantStore) -> Customer` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:581`
- `OrderFacadeImpl.refreshOrder(ShopOrder, MerchantStore, Customer, ShoppingCart, Language) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:604`
- `OrderFacadeImpl.getShippingQuote(PersistableCustomer, ShoppingCart, ShopOrder, MerchantStore, Language) -> ShippingQuote` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:622`
- `OrderFacadeImpl.validatePostalCode(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:663`
- `OrderFacadeImpl.getShipToCountry(MerchantStore, Language) -> List<Country>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:672`
- `OrderFacadeImpl.getShippingSummary(ShippingQuote, MerchantStore, Language) -> ShippingSummary` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:683`
- `OrderFacadeImpl.validateOrder(ShopOrder, BindingResult, Map<String, String>, MerchantStore, Locale) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:706`
- `OrderFacadeImpl.getReadableOrderList(MerchantStore, Customer, int, int, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:922`
- `OrderFacadeImpl.getReadableOrderList(OrderCriteria, MerchantStore) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:935`
- `OrderFacadeImpl.getShippingQuote(Customer, ShoppingCart, com.salesmanager.shop.model.order.v0.PersistableOrder, MerchantStore, Language) -> ShippingQuote` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:974`
- `OrderFacadeImpl.populateOrderList(OrderList, MerchantStore, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1007`
- `OrderFacadeImpl.setOrderProductList(Order, Locale, MerchantStore, Language, com.salesmanager.shop.model.order.v0.ReadableOrder) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1041`
- `OrderFacadeImpl.getReadableOrderList(OrderCriteria, MerchantStore, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1064`
- `OrderFacadeImpl.getReadableOrderList(MerchantStore, int, int, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1095`
- `OrderFacadeImpl.getReadableOrder(Long, MerchantStore, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1106`
- `OrderFacadeImpl.getShippingQuote(Customer, ShoppingCart, MerchantStore, Language) -> ShippingQuote` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1151`
- `OrderFacadeImpl.processOrder(com.salesmanager.shop.model.order.v1.PersistableOrder, Customer, MerchantStore, Language, Locale) -> Order` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1195`
- `OrderFacadeImpl.notify(Order, Customer, MerchantStore, Language, Locale) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1361`
- `OrderFacadeImpl.getCapturableOrderList(MerchantStore, Date, Date, Language) -> com.salesmanager.shop.model.order.v0.ReadableOrderList` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1382`
- `OrderFacadeImpl.captureOrder(MerchantStore, Order, Customer, Language) -> ReadableTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1415`
- `OrderFacadeImpl.getReadableOrderHistory(Long, MerchantStore, Language) -> List<ReadableOrderStatusHistory>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1431`
- `OrderFacadeImpl.mapToReadbleOrderStatusHistory(OrderStatusHistory) -> ReadableOrderStatusHistory` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1447`
- `OrderFacadeImpl.createOrderStatus(PersistableOrderStatusHistory, Long, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1458`
- `OrderFacadeImpl.updateOrderCustomre(Long, PersistableCustomer, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1486`
- `OrderFacadeImpl.convertBilling(Address) -> Billing` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1512`
- `OrderFacadeImpl.convertDelivery(Address) -> Delivery` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1533`
- `OrderFacadeImpl.nextTransaction(Long, MerchantStore) -> TransactionType` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1554`
- `OrderFacadeImpl.listTransactions(Long, MerchantStore) -> List<ReadableTransaction>` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1587`
- `OrderFacadeImpl.updateOrderStatus(Order, OrderStatus, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1624`

## Depends on
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:132`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:120`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductAttributeService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:122`
- [com.salesmanager.core.business.services.catalog.product.file.DigitalProductService](/modules/com.salesmanager.core.business.services.catalog.product.file.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:126`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:118`
- [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:140`
- [com.salesmanager.core.business.services.payments.TransactionService](/modules/com.salesmanager.core.business.services.payments.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:157`
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:142`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:144`
- [com.salesmanager.core.business.services.shipping.ShippingQuoteService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:136`
- [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:128`
- [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:124`
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:138`
- [com.salesmanager.core.business.utils.ProductPriceUtils](/modules/com.salesmanager.core.business.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:166`
- [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:154`
- [com.salesmanager.shop.populator.order.PersistableOrderApiPopulator](/modules/com.salesmanager.shop.populator.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:148`
- [com.salesmanager.shop.populator.order.ReadableOrderPopulator](/modules/com.salesmanager.shop.populator.order.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:151`
- [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:130`
- [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:134`
- [com.salesmanager.shop.utils.EmailTemplatesUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:160`
- [com.salesmanager.shop.utils.ImageFilePath](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:169`
- [com.salesmanager.shop.utils.LabelUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:163`

## Calls
- `OrderFacadeImpl.calculateOrderTotal` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.caculateOrderTotal` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:272`
- `OrderFacadeImpl.calculateOrderTotal` calls [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `ShoppingCartService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:266`
- `OrderFacadeImpl.calculateOrderTotal` calls [com.salesmanager.shop.populator.order.ShoppingCartItemPopulator](/modules/com.salesmanager.shop.populator.order.md) `ShoppingCartItemPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:221`
- `OrderFacadeImpl.captureOrder` calls [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `PaymentService.processCapturePayment` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1418`
- `OrderFacadeImpl.captureOrder` calls [com.salesmanager.shop.populator.order.transaction.ReadableTransactionPopulator](/modules/com.salesmanager.shop.populator.order.transaction.md) `ReadableTransactionPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1425`
- `OrderFacadeImpl.createOrderStatus` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.addOrderStatusHistory` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1478`
- `OrderFacadeImpl.customer` calls [com.salesmanager.shop.populator.customer.CustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `CustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:295`
- `OrderFacadeImpl.getCapturableOrderList` calls [com.salesmanager.shop.populator.order.ReadableOrderPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1404`
- `OrderFacadeImpl.getReadableOrder` calls [com.salesmanager.shop.populator.order.ReadableOrderPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1128`
- `OrderFacadeImpl.getReadableOrder` calls [com.salesmanager.shop.populator.order.ReadableOrderProductPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderProductPopulator.populate`, `ReadableOrderProductPopulator.setimageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1139`
- `OrderFacadeImpl.getReadableOrderList` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.listByStore` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1067`
- `OrderFacadeImpl.getReadableOrderList` calls [com.salesmanager.shop.populator.order.ReadableOrderPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:955`
- `OrderFacadeImpl.getShippingQuote` calls [com.salesmanager.core.business.services.shoppingcart.ShoppingCartService](/modules/com.salesmanager.core.business.services.shoppingcart.md) `ShoppingCartService.createShippingProduct` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:627`
- `OrderFacadeImpl.listTransactions` calls [com.salesmanager.core.business.services.payments.TransactionService](/modules/com.salesmanager.core.business.services.payments.md) `TransactionService.listTransactions` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1599`
- `OrderFacadeImpl.listTransactions` calls [com.salesmanager.shop.populator.order.transaction.ReadableTransactionPopulator](/modules/com.salesmanager.shop.populator.order.transaction.md) `ReadableTransactionPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1611`
- `OrderFacadeImpl.mapToReadbleOrderStatusHistory` calls [com.salesmanager.shop.utils.DateUtil](/modules/com.salesmanager.shop.utils.md) `DateUtil.formatLongDate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1450`
- `OrderFacadeImpl.nextTransaction` calls [com.salesmanager.core.business.services.payments.TransactionService](/modules/com.salesmanager.core.business.services.payments.md) `TransactionService.lastTransaction` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1565`
- `OrderFacadeImpl.notify` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.hasDownloadFiles` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1368`
- `OrderFacadeImpl.notify` calls [com.salesmanager.shop.utils.EmailTemplatesUtils](/modules/com.salesmanager.shop.utils.md) `EmailTemplatesUtils.sendOrderDownloadEmail`, `EmailTemplatesUtils.sendOrderEmail` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1369`
- `OrderFacadeImpl.persistableCustomer` calls [com.salesmanager.shop.populator.customer.PersistableCustomerPopulator](/modules/com.salesmanager.shop.populator.customer.md) `PersistableCustomerPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:287`
- `OrderFacadeImpl.populateOrderList` calls [com.salesmanager.shop.populator.order.ReadableOrderPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1026`
- `OrderFacadeImpl.processOrder` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.caculateOrderTotal`, `OrderService.processOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1273`
- `OrderFacadeImpl.processOrder` calls [com.salesmanager.shop.populator.order.OrderProductPopulator](/modules/com.salesmanager.shop.populator.order.md) `OrderProductPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1231`
- `OrderFacadeImpl.processOrder` calls [com.salesmanager.shop.populator.order.PersistableOrderApiPopulator](/modules/com.salesmanager.shop.populator.order.md) `PersistableOrderApiPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1209`
- `OrderFacadeImpl.processOrder` calls [com.salesmanager.shop.populator.order.transaction.PersistablePaymentPopulator](/modules/com.salesmanager.shop.populator.order.transaction.md) `PersistablePaymentPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1311`
- `OrderFacadeImpl.processOrder` calls [com.salesmanager.shop.store.controller.customer.facade.CustomerFacade](/modules/com.salesmanager.shop.store.controller.customer.facade.md) `CustomerFacade.checkIfUserExists` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1319`
- `OrderFacadeImpl.processOrder` calls [com.salesmanager.shop.store.controller.shoppingCart.facade.ShoppingCartFacade](/modules/com.salesmanager.shop.store.controller.shoppingCart.facade.md) `ShoppingCartFacade.saveOrUpdateShoppingCart` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1333`
- `OrderFacadeImpl.processOrderModel` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.processOrder` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:551`
- `OrderFacadeImpl.processOrderModel` calls [com.salesmanager.core.business.utils.CreditCardUtils](/modules/com.salesmanager.core.business.utils.md) `CreditCardUtils.maskCardNumber` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:520`
- `OrderFacadeImpl.processOrderModel` calls [com.salesmanager.core.model.payments.PaymentType](/modules/com.salesmanager.core.model.payments.md) `PaymentType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:361`
- `OrderFacadeImpl.processOrderModel` calls [com.salesmanager.shop.populator.order.OrderProductPopulator](/modules/com.salesmanager.shop.populator.order.md) `OrderProductPopulator.populate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:415`
- `OrderFacadeImpl.setOrderProductList` calls [com.salesmanager.shop.populator.order.ReadableOrderProductPopulator](/modules/com.salesmanager.shop.populator.order.md) `ReadableOrderProductPopulator.populate`, `ReadableOrderProductPopulator.setimageUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1052`
- `OrderFacadeImpl.updateOrderCustomre` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.saveOrUpdate` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1504`
- `OrderFacadeImpl.updateOrderStatus` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.addOrderStatusHistory` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1642`
- `OrderFacadeImpl.updateOrderStatus` calls [com.salesmanager.core.model.order.orderstatus.OrderStatus](/modules/com.salesmanager.core.model.order.orderstatus.md) `OrderStatus.name` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:1635`
- `OrderFacadeImpl.validateOrder` calls [com.salesmanager.core.business.services.shipping.ShippingService](/modules/com.salesmanager.core.business.services.shipping.md) `ShippingService.requiresShipping` `sm-shop/src/main/java/com/salesmanager/shop/store/controller/order/facade/OrderFacadeImpl.java:867`
