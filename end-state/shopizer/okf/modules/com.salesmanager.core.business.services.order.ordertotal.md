---
type: Code Module
title: "com.salesmanager.core.business.services.order.ordertotal"
description: "com.salesmanager.core.business.services.order.ordertotal: OrderTotalServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalService.java"
    sha256: "360548ff84e2c9382fbb640b4067a693898790c9b2d8bd6e0144a1693636d0de"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java"
    sha256: "5695ce64768a98a0c2790eb9708eba2470c7413367f988dfb9ac14264c188b87"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.order.ordertotal

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java`

## Types
- `OrderTotalService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalService.java:15`
- `OrderTotalServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java:25`

## Fields
- `OrderTotalServiceImpl.orderTotalPostProcessors: List<OrderTotalPostProcessorModule>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java:30`
- `OrderTotalServiceImpl.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java:33`

## Functions and methods
- `OrderTotalService.findOrderTotalVariation(OrderSummary, Customer, MerchantStore, Language) -> OrderTotalVariation` `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalService.java:17`
- `OrderTotalServiceImpl.findOrderTotalVariation(OrderSummary, Customer, MerchantStore, Language) -> OrderTotalVariation` `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java:36`

## Depends on
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java:32`
- [com.salesmanager.core.modules.order.total.OrderTotalPostProcessorModule](/modules/com.salesmanager.core.modules.order.total.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/ordertotal/OrderTotalServiceImpl.java:28`
