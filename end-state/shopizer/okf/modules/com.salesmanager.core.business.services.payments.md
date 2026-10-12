---
type: Code Module
title: "com.salesmanager.core.business.services.payments"
description: "com.salesmanager.core.business.services.payments: PaymentServiceImpl, TransactionServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java"
    sha256: "477ed09bfb927a6b54b5bc6b7dae29638eb7ad9858a451e1124f3ef3d3f7bd70"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java"
    sha256: "68b0790e019c1deba33849b87a71e5a2dfa1dc1d088062165c8b7d1ce5b6b105"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java"
    sha256: "73f3817ac2361f2d8428c3888d7377f2caaad7250e9f9279fafbc2eb1ec8a646"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java"
    sha256: "fd428c1120b741c15a983ada39fec399f9763bc9d7b8b79aa150935d1a438c8b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.payments

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java`

## Types
- `PaymentService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:20`
- `PaymentServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:52`
- `TransactionService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java:15`
- `TransactionServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:25`

## Fields
- `PaymentServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:56`
- `PaymentServiceImpl.merchantConfigurationService: MerchantConfigurationService` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:60`
- `PaymentServiceImpl.moduleConfigurationService: ModuleConfigurationService` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:63`
- `PaymentServiceImpl.transactionService: TransactionService` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:66`
- `PaymentServiceImpl.orderService: OrderService` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:69`
- `PaymentServiceImpl.coreConfiguration: CoreConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:72`
- `PaymentServiceImpl.paymentModules: Map<String,PaymentModule>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:76`
- `PaymentServiceImpl.encryption: Encryption` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:79`
- `TransactionServiceImpl.transactionRepository: TransactionRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:29`

## Functions and methods
- `PaymentService.getPaymentMethods(MerchantStore) -> List<IntegrationModule>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:22`
- `PaymentService.getPaymentModulesConfigured(MerchantStore) -> Map<String, IntegrationConfiguration>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:25`
- `PaymentService.processPayment(Customer, MerchantStore, Payment, List<ShoppingCartItem>, Order) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:28`
- `PaymentService.processRefund(Order, Customer, MerchantStore, BigDecimal) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:29`
- `PaymentService.getPaymentMethodByType(MerchantStore, String) -> IntegrationModule` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:38`
- `PaymentService.getPaymentMethodByCode(MerchantStore, String) -> IntegrationModule` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:48`
- `PaymentService.savePaymentModuleConfiguration(IntegrationConfiguration, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:57`
- `PaymentService.validateCreditCard(String, CreditCardType, String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:68`
- `PaymentService.getPaymentConfiguration(String, MerchantStore) -> IntegrationConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:79`
- `PaymentService.removePaymentModuleConfiguration(String, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:82`
- `PaymentService.processCapturePayment(Order, Customer, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:85`
- `PaymentService.initTransaction(Order, Customer, Payment, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:97`
- `PaymentService.initTransaction(Customer, Payment, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:107`
- `PaymentService.getAcceptedPaymentMethods(MerchantStore) -> List<PaymentMethod>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:109`
- `PaymentService.getPaymentModule(String) -> PaymentModule` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentService.java:118`
- `PaymentServiceImpl.getPaymentMethods(MerchantStore) -> List<IntegrationModule>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:81`
- `PaymentServiceImpl.getAcceptedPaymentMethods(MerchantStore) -> List<PaymentMethod>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:98`
- `PaymentServiceImpl.getPaymentMethodByType(MerchantStore, String) -> IntegrationModule` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:132`
- `PaymentServiceImpl.getPaymentMethodByCode(MerchantStore, String) -> IntegrationModule` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:146`
- `PaymentServiceImpl.getPaymentConfiguration(String, MerchantStore) -> IntegrationConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:161`
- `PaymentServiceImpl.getPaymentModulesConfigured(MerchantStore) -> Map<String,IntegrationConfiguration>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:184`
- `PaymentServiceImpl.savePaymentModuleConfiguration(IntegrationConfiguration, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:208`
- `PaymentServiceImpl.removePaymentModuleConfiguration(String, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:254`
- `PaymentServiceImpl.processPayment(Customer, MerchantStore, Payment, List<ShoppingCartItem>, Order) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:299`
- `PaymentServiceImpl.getPaymentModule(String) -> PaymentModule` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:399`
- `PaymentServiceImpl.processCapturePayment(Order, Customer, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:404`
- `PaymentServiceImpl.processRefund(Order, Customer, MerchantStore, BigDecimal) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:473`
- `PaymentServiceImpl.validateCreditCard(String, CreditCardType, String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:570`
- `PaymentServiceImpl.validateCreditCardDate(int, int) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:598`
- `PaymentServiceImpl.validateCreditCardNumber(String, CreditCardType) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:612`
- `PaymentServiceImpl.luhnValidate(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:671`
- `PaymentServiceImpl.initTransaction(Order, Customer, Payment, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:699`
- `PaymentServiceImpl.initTransaction(Customer, Payment, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:738`
- `TransactionService.getCapturableTransaction(Order) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java:23`
- `TransactionService.getRefundableTransaction(Order) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java:25`
- `TransactionService.listTransactions(Order) -> List<Transaction>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java:27`
- `TransactionService.listTransactions(Date, Date) -> List<Transaction>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java:29`
- `TransactionService.lastTransaction(Order, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionService.java:31`
- `TransactionServiceImpl.create(Transaction) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:37`
- `TransactionServiceImpl.listTransactions(Order) -> List<Transaction>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:51`
- `TransactionServiceImpl.lastTransaction(Order, MerchantStore) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:86`
- `TransactionServiceImpl.getCapturableTransaction(Order) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:118`
- `TransactionServiceImpl.getRefundableTransaction(Order) -> Transaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:148`
- `TransactionServiceImpl.listTransactions(Date, Date) -> List<Transaction>` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:202`

## Depends on
- [com.salesmanager.core.business.repositories.payments.TransactionRepository](/modules/com.salesmanager.core.business.repositories.payments.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:29`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:68`
- [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:59`
- [com.salesmanager.core.business.services.system.ModuleConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:62`
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:71`
- [com.salesmanager.core.modules.integration.payment.model.PaymentModule](/modules/com.salesmanager.core.modules.integration.payment.model.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:74`
- [com.salesmanager.core.modules.utils.Encryption](/modules/com.salesmanager.core.modules.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:78`

## Calls
- `PaymentServiceImpl.getAcceptedPaymentMethods` calls [com.salesmanager.core.model.payments.PaymentType](/modules/com.salesmanager.core.model.payments.md) `PaymentType.fromString` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:120`
- `PaymentServiceImpl.getPaymentModulesConfigured` calls [com.salesmanager.core.business.services.reference.loader.ConfigurationModulesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `ConfigurationModulesLoader.loadIntegrationConfigurations` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:196`
- `PaymentServiceImpl.getPaymentModulesConfigured` calls [com.salesmanager.core.modules.utils.Encryption](/modules/com.salesmanager.core.modules.utils.md) `Encryption.decrypt` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:195`
- `PaymentServiceImpl.initTransaction` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.save` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:775`
- `PaymentServiceImpl.initTransaction` calls [com.salesmanager.core.modules.integration.payment.model.PaymentModule](/modules/com.salesmanager.core.modules.integration.payment.model.md) `PaymentModule.initTransaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:735`
- `PaymentServiceImpl.processCapturePayment` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:454`
- `PaymentServiceImpl.processCapturePayment` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.addOrderStatusHistory`, `OrderService.saveOrUpdate` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:462`
- `PaymentServiceImpl.processCapturePayment` calls [com.salesmanager.core.modules.integration.payment.model.PaymentModule](/modules/com.salesmanager.core.modules.integration.payment.model.md) `PaymentModule.capture` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:449`
- `PaymentServiceImpl.processPayment` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:383`
- `PaymentServiceImpl.processPayment` calls [com.salesmanager.core.model.payments.TransactionType](/modules/com.salesmanager.core.model.payments.md) `TransactionType.equals`, `TransactionType.valueOf` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:367`
- `PaymentServiceImpl.processPayment` calls [com.salesmanager.core.modules.integration.payment.model.PaymentModule](/modules/com.salesmanager.core.modules.integration.payment.model.md) `PaymentModule.authorize`, `PaymentModule.authorizeAndCapture`, `PaymentModule.initTransaction` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:374`
- `PaymentServiceImpl.processRefund` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.create` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:527`
- `PaymentServiceImpl.processRefund` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.saveOrUpdate` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:565`
- `PaymentServiceImpl.processRefund` calls [com.salesmanager.core.modules.integration.payment.model.PaymentModule](/modules/com.salesmanager.core.modules.integration.payment.model.md) `PaymentModule.refund` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:525`
- `PaymentServiceImpl.removePaymentModuleConfiguration` calls [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `SalesManagerEntityService.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:285`
- `PaymentServiceImpl.removePaymentModuleConfiguration` calls [com.salesmanager.core.business.services.reference.loader.ConfigurationModulesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `ConfigurationModulesLoader.loadIntegrationConfigurations`, `ConfigurationModulesLoader.toJSONString` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:267`
- `PaymentServiceImpl.removePaymentModuleConfiguration` calls [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `MerchantConfigurationService.saveOrUpdate` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:276`
- `PaymentServiceImpl.removePaymentModuleConfiguration` calls [com.salesmanager.core.modules.utils.Encryption](/modules/com.salesmanager.core.modules.utils.md) `Encryption.decrypt`, `Encryption.encrypt` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:266`
- `PaymentServiceImpl.savePaymentModuleConfiguration` calls [com.salesmanager.core.business.services.reference.loader.ConfigurationModulesLoader](/modules/com.salesmanager.core.business.services.reference.loader.md) `ConfigurationModulesLoader.loadIntegrationConfigurations`, `ConfigurationModulesLoader.toJSONString` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:233`
- `PaymentServiceImpl.savePaymentModuleConfiguration` calls [com.salesmanager.core.business.services.system.MerchantConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `MerchantConfigurationService.saveOrUpdate` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:247`
- `PaymentServiceImpl.savePaymentModuleConfiguration` calls [com.salesmanager.core.modules.integration.payment.model.PaymentModule](/modules/com.salesmanager.core.modules.integration.payment.model.md) `PaymentModule.validateModuleConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:219`
- `PaymentServiceImpl.savePaymentModuleConfiguration` calls [com.salesmanager.core.modules.utils.Encryption](/modules/com.salesmanager.core.modules.utils.md) `Encryption.decrypt`, `Encryption.encrypt` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:231`
- `PaymentServiceImpl.validateCreditCardNumber` calls [com.salesmanager.core.model.payments.CreditCardType](/modules/com.salesmanager.core.model.payments.md) `CreditCardType.name` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/PaymentServiceImpl.java:623`
- `TransactionServiceImpl.create` calls [com.salesmanager.core.model.payments.Transaction](/modules/com.salesmanager.core.model.payments.md) `Transaction.toJSONString` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:41`
- `TransactionServiceImpl.getCapturableTransaction` calls [com.salesmanager.core.business.repositories.payments.TransactionRepository](/modules/com.salesmanager.core.business.repositories.payments.md) `TransactionRepository.findByOrder` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:121`
- `TransactionServiceImpl.getRefundableTransaction` calls [com.salesmanager.core.business.repositories.payments.TransactionRepository](/modules/com.salesmanager.core.business.repositories.payments.md) `TransactionRepository.findByOrder` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:151`
- `TransactionServiceImpl.lastTransaction` calls [com.salesmanager.core.business.repositories.payments.TransactionRepository](/modules/com.salesmanager.core.business.repositories.payments.md) `TransactionRepository.findByOrder` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:88`
- `TransactionServiceImpl.listTransactions` calls [com.salesmanager.core.business.repositories.payments.TransactionRepository](/modules/com.salesmanager.core.business.repositories.payments.md) `TransactionRepository.findByDates`, `TransactionRepository.findByOrder` `sm-core/src/main/java/com/salesmanager/core/business/services/payments/TransactionServiceImpl.java:205`
