---
type: Code Module
title: "com.salesmanager.core.business.repositories.shoppingcart"
description: "com.salesmanager.core.business.repositories.shoppingcart: findOne, deleteById, findOne, findByCode"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartAttributeRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartAttributeRepository.java"
    sha256: "5c1ce64722aeabdd5e010654fa389a32e4db6740aecbd6413fec4103d0df051b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartItemRepository.java"
    sha256: "90421c2e0db3a412fc71750e4fe3534ea2fe8da89cf0241e6343591137c05f91"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java"
    sha256: "fbf6b9167d0ca7699025a7ad73d969a7e3721a815769804c064cf8be19002978"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.shoppingcart

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartAttributeRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartItemRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java`

## Types
- `ShoppingCartAttributeRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartAttributeRepository.java:6`
- `ShoppingCartItemRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartItemRepository.java:7`
- `ShoppingCartRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java:9`

## Functions and methods
- `ShoppingCartItemRepository.findOne(Long) -> ShoppingCartItem` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartItemRepository.java:9`
- `ShoppingCartItemRepository.deleteById(Long) -> void` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartItemRepository.java:12`
- `ShoppingCartRepository.findOne(Long) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java:11`
- `ShoppingCartRepository.findByCode(String) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java:14`
- `ShoppingCartRepository.findById(Integer, Long) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java:17`
- `ShoppingCartRepository.findByCode(Integer, String) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java:20`
- `ShoppingCartRepository.findByCustomer(Long) -> List<ShoppingCart>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/shoppingcart/ShoppingCartRepository.java:23`
