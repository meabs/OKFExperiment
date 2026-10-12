---
type: Code Module
title: "com.salesmanager.core.model.customer.connection"
description: "com.salesmanager.core.model.customer.connection: AbstractUserConnection, AbstractUserConnectionWithCompositeKey, UserConnection, UserConnectionPK"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java"
    sha256: "3112f0535b16c20f1498da55eca49e31397b12a22c767989953f21cb73135fc9"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java"
    sha256: "741fefc96ec46d68530317fdac06ff64977e2f049f283db5aa59da5a2a5ae755"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java"
    sha256: "8b459c50cf39657ef091a7143816ae19f028d2b1fd653bbff7b537b37b1e0aad"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnection.java"
    sha256: "b4c2f745db9b0e268085436449ccfb8da4ceedc7ff719285c7595a666c2a7e5f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java"
    sha256: "9bd64def05cf38d586a3196d9e949675eb69134b7c6fdfea96c3b3fafedda77e"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.customer.connection

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnection.java`, `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java`

## Types
- `AbstractUserConnection` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:8`
- `AbstractUserConnectionWithCompositeKey` (class) extends [com.salesmanager.core.model.customer.connection.AbstractUserConnection](/modules/com.salesmanager.core.model.customer.connection.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:10`
- `RemoteUser` (interface) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:5`
- `UserConnection` (class) extends [com.salesmanager.core.model.customer.connection.AbstractUserConnectionWithCompositeKey](/modules/com.salesmanager.core.model.customer.connection.md) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnection.java:5`
- `UserConnectionPK` (class) `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:12`

## Fields
- `AbstractUserConnection.accessToken: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:18`
- `AbstractUserConnection.displayName: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:19`
- `AbstractUserConnection.expireTime: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:20`
- `AbstractUserConnection.imageUrl: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:21`
- `AbstractUserConnection.profileUrl: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:22`
- `AbstractUserConnection.userRank: int` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:23`
- `AbstractUserConnection.refreshToken: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:24`
- `AbstractUserConnection.secret: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:25`
- `AbstractUserConnectionWithCompositeKey.primaryKey: UserConnectionPK` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:18`
- `UserConnectionPK.userId: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:20`
- `UserConnectionPK.providerId: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:21`
- `UserConnectionPK.providerUserId: String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:22`

## Functions and methods
- `AbstractUserConnection.getAccessToken() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:28`
- `AbstractUserConnection.setAccessToken(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:32`
- `AbstractUserConnection.getDisplayName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:36`
- `AbstractUserConnection.setDisplayName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:40`
- `AbstractUserConnection.getExpireTime() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:44`
- `AbstractUserConnection.setExpireTime(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:48`
- `AbstractUserConnection.getImageUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:52`
- `AbstractUserConnection.setImageUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:56`
- `AbstractUserConnection.getProfileUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:60`
- `AbstractUserConnection.setProfileUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:64`
- `AbstractUserConnection.getProviderId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:68`
- `AbstractUserConnection.setProviderId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:70`
- `AbstractUserConnection.getProviderUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:72`
- `AbstractUserConnection.setProviderUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:74`
- `AbstractUserConnection.getRank() -> int` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:76`
- `AbstractUserConnection.setRank(int) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:80`
- `AbstractUserConnection.getRefreshToken() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:84`
- `AbstractUserConnection.setRefreshToken(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:88`
- `AbstractUserConnection.getSecret() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:92`
- `AbstractUserConnection.setSecret(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:96`
- `AbstractUserConnection.getUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:100`
- `AbstractUserConnection.setUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:102`
- `AbstractUserConnection.getId() -> P` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnection.java:104`
- `AbstractUserConnectionWithCompositeKey.getProviderId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:25`
- `AbstractUserConnectionWithCompositeKey.setProviderId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:30`
- `AbstractUserConnectionWithCompositeKey.getProviderUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:35`
- `AbstractUserConnectionWithCompositeKey.setProviderUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:40`
- `AbstractUserConnectionWithCompositeKey.getUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:45`
- `AbstractUserConnectionWithCompositeKey.setUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:50`
- `AbstractUserConnectionWithCompositeKey.getId() -> UserConnectionPK` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/AbstractUserConnectionWithCompositeKey.java:55`
- `RemoteUser.getUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:8`
- `RemoteUser.setUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:10`
- `RemoteUser.getProviderUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:14`
- `RemoteUser.setProviderUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:16`
- `RemoteUser.getProviderId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:18`
- `RemoteUser.setProviderId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:20`
- `RemoteUser.getRank() -> int` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:22`
- `RemoteUser.setRank(int) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:24`
- `RemoteUser.getSecret() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:26`
- `RemoteUser.setSecret(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:28`
- `RemoteUser.getDisplayName() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:30`
- `RemoteUser.setDisplayName(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:32`
- `RemoteUser.getProfileUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:34`
- `RemoteUser.setProfileUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:36`
- `RemoteUser.getImageUrl() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:38`
- `RemoteUser.setImageUrl(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:40`
- `RemoteUser.getAccessToken() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:42`
- `RemoteUser.setAccessToken(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:44`
- `RemoteUser.getRefreshToken() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:46`
- `RemoteUser.setRefreshToken(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:48`
- `RemoteUser.getExpireTime() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:50`
- `RemoteUser.setExpireTime(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/RemoteUser.java:52`
- `UserConnectionPK.getUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:24`
- `UserConnectionPK.setUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:28`
- `UserConnectionPK.getProviderId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:32`
- `UserConnectionPK.setProviderId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:36`
- `UserConnectionPK.getProviderUserId() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:40`
- `UserConnectionPK.setProviderUserId(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:44`
- `UserConnectionPK.equals(Object) -> boolean` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:48`
- `UserConnectionPK.hashCode() -> int` `sm-core-model/src/main/java/com/salesmanager/core/model/customer/connection/UserConnectionPK.java:59`
