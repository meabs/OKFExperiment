---
type: Code Module
title: "com.salesmanager.shop.store.security.user"
description: "com.salesmanager.shop.store.security.user: CustomerDetails, JWTUser"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java"
    sha256: "2e62bebfe626aaf2153ceca872b978e7c3467b87d0b95d9f747455a7b9f3d425"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java"
    sha256: "7ef30180af02810e7fde8ff283fb3a0e9fe5eb22427af02da82bf4986d31bf03"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.security.user

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java`

## Types
- `CustomerDetails` (class) extends `org.springframework.security.core.userdetails.User` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:8`
- `JWTUser` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:11`

## Fields
- `CustomerDetails.email: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:15`
- `CustomerDetails.id: Long` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:16`
- `CustomerDetails.firstName: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:17`
- `CustomerDetails.lastName: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:18`
- `JWTUser.id: Long` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:17`
- `JWTUser.username: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:18`
- `JWTUser.firstname: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:19`
- `JWTUser.lastname: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:20`
- `JWTUser.password: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:21`
- `JWTUser.email: String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:22`
- `JWTUser.authorities: Collection<? extends GrantedAuthority>` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:23`
- `JWTUser.enabled: boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:24`
- `JWTUser.lastPasswordResetDate: Date` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:25`

## Functions and methods
- `CustomerDetails.getEmail() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:38`
- `CustomerDetails.setEmail(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:42`
- `CustomerDetails.getId() -> Long` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:46`
- `CustomerDetails.setId(Long) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:50`
- `CustomerDetails.getFirstName() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:54`
- `CustomerDetails.setFirstName(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:58`
- `CustomerDetails.getLastName() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:62`
- `CustomerDetails.setLastName(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/CustomerDetails.java:66`
- `JWTUser.getId() -> Long` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:48`
- `JWTUser.getUsername() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:53`
- `JWTUser.isAccountNonExpired() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:58`
- `JWTUser.isAccountNonLocked() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:64`
- `JWTUser.isCredentialsNonExpired() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:70`
- `JWTUser.getFirstname() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:76`
- `JWTUser.getLastname() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:80`
- `JWTUser.getEmail() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:84`
- `JWTUser.getPassword() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:88`
- `JWTUser.getAuthorities() -> Collection<? extends GrantedAuthority>` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:94`
- `JWTUser.isEnabled() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:99`
- `JWTUser.getLastPasswordResetDate() -> Date` `sm-shop/src/main/java/com/salesmanager/shop/store/security/user/JWTUser.java:104`
