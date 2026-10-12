---
type: Code Module
title: "com.salesmanager.shop.model.content.page"
description: "com.salesmanager.shop.model.content.page: ContentPage, PersistableContentPage, ReadableContentPage, ReadableContentPageFull"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java"
    sha256: "718fd2268e42c9b5dcac75372a925924839c01855c17eb918804f088d0cbad2c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java"
    sha256: "7d3a110b9bed6ed514b3da8775b046b8a16f8b576b0a0470a95baa40d1edb6d6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java"
    sha256: "bd169ea6f89bd0d8a5de4dbdeadf7143319b8dffa1b1a1a47fa10aeeb0e70906"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java"
    sha256: "82cc96a2a0039e3d65b720ee7ee2c1c68da8df9a785a7bef9b3f1bb7732f6fd6"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.content.page

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java`

## Types
- `ContentPage` (class) extends [com.salesmanager.shop.model.content.common.Content](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java:5`
- `PersistableContentPage` (class) extends [com.salesmanager.shop.model.content.page.ContentPage](/modules/com.salesmanager.shop.model.content.page.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java:7`
- `ReadableContentPage` (class) extends [com.salesmanager.shop.model.content.page.ContentPage](/modules/com.salesmanager.shop.model.content.page.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:5`
- `ReadableContentPageFull` (class) extends [com.salesmanager.shop.model.content.page.ReadableContentPage](/modules/com.salesmanager.shop.model.content.page.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java:7`

## Fields
- `ContentPage.linkToMenu: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java:11`
- `PersistableContentPage.descriptions: List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java:14`
- `ReadableContentPage.description: ContentDescription` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:13`
- `ReadableContentPage.path: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:14`
- `ReadableContentPageFull.descriptions: List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java:13`

## Functions and methods
- `ContentPage.isLinkToMenu() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java:12`
- `ContentPage.setLinkToMenu(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ContentPage.java:15`
- `PersistableContentPage.getDescriptions() -> List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java:16`
- `PersistableContentPage.setDescriptions(List<ContentDescription>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java:20`
- `ReadableContentPage.getDescription() -> ContentDescription` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:17`
- `ReadableContentPage.setDescription(ContentDescription) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:21`
- `ReadableContentPage.getPath() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:25`
- `ReadableContentPage.setPath(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPage.java:29`
- `ReadableContentPageFull.getDescriptions() -> List<ContentDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java:15`
- `ReadableContentPageFull.setDescriptions(List<ContentDescription>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java:19`

## Depends on
- [com.salesmanager.shop.model.content.common.ContentDescription](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/PersistableContentPage.java:14`
- [com.salesmanager.shop.model.content.common.ContentDescription](/modules/com.salesmanager.shop.model.content.common.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/content/page/ReadableContentPageFull.java:13`
