---
type: Code Module
title: "com.salesmanager.shop.model.shipping"
description: "com.salesmanager.shop.model.shipping: BoxConfiguration, ExpeditionConfiguration, ShippingConfiguration"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java"
    sha256: "47d97cd8bbf3453cd7b35f6be1860134ca055345ee6e88649937ae1d2286604e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java"
    sha256: "72f302a83f6606597df04752a91298a3b678c4e225ebb420c5319407b729a788"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java"
    sha256: "1cbc95f4cb6dae8ca6afb9842b4864356bd3469701fcb596663c5bde788b939c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.shipping

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java`

## Types
- `BoxConfiguration` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:5`
- `ExpeditionConfiguration` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:6`
- `ShippingConfiguration` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:7`

## Fields
- `BoxConfiguration.code: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:7`
- `BoxConfiguration.boxWidth: double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:9`
- `BoxConfiguration.boxHeight: double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:10`
- `BoxConfiguration.boxLength: double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:11`
- `BoxConfiguration.boxWeight: double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:12`
- `BoxConfiguration.maxWeight: double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/BoxConfiguration.java:13`
- `ExpeditionConfiguration.iternationalShipping: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:8`
- `ExpeditionConfiguration.taxOnShipping: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:9`
- `ExpeditionConfiguration.shipToCountry: List<String>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:10`
- `ShippingConfiguration.taxOnShipping: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:16`
- `ShippingConfiguration.boxConfigurations: List<BoxConfiguration>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:17`

## Functions and methods
- `ExpeditionConfiguration.isIternationalShipping() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:12`
- `ExpeditionConfiguration.setIternationalShipping(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:16`
- `ExpeditionConfiguration.getShipToCountry() -> List<String>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:20`
- `ExpeditionConfiguration.setShipToCountry(List<String>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:24`
- `ExpeditionConfiguration.isTaxOnShipping() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:28`
- `ExpeditionConfiguration.setTaxOnShipping(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ExpeditionConfiguration.java:32`
- `ShippingConfiguration.isTaxOnShipping() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:20`
- `ShippingConfiguration.setTaxOnShipping(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:24`
- `ShippingConfiguration.getBoxConfigurations() -> List<BoxConfiguration>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:28`
- `ShippingConfiguration.setBoxConfigurations(List<BoxConfiguration>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/shipping/ShippingConfiguration.java:32`
