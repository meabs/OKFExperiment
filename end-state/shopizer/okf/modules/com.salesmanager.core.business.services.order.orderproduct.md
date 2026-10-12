---
type: Code Module
title: "com.salesmanager.core.business.services.order.orderproduct"
description: "com.salesmanager.core.business.services.order.orderproduct: OrderProductDownloadServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadService.java"
    sha256: "d26656dbcd255bcf7d0457a78d496e30f09a9ef5ce0cc5d7cbe47fd7bd69a597"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java"
    sha256: "3a6f5e8a5ae8ffa9fffe88bb08c80cae70b8110129ad9ea2e448e5e1f793ce64"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.order.orderproduct

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java`

## Types
- `OrderProductDownloadService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadService.java:9`
- `OrderProductDownloadServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java:18`

## Fields
- `OrderProductDownloadServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java:21`
- `OrderProductDownloadServiceImpl.orderProductDownloadRepository: OrderProductDownloadRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java:24`

## Functions and methods
- `OrderProductDownloadService.getByOrderId(Long) -> List<OrderProductDownload>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadService.java:16`
- `OrderProductDownloadServiceImpl.getByOrderId(Long) -> List<OrderProductDownload>` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java:32`

## Depends on
- [com.salesmanager.core.business.repositories.order.orderproduct.OrderProductDownloadRepository](/modules/com.salesmanager.core.business.repositories.order.orderproduct.md) `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java:24`

## Calls
- `OrderProductDownloadServiceImpl.getByOrderId` calls [com.salesmanager.core.business.repositories.order.orderproduct.OrderProductDownloadRepository](/modules/com.salesmanager.core.business.repositories.order.orderproduct.md) `OrderProductDownloadRepository.findByOrderId` `sm-core/src/main/java/com/salesmanager/core/business/services/order/orderproduct/OrderProductDownloadServiceImpl.java:34`
