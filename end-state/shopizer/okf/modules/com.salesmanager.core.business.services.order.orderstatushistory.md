---
type: Code Module
title: "com.salesmanager.core.business.services.order.orderstatushistory"
description: "com.salesmanager.core.business.services.order.orderstatushistory: OrderStatusHistoryServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryService.java"
    sha256: "e245a22eb529d6ed59f91adb70c572c9dab7e9a4594375b89d368de60054e54a"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java"
    sha256: "178b27f845b597bc0c90710439f1925a02d09ffd6ddd54a9c33687ba72f38c76"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.order.orderstatushistory

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java`

## Types
- `OrderStatusHistoryService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryService.java:8`
- `OrderStatusHistoryServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java:11`

## Fields
- `OrderStatusHistoryServiceImpl.orderStatusHistoryRepository: OrderStatusHistoryRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java:14`

## Functions and methods
- `OrderStatusHistoryService.findByOrder(Order) -> List<OrderStatusHistory>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryService.java:9`
- `OrderStatusHistoryServiceImpl.findByOrder(Order) -> List<OrderStatusHistory>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java:16`

## Depends on
- [com.salesmanager.core.business.repositories.order.OrderStatusHistoryRepository](/modules/com.salesmanager.core.business.repositories.order.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java:13`

## Calls
- `OrderStatusHistoryServiceImpl.findByOrder` calls [com.salesmanager.core.business.repositories.order.OrderStatusHistoryRepository](/modules/com.salesmanager.core.business.repositories.order.md) `OrderStatusHistoryRepository.findByOrderId` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderstatushistory/OrderStatusHistoryServiceImpl.java:18`
