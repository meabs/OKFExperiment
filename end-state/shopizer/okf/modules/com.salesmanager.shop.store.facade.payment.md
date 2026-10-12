---
type: Code Module
title: "com.salesmanager.shop.store.facade.payment"
description: "com.salesmanager.shop.store.facade.payment: PaymentConfigurationFacadeImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java"
    sha256: "f72d9122fc65bd3ed2c7422ed11f09a75a165c79be835fe16360d9f55c131ec6"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.facade.payment

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java`

## Types
- `PaymentConfigurationFacadeImpl` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:21`

## Fields
- `PaymentConfigurationFacadeImpl.paymentService: PaymentService` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:26`

## Functions and methods
- `PaymentConfigurationFacadeImpl.configurations(MerchantStore) -> List<ReadableConfiguration>` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:28`
- `PaymentConfigurationFacadeImpl.configuration(String, MerchantStore) -> ReadableConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:45`
- `PaymentConfigurationFacadeImpl.saveConfiguration(PersistableConfiguration, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:70`
- `PaymentConfigurationFacadeImpl.deleteConfiguration(String, MerchantStore) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:76`
- `PaymentConfigurationFacadeImpl.configuration(IntegrationConfiguration, MerchantStore) -> ReadableConfiguration` `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:83`

## Depends on
- [com.salesmanager.core.business.services.payments.PaymentService](/modules/com.salesmanager.core.business.services.payments.md) `sm-shop/src/main/java/com/salesmanager/shop/store/facade/payment/PaymentConfigurationFacadeImpl.java:25`
