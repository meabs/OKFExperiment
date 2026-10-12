---
type: Code Module
title: "com.salesmanager.core.business.repositories.system"
description: "com.salesmanager.core.business.repositories.system: findByMerchantStore, findByMerchantStoreAndKey, findByMerchantStoreAndType, findByStore"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java"
    sha256: "2cafe43a8897a969e7cf82091a76ce8f7eeae50a43a1d7bf593b4d4b413d65af"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantLogRepository.java"
    sha256: "e58e20ffe7555bd38ed6c5ab7ed61da1acec4ce197526afa1cac03ccdba03767"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/ModuleConfigurationRepository.java"
    sha256: "7a10515fce1003e986e00dd1ae436aaacef1c3a894de09be1e47aa2eec5ac620"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/OptinRepository.java"
    sha256: "f6c33a33786a982fd736c8a30dc433c6a59a156598dbb71edbfc2f6bd05bdb64"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemConfigurationRepository.java"
    sha256: "3d778568eb1fbbacce69ffb2fcbddfc26d31c5720be2f9cfd22501cb3092c1ef"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemNotificationRepository.java"
    sha256: "17e55500ab687672e20419e795f22f6e0eafc8f11e62de1df294932daec6b1ca"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.system

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantLogRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/ModuleConfigurationRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/OptinRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemConfigurationRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemNotificationRepository.java`

## Types
- `MerchantConfigurationRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java:11`
- `MerchantLogRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantLogRepository.java:10`
- `ModuleConfigurationRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/ModuleConfigurationRepository.java:9`
- `OptinRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/OptinRepository.java:12`
- `SystemConfigurationRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemConfigurationRepository.java:7`
- `SystemNotificationRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemNotificationRepository.java:7`

## Functions and methods
- `MerchantConfigurationRepository.findByMerchantStore(Integer) -> List<MerchantConfiguration>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java:17`
- `MerchantConfigurationRepository.findByMerchantStoreAndKey(Integer, String) -> MerchantConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java:20`
- `MerchantConfigurationRepository.findByMerchantStoreAndType(Integer, MerchantConfigurationType) -> List<MerchantConfiguration>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantConfigurationRepository.java:23`
- `MerchantLogRepository.findByStore(MerchantStore) -> List<MerchantLog>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/MerchantLogRepository.java:12`
- `ModuleConfigurationRepository.findByModule(String) -> List<IntegrationModule>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/ModuleConfigurationRepository.java:11`
- `ModuleConfigurationRepository.findByCode(String) -> IntegrationModule` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/ModuleConfigurationRepository.java:13`
- `OptinRepository.findByMerchant(Integer) -> List<Optin>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/OptinRepository.java:15`
- `OptinRepository.findByMerchantAndType(Integer, OptinType) -> Optin` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/OptinRepository.java:19`
- `OptinRepository.findByMerchantAndCode(Integer, String) -> Optin` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/OptinRepository.java:22`
- `SystemConfigurationRepository.findByKey(String) -> SystemConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/repositories/system/SystemConfigurationRepository.java:10`
