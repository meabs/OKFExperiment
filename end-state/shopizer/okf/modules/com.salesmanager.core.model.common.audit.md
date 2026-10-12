---
type: Code Module
title: "com.salesmanager.core.model.common.audit"
description: "com.salesmanager.core.model.common.audit: AuditListener, AuditSection"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditListener.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditListener.java"
    sha256: "00d0b2f4c6f266ebabb7f471b524ecadd4e4f6fb0406585b69738786b3a6cb80"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java"
    sha256: "944b8807d72af979a260b6203d2c1beba21a11367c8589bac85c51f784d3763e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/Auditable.java"
    sha256: "fbd524a9864fb5767771c36490c2ea4bb34c04e102dcae5652e00d400d11f904"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.common.audit

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditListener.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/Auditable.java`

## Types
- `AuditListener` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditListener.java:7`
- `AuditSection` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:15`
- `Auditable` (interface) `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/Auditable.java:3`

## Fields
- `AuditSection.dateCreated: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:23`
- `AuditSection.dateModified: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:27`
- `AuditSection.modifiedBy: String` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:30`

## Functions and methods
- `AuditListener.onSave(Object) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditListener.java:9`
- `AuditListener.onUpdate(Object) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditListener.java:23`
- `AuditSection.getDateCreated() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:34`
- `AuditSection.setDateCreated(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:38`
- `AuditSection.getDateModified() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:42`
- `AuditSection.setDateModified(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:46`
- `AuditSection.getModifiedBy() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:50`
- `AuditSection.setModifiedBy(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:54`
- `Auditable.getAuditSection() -> AuditSection` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/Auditable.java:5`
- `Auditable.setAuditSection(AuditSection) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/Auditable.java:7`

## Calls
- `AuditSection.getDateCreated` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:35`
- `AuditSection.getDateModified` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:43`
- `AuditSection.setDateCreated` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:39`
- `AuditSection.setDateModified` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/common/audit/AuditSection.java:47`
