---
type: Code Module
title: "com.salesmanager.core.business.repositories.order"
description: "com.salesmanager.core.business.repositories.order: OrderRepositoryImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepository.java"
    sha256: "321896fad876be224f5d6bb7482baeef2a794507a7df270c8085c8b798cb9a23"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryCustom.java"
    sha256: "c6eb734d04d6f3791b91b42af48b8b49e63010e624fc67fd68c5489209b45cd7"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java"
    sha256: "154a12c8922f1af91cc0910373043d8f8fdb7495f7934b15d4da349ae6226692"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderStatusHistoryRepository.java"
    sha256: "8ca33a33d03636332a9804f4080976c2f3fa07b66bf805e8915041f055534326"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderTotalRepository.java"
    sha256: "ff439d272f9710d86fe439470d703a4203672426e339712d3f5c7e72703f2884"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.order

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryCustom.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderStatusHistoryRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderTotalRepository.java`

## Types
- `OrderRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository`, [com.salesmanager.core.business.repositories.order.OrderRepositoryCustom](/modules/com.salesmanager.core.business.repositories.order.md) `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepository.java:8`
- `OrderRepositoryCustom` (interface) `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryCustom.java:10`
- `OrderRepositoryImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:18`
- `OrderStatusHistoryRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderStatusHistoryRepository.java:9`
- `OrderTotalRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderTotalRepository.java:7`

## Fields
- `OrderRepositoryImpl.em: EntityManager` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:22`

## Functions and methods
- `OrderRepository.findOne(Long, Integer) -> Order` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepository.java:10`
- `OrderRepositoryCustom.listByStore(MerchantStore, OrderCriteria) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryCustom.java:12`
- `OrderRepositoryCustom.listOrders(MerchantStore, OrderCriteria) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryCustom.java:13`
- `OrderRepositoryImpl.listByStore(MerchantStore, OrderCriteria) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:27`
- `OrderRepositoryImpl.listOrders(MerchantStore, OrderCriteria) -> OrderList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:137`
- `OrderRepositoryImpl.like(String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:263`
- `OrderStatusHistoryRepository.findByOrderId(Long) -> List<OrderStatusHistory>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderStatusHistoryRepository.java:11`

## Calls
- `OrderRepositoryImpl.listOrders` calls [com.salesmanager.core.business.utils.RepositoryHelper](/modules/com.salesmanager.core.business.utils.md) `RepositoryHelper.paginateQuery` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:251`
- `OrderRepositoryImpl.listOrders` calls [com.salesmanager.core.model.order.orderstatus.OrderStatus](/modules/com.salesmanager.core.model.order.orderstatus.md) `OrderStatus.valueOf` `sm-core/src/main/java/com/salesmanager/core/business/repositories/order/OrderRepositoryImpl.java:233`
