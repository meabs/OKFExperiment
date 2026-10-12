---
type: Code Module
title: "com.salesmanager.shop.store.api.v1.payment"
description: "com.salesmanager.shop.store.api.v1.payment: PaymentApi; 3 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java"
    sha256: "6f9b7a4578f335582f3f635fd9932ff8321fc73a7f3de7a32ef1110aabf64e6d"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v1.payment

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java`

## Types
- `PaymentApi` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:43`

## Fields
- `PaymentApi.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:49`
- `PaymentApi.paymentService: PaymentService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:52`

## Functions and methods
- `PaymentApi.paymentModules(MerchantStore, Language) -> List<IntegrationModuleSummaryEntity>` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:61`
- `PaymentApi.configure(IntegrationModuleConfiguration, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:83`
- `PaymentApi.paymentModule(String, MerchantStore, Language) -> IntegrationModuleConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:134`
- `PaymentApi.integrationModule(IntegrationModule, Map<String, IntegrationConfiguration>) -> IntegrationModuleSummaryEntity` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:184`

## HTTP routes
- `GET /api/v1/private/modules/payment` handled by `com.salesmanager.shop.store.api.v1.payment.PaymentApi#paymentModules` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:61`
- `POST /api/v1/private/modules/payment` handled by `com.salesmanager.shop.store.api.v1.payment.PaymentApi#configure` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:83`
- `GET /api/v1/private/modules/payment/{code}` handled by `com.salesmanager.shop.store.api.v1.payment.PaymentApi#paymentModule` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:134`

## Depends on
- [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:51`

## Calls
- `PaymentApi.configure` calls [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `PaymentService.savePaymentModuleConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v1/payment/PaymentApi.java:118`
