---
type: Code Module
title: "com.salesmanager.core.modules.integration.payment.model"
description: "com.salesmanager.core.modules.integration.payment.model: validateModuleConfiguration, initTransaction, authorize, capture"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java"
    sha256: "230055736d987e46da75f91ce4881d43ebc601e307d2de30fc308c48551aac50"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.modules.integration.payment.model

Source: `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java`

## Types
- `PaymentModule` (interface) `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:16`

## Functions and methods
- `PaymentModule.validateModuleConfiguration(IntegrationConfiguration, MerchantStore) -> void` `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:18`
- `PaymentModule.initTransaction(MerchantStore, Customer, BigDecimal, Payment, IntegrationConfiguration, IntegrationModule) -> Transaction` `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:33`
- `PaymentModule.authorize(MerchantStore, Customer, List<ShoppingCartItem>, BigDecimal, Payment, IntegrationConfiguration, IntegrationModule) -> Transaction` `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:37`
- `PaymentModule.capture(MerchantStore, Customer, Order, Transaction, IntegrationConfiguration, IntegrationModule) -> Transaction` `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:42`
- `PaymentModule.authorizeAndCapture(MerchantStore, Customer, List<ShoppingCartItem>, BigDecimal, Payment, IntegrationConfiguration, IntegrationModule) -> Transaction` `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:46`
- `PaymentModule.refund(boolean, MerchantStore, Transaction, Order, BigDecimal, IntegrationConfiguration, IntegrationModule) -> Transaction` `sm-core-modules/src/main/java/com/salesmanager/core/modules/integration/payment/model/PaymentModule.java:50`
