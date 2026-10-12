---
type: Code Module
title: "com.salesmanager.shop.store.model.catalog"
description: "com.salesmanager.shop.store.model.catalog: Attribute, AttributeValue"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java"
    sha256: "b959882553b8273f09b6c376974ce6b8747cf869b7018f965191bf168d759d64"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java"
    sha256: "e9bbc64bb1a2c3df8b8c7edad6d7962632eaa6ddcd0c4c2924688d938c3f3425"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.model.catalog

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java`, `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java`

## Types
- `Attribute` (class) extends [com.salesmanager.shop.model.entity.ShopEntity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:9`
- `AttributeValue` (class) extends [com.salesmanager.shop.model.entity.ShopEntity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:7`

## Fields
- `Attribute.name: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:15`
- `Attribute.type: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:16`
- `Attribute.code: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:17`
- `Attribute.values: List<AttributeValue>` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:18`
- `Attribute.readOnlyValue: AttributeValue` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:19`
- `AttributeValue.name: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:13`
- `AttributeValue.description: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:14`
- `AttributeValue.defaultAttribute: boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:15`
- `AttributeValue.image: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:16`
- `AttributeValue.price: String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:17`
- `AttributeValue.sortOrder: int` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:18`

## Functions and methods
- `Attribute.getName() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:20`
- `Attribute.setName(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:23`
- `Attribute.getType() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:26`
- `Attribute.setType(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:29`
- `Attribute.setValues(List<AttributeValue>) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:35`
- `Attribute.getValues() -> List<AttributeValue>` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:38`
- `Attribute.setCode(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:41`
- `Attribute.getCode() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:44`
- `Attribute.setReadOnlyValue(AttributeValue) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:47`
- `Attribute.getReadOnlyValue() -> AttributeValue` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/Attribute.java:50`
- `AttributeValue.getName() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:20`
- `AttributeValue.setName(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:23`
- `AttributeValue.isDefaultAttribute() -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:26`
- `AttributeValue.setDefaultAttribute(boolean) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:29`
- `AttributeValue.getImage() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:32`
- `AttributeValue.setImage(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:35`
- `AttributeValue.getPrice() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:38`
- `AttributeValue.setPrice(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:41`
- `AttributeValue.getDescription() -> String` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:44`
- `AttributeValue.setDescription(String) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:47`
- `AttributeValue.getSortOrder() -> int` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:50`
- `AttributeValue.setSortOrder(int) -> void` `sm-shop/src/main/java/com/salesmanager/shop/store/model/catalog/AttributeValue.java:53`
