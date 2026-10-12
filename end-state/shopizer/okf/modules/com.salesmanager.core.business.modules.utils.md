---
type: Code Module
title: "com.salesmanager.core.business.modules.utils"
description: "com.salesmanager.core.business.modules.utils: EncryptionImpl, GeoLocationImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java"
    sha256: "ffd337fdee7172e8bf97f57e921110ce9e89eecaa41d87376fe7801242eb4f17"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/utils/GeoLocationImpl.java"
    sha256: "2d74b9ed7393eccaf7d9b687f5f6d07d8eb039203e2c6b6af1a1daa0de61997f"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.utils

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/GeoLocationImpl.java`

## Types
- `EncryptionImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:11`
- `GeoLocationImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/GeoLocationImpl.java:20`

## Fields
- `EncryptionImpl.IV_P: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:13`
- `EncryptionImpl.KEY_SPEC: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:14`
- `EncryptionImpl.CYPHER_SPEC: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:15`
- `EncryptionImpl.secretKey: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:19`
- `GeoLocationImpl.reader: DatabaseReader` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/GeoLocationImpl.java:22`
- `GeoLocationImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/GeoLocationImpl.java:23`

## Functions and methods
- `EncryptionImpl.encrypt(String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:23`
- `EncryptionImpl.decrypt(String) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:42`
- `EncryptionImpl.bytesToHex(byte[]) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:64`
- `EncryptionImpl.hexToBytes(String) -> byte[]` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:83`
- `EncryptionImpl.getSecretKey() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:99`
- `EncryptionImpl.setSecretKey(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/EncryptionImpl.java:103`
- `GeoLocationImpl.getAddress(String) -> Address` `sm-core/src/main/java/com/salesmanager/core/business/modules/utils/GeoLocationImpl.java:26`
