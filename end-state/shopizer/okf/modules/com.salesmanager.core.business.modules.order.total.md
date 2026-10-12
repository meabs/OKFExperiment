---
type: Code Module
title: "com.salesmanager.core.business.modules.order.total"
description: "com.salesmanager.core.business.modules.order.total: ManufacturerShippingCodeOrderTotalModuleImpl, OrderTotalInputParameters, OrderTotalResponse, PromoCodeCalculatorModule"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java"
    sha256: "a5235e7c8e14d1bf8d3b7919a900fa3315908f7dfa7cf2b06d668558abe0d1ea"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java"
    sha256: "35394940f80a76f732504a0b414a2dcc93b0da665177f355c2930c48b8f76479"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java"
    sha256: "798d4d441871912001803b103e0cbb12081587a7c9181a671a5ab7ca912704dd"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java"
    sha256: "84adc9e2c311c51b8138b945d9ddea8e4f40f678b420c03018c1d8473ce12901"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.order.total

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java`

## Types
- `ManufacturerShippingCodeOrderTotalModuleImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:29`
- `OrderTotalInputParameters` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:10`
- `OrderTotalResponse` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:3`
- `PromoCodeCalculatorModule` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:26`

## Fields
- `ManufacturerShippingCodeOrderTotalModuleImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:32`
- `ManufacturerShippingCodeOrderTotalModuleImpl.name: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:34`
- `ManufacturerShippingCodeOrderTotalModuleImpl.code: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:35`
- `ManufacturerShippingCodeOrderTotalModuleImpl.pricingService: PricingService` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:45`
- `OrderTotalInputParameters.discount: Double` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:12`
- `OrderTotalInputParameters.totalCode: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:13`
- `OrderTotalInputParameters.productId: long` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:16`
- `OrderTotalInputParameters.itemManufacturerCode: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:17`
- `OrderTotalInputParameters.itemCategoryCode: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:18`
- `OrderTotalInputParameters.shippingMethod: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:19`
- `OrderTotalInputParameters.promoCode: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:20`
- `OrderTotalInputParameters.date: Date` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:21`
- `OrderTotalResponse.discount: Double` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:5`
- `OrderTotalResponse.expiration: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:6`
- `PromoCodeCalculatorModule.droolsBeanFactory: DroolsBeanFactory` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:31`
- `PromoCodeCalculatorModule.pricingService: PricingService` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:34`
- `PromoCodeCalculatorModule.name: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:36`
- `PromoCodeCalculatorModule.code: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:37`

## Functions and methods
- `ManufacturerShippingCodeOrderTotalModuleImpl.getPricingService() -> PricingService` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:49`
- `ManufacturerShippingCodeOrderTotalModuleImpl.setPricingService(PricingService) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:53`
- `ManufacturerShippingCodeOrderTotalModuleImpl.caculateProductPiceVariation(OrderSummary, ShoppingCartItem, Product, Customer, MerchantStore) -> OrderTotal` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:57`
- `ManufacturerShippingCodeOrderTotalModuleImpl.getName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:129`
- `ManufacturerShippingCodeOrderTotalModuleImpl.setName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:134`
- `ManufacturerShippingCodeOrderTotalModuleImpl.getCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:139`
- `ManufacturerShippingCodeOrderTotalModuleImpl.setCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:144`
- `OrderTotalInputParameters.getDiscount() -> Double` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:25`
- `OrderTotalInputParameters.setDiscount(Double) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:28`
- `OrderTotalInputParameters.getTotalCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:31`
- `OrderTotalInputParameters.setTotalCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:34`
- `OrderTotalInputParameters.getItemManufacturerCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:37`
- `OrderTotalInputParameters.setItemManufacturerCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:40`
- `OrderTotalInputParameters.getItemCategoryCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:43`
- `OrderTotalInputParameters.setItemCategoryCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:46`
- `OrderTotalInputParameters.getProductId() -> long` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:49`
- `OrderTotalInputParameters.setProductId(long) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:52`
- `OrderTotalInputParameters.getShippingMethod() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:55`
- `OrderTotalInputParameters.setShippingMethod(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:58`
- `OrderTotalInputParameters.getPromoCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:61`
- `OrderTotalInputParameters.setPromoCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:64`
- `OrderTotalInputParameters.getDate() -> Date` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:67`
- `OrderTotalInputParameters.setDate(Date) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalInputParameters.java:70`
- `OrderTotalResponse.getDiscount() -> Double` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:8`
- `OrderTotalResponse.setDiscount(Double) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:12`
- `OrderTotalResponse.getExpiration() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:16`
- `OrderTotalResponse.setExpiration(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/OrderTotalResponse.java:20`
- `PromoCodeCalculatorModule.getName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:39`
- `PromoCodeCalculatorModule.setName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:45`
- `PromoCodeCalculatorModule.getCode() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:51`
- `PromoCodeCalculatorModule.setCode(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:57`
- `PromoCodeCalculatorModule.caculateProductPiceVariation(OrderSummary, ShoppingCartItem, Product, Customer, MerchantStore) -> OrderTotal` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:62`

## Depends on
- [com.salesmanager.core.business.configuration.DroolsBeanFactory](/modules/com.salesmanager.core.business.configuration.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:30`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:45`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:33`

## Calls
- `ManufacturerShippingCodeOrderTotalModuleImpl.caculateProductPiceVariation` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculateProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/ManufacturerShippingCodeOrderTotalModuleImpl.java:96`
- `PromoCodeCalculatorModule.caculateProductPiceVariation` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculateProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/total/PromoCodeCalculatorModule.java:96`
