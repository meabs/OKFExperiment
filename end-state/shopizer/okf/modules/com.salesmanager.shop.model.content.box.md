---
type: Code Module
title: "com.salesmanager.shop.model.content.box"
description: "com.salesmanager.shop.model.content.box: ContentBox, PersistableContentBox, ReadableContentBox, ReadableContentBoxFull"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ContentBox.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ContentBox.java"
    sha256: "8c09088866de4e10a1ccba10d55e0facde3425c0866a6f1dcf42b73b1f65af04"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/PersistableContentBox.java"
    sha256: "5bed81b5ca3467b087e774453067f651542fd3f394fb397b3949ef9a9c09410a"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java"
    sha256: "efdbafa9b4912a3fa2367883b1f6fe776cc29988fd21adde0a9ecf461de65e16"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java"
    sha256: "7986097e421cc2bfd26409cd8b8f50d6de8eb94d72a2e1d19ec6816a59f7564a"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.content.box

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ContentBox.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/PersistableContentBox.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java`

## Types
- `ContentBox` (class) extends [com.salesmanager.shop.model.content.common.Content](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ContentBox.java:5`
- `PersistableContentBox` (class) extends [com.salesmanager.shop.model.content.box.ContentBox](/modules/com.salesmanager.shop.model.content.box.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/PersistableContentBox.java:7`
- `ReadableContentBox` (class) extends [com.salesmanager.shop.model.content.common.Content](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java:6`
- `ReadableContentBoxFull` (class) extends [com.salesmanager.shop.model.content.box.ReadableContentBox](/modules/com.salesmanager.shop.model.content.box.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java:7`

## Fields
- `PersistableContentBox.descriptions: List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/PersistableContentBox.java:14`
- `ReadableContentBox.description: ContentDescription` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java:8`
- `ReadableContentBox.BOX: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java:9`
- `ReadableContentBoxFull.descriptions: List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java:14`

## Functions and methods
- `PersistableContentBox.getDescriptions() -> List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/PersistableContentBox.java:16`
- `PersistableContentBox.setDescriptions(List<ContentDescription>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/PersistableContentBox.java:20`
- `ReadableContentBox.getDescription() -> ContentDescription` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java:20`
- `ReadableContentBox.setDescription(ContentDescription) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java:24`
- `ReadableContentBoxFull.getDescriptions() -> List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java:16`
- `ReadableContentBoxFull.setDescriptions(List<ContentDescription>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java:20`

## Depends on
- [com.salesmanager.shop.model.content.common.ContentDescription](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBoxFull.java:14`
- [com.salesmanager.shop.model.content.common.ContentDescription](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/box/ReadableContentBox.java:8`
