---
type: Code Module
title: "com.salesmanager.core.model.reference.language"
description: "com.salesmanager.core.model.reference.language: Language"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java"
    sha256: "ac6ceef3eaa4e18cbc027ae0f74da784a259e733b8a89b087db0143c6cf6fa72"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.reference.language

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java`

## Types
- `Language` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:28`

## Fields
- `Language.id: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:42`
- `Language.auditSection: AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:46`
- `Language.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:49`
- `Language.sortOrder: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:53`
- `Language.storesDefaultLanguage: List<MerchantStore>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:57`
- `Language.stores: List<MerchantStore>` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:61`

## Functions and methods
- `Language.getId() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:69`
- `Language.setId(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:74`
- `Language.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:80`
- `Language.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:84`
- `Language.getSortOrder() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:88`
- `Language.setSortOrder(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:92`
- `Language.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:96`
- `Language.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:101`
- `Language.equals(Object) -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:106`

## Depends on
- [com.salesmanager.core.model.common.audit.AuditSection](/modules/com.salesmanager.core.model.common.audit.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:44`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/reference/language/Language.java:55`
