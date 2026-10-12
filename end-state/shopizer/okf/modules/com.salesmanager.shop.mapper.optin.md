---
type: Code Module
title: "com.salesmanager.shop.mapper.optin"
description: "com.salesmanager.shop.mapper.optin: PersistableOptinMapper, ReadableOptinMapper"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java"
    sha256: "f2d9924dd1c765974fea28e656a8f93731014528b10216a8b6175b346dd724b4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/ReadableOptinMapper.java"
    sha256: "bcc706c3b8639acec15407ada055f521e583c5fc802d8f9091a8d5aeb44f193c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.mapper.optin

Source: `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java`, `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/ReadableOptinMapper.java`

## Types
- `PersistableOptinMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java:11`
- `ReadableOptinMapper` (class) `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/ReadableOptinMapper.java:10`

## Functions and methods
- `PersistableOptinMapper.convert(PersistableOptin, MerchantStore, Language) -> Optin` `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java:15`
- `PersistableOptinMapper.merge(PersistableOptin, Optin, MerchantStore, Language) -> Optin` `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java:25`
- `ReadableOptinMapper.convert(Optin, MerchantStore, Language) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/ReadableOptinMapper.java:14`
- `ReadableOptinMapper.merge(Optin, ReadableOptin, MerchantStore, Language) -> ReadableOptin` `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/ReadableOptinMapper.java:23`

## Calls
- `PersistableOptinMapper.convert` calls [com.salesmanager.core.model.system.optin.OptinType](/modules/com.salesmanager.core.model.system.optin.md) `OptinType.valueOf` `sm-shop/src/main/java/com/salesmanager/shop/mapper/optin/PersistableOptinMapper.java:20`
