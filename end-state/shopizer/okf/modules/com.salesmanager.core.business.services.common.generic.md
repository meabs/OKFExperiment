---
type: Code Module
title: "com.salesmanager.core.business.services.common.generic"
description: "com.salesmanager.core.business.services.common.generic: SalesManagerEntityServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java"
    sha256: "f6a53397a19525a04be35361e8dd5b3b105ab7e8970cc3a08f71f099e8139f37"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java"
    sha256: "4541bdea38c89af6f43161bab66d3dc7a958972edfa20f3d13ed898fb049375f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/TransactionalAspectAwareService.java"
    sha256: "a62772a3e713160fe5fa021a4784e19120f7f204e75d2355f976f435b53293ef"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.common.generic

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/TransactionalAspectAwareService.java`

## Types
- `SalesManagerEntityService` (interface) extends [com.salesmanager.core.business.services.common.generic.TransactionalAspectAwareService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:14`
- `SalesManagerEntityServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:15`
- `TransactionalAspectAwareService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/TransactionalAspectAwareService.java:10`

## Fields
- `SalesManagerEntityServiceImpl.objectClass: Class<E>` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:21`
- `SalesManagerEntityServiceImpl.repository: JpaRepository<E, K>` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:24`

## Functions and methods
- `SalesManagerEntityService.save(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:22`
- `SalesManagerEntityService.saveAll(Iterable<E>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:27`
- `SalesManagerEntityService.update(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:34`
- `SalesManagerEntityService.create(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:41`
- `SalesManagerEntityService.delete(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:49`
- `SalesManagerEntityService.getById(K) -> E` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:58`
- `SalesManagerEntityService.list() -> List<E>` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:65`
- `SalesManagerEntityService.count() -> Long` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:73`
- `SalesManagerEntityService.flush() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityService.java:78`
- `SalesManagerEntityServiceImpl.getObjectClass() -> Class<E>` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:33`
- `SalesManagerEntityServiceImpl.getById(K) -> E` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:38`
- `SalesManagerEntityServiceImpl.save(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:43`
- `SalesManagerEntityServiceImpl.saveAll(Iterable<E>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:47`
- `SalesManagerEntityServiceImpl.create(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:52`
- `SalesManagerEntityServiceImpl.update(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:58`
- `SalesManagerEntityServiceImpl.delete(E) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:63`
- `SalesManagerEntityServiceImpl.flush() -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:68`
- `SalesManagerEntityServiceImpl.list() -> List<E>` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:74`
- `SalesManagerEntityServiceImpl.count() -> Long` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:79`
- `SalesManagerEntityServiceImpl.saveAndFlush(E) -> E` `sm-core/src/main/java/com/salesmanager/core/business/services/common/generic/SalesManagerEntityServiceImpl.java:83`
