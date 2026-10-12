---
type: Code Module
title: "com.salesmanager.core.model.order.filehistory"
description: "com.salesmanager.core.model.order.filehistory: FileHistory"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java"
    sha256: "eb8c06a5f7f6648f1faf7985ea024244277d3e8027cb80b540b055641771a097"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.order.filehistory

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java`

## Types
- `FileHistory` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:22`

## Fields
- `FileHistory.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:40`
- `FileHistory.store: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:44`
- `FileHistory.fileId: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:47`
- `FileHistory.filesize: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:50`
- `FileHistory.dateAdded: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:54`
- `FileHistory.dateDeleted: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:58`
- `FileHistory.accountedDate: Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:62`
- `FileHistory.downloadCount: Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:65`

## Functions and methods
- `FileHistory.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:70`
- `FileHistory.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:74`
- `FileHistory.getStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:78`
- `FileHistory.setStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:82`
- `FileHistory.getFileId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:86`
- `FileHistory.setFileId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:90`
- `FileHistory.getFilesize() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:94`
- `FileHistory.setFilesize(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:98`
- `FileHistory.getDateAdded() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:102`
- `FileHistory.setDateAdded(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:106`
- `FileHistory.getDateDeleted() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:110`
- `FileHistory.setDateDeleted(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:114`
- `FileHistory.getAccountedDate() -> Date` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:118`
- `FileHistory.setAccountedDate(Date) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:122`
- `FileHistory.getDownloadCount() -> Integer` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:126`
- `FileHistory.setDownloadCount(Integer) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:130`

## Depends on
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:42`

## Calls
- `FileHistory.getAccountedDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:119`
- `FileHistory.getDateAdded` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:103`
- `FileHistory.getDateDeleted` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:111`
- `FileHistory.setAccountedDate` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:123`
- `FileHistory.setDateAdded` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:107`
- `FileHistory.setDateDeleted` calls [com.salesmanager.core.utils.CloneUtils](/modules/com.salesmanager.core.utils.md) `CloneUtils.clone` `sm-core-model/src/main/java/com/salesmanager/core/model/order/filehistory/FileHistory.java:115`
