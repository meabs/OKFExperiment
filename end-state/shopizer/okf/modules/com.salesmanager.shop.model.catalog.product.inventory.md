---
type: Code Module
title: "com.salesmanager.shop.model.catalog.product.inventory"
description: "com.salesmanager.shop.model.catalog.product.inventory: InventoryEntity, PersistableInventory, ReadableInventory, ReadableInventoryList"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java"
    sha256: "75ee73ede4b830c60cf717fc4a13f77bcbcea37bda8032d15a7e3578fcad2b20"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java"
    sha256: "032e14243fc4a5fe04d6d350c2ecf435bb5c0930e26e0925a66fa8469f762dc0"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java"
    sha256: "ebda027e9a1cf4ada226eca46ae7dba6976cb993aa4414243db75c84bf594b16"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventoryList.java"
    sha256: "4198f1e0b57772b8555c7add734c606842e9dd54ee551d7d1c0e89d9aecb404d"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog.product.inventory

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventoryList.java`

## Types
- `InventoryEntity` (class) extends [com.salesmanager.shop.model.entity.Entity](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:5`
- `PersistableInventory` (class) extends [com.salesmanager.shop.model.catalog.product.inventory.InventoryEntity](/modules/com.salesmanager.shop.model.catalog.product.inventory.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:8`
- `ReadableInventory` (class) extends [com.salesmanager.shop.model.catalog.product.inventory.InventoryEntity](/modules/com.salesmanager.shop.model.catalog.product.inventory.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:9`
- `ReadableInventoryList` (class) extends [com.salesmanager.shop.model.entity.ReadableList](/modules/com.salesmanager.shop.model.entity.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventoryList.java:7`

## Fields
- `InventoryEntity.quantity: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:11`
- `InventoryEntity.region: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:12`
- `InventoryEntity.regionVariant: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:13`
- `InventoryEntity.owner: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:14`
- `InventoryEntity.dateAvailable: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:15`
- `InventoryEntity.available: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:16`
- `InventoryEntity.productQuantityOrderMin: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:17`
- `InventoryEntity.productQuantityOrderMax: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:18`
- `PersistableInventory.store: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:14`
- `PersistableInventory.productId: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:16`
- `PersistableInventory.variant: Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:17`
- `PersistableInventory.prices: List<PersistableProductPrice>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:18`
- `ReadableInventory.creationDate: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:15`
- `ReadableInventory.store: ReadableMerchantStore` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:17`
- `ReadableInventory.sku: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:18`
- `ReadableInventory.prices: List<ReadableProductPrice>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:19`
- `ReadableInventory.price: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:20`
- `ReadableInventoryList.inventory: List<ReadableInventory>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventoryList.java:13`

## Functions and methods
- `InventoryEntity.getQuantity() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:19`
- `InventoryEntity.setQuantity(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:22`
- `InventoryEntity.getRegion() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:25`
- `InventoryEntity.setRegion(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:28`
- `InventoryEntity.getRegionVariant() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:31`
- `InventoryEntity.setRegionVariant(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:34`
- `InventoryEntity.getOwner() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:37`
- `InventoryEntity.setOwner(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:40`
- `InventoryEntity.isAvailable() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:43`
- `InventoryEntity.setAvailable(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:46`
- `InventoryEntity.getProductQuantityOrderMin() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:49`
- `InventoryEntity.setProductQuantityOrderMin(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:52`
- `InventoryEntity.getProductQuantityOrderMax() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:55`
- `InventoryEntity.setProductQuantityOrderMax(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:58`
- `InventoryEntity.getDateAvailable() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:61`
- `InventoryEntity.setDateAvailable(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/InventoryEntity.java:64`
- `PersistableInventory.getStore() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:20`
- `PersistableInventory.setStore(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:24`
- `PersistableInventory.getPrices() -> List<PersistableProductPrice>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:28`
- `PersistableInventory.setPrices(List<PersistableProductPrice>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:32`
- `PersistableInventory.getProductId() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:36`
- `PersistableInventory.setProductId(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:40`
- `PersistableInventory.getVariant() -> Long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:44`
- `PersistableInventory.setVariant(Long) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:48`
- `ReadableInventory.getStore() -> ReadableMerchantStore` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:22`
- `ReadableInventory.setStore(ReadableMerchantStore) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:26`
- `ReadableInventory.getPrices() -> List<ReadableProductPrice>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:30`
- `ReadableInventory.setPrices(List<ReadableProductPrice>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:34`
- `ReadableInventory.getCreationDate() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:38`
- `ReadableInventory.setCreationDate(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:42`
- `ReadableInventory.getSku() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:46`
- `ReadableInventory.setSku(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:50`
- `ReadableInventory.getPrice() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:54`
- `ReadableInventory.setPrice(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:58`
- `ReadableInventoryList.getInventory() -> List<ReadableInventory>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventoryList.java:14`
- `ReadableInventoryList.setInventory(List<ReadableInventory>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventoryList.java:17`

## Depends on
- [com.salesmanager.shop.model.catalog.product.PersistableProductPrice](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/PersistableInventory.java:18`
- [com.salesmanager.shop.model.catalog.product.ReadableProductPrice](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:19`
- [com.salesmanager.shop.model.store.ReadableMerchantStore](/modules/com.salesmanager.shop.model.store.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/inventory/ReadableInventory.java:17`
