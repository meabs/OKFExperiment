---
type: Code Module
title: "com.salesmanager.shop.model.catalog.product.product"
description: "com.salesmanager.shop.model.catalog.product.product: PersistableProduct, PersistableProductInventory, ProductEntity, ProductSpecification"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java"
    sha256: "b8960839750c50b3c2364468aa04ca53889982dfe0ba1e3dd6604003259cb1b2"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java"
    sha256: "bef55f39fe1ed10f884f043ee3c86cc7a0edcbf69d12ac2dec5504863871ce2b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java"
    sha256: "6b313ee0da6c0041ac80ca7a6e915debe3c8e273750d1a8e512aef74e86fbe3f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java"
    sha256: "1a0495363b95d29a224acec2c485e8808658029aad7a2982c7b22d931e950a26"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.model.catalog.product.product

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java`

## Types
- `PersistableProduct` (class) extends [com.salesmanager.shop.model.catalog.product.product.ProductEntity](/modules/com.salesmanager.shop.model.catalog.product.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:14`
- `PersistableProductInventory` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:7`
- `ProductEntity` (class) extends [com.salesmanager.shop.model.catalog.product.Product](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:15`
- `ProductSpecification` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:13`

## Fields
- `PersistableProduct.descriptions: List<ProductDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:21`
- `PersistableProduct.attributes: List<PersistableProductAttribute>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:22`
- `PersistableProduct.images: List<PersistableImage>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:23`
- `PersistableProduct.categories: List<Category>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:24`
- `PersistableProduct.inventory: PersistableProductInventory` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:25`
- `PersistableProduct.variants: List<PersistableProductVariant>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:26`
- `PersistableProduct.type: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:27`
- `PersistableProductInventory.sku: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:11`
- `PersistableProductInventory.quantity: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:12`
- `PersistableProductInventory.price: PersistableProductPrice` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:13`
- `ProductEntity.price: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:22`
- `ProductEntity.quantity: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:23`
- `ProductEntity.sku: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:24`
- `ProductEntity.preOrder: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:25`
- `ProductEntity.productVirtual: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:26`
- `ProductEntity.quantityOrderMaximum: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:27`
- `ProductEntity.quantityOrderMinimum: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:28`
- `ProductEntity.productIsFree: boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:29`
- `ProductEntity.productSpecifications: ProductSpecification` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:31`
- `ProductEntity.rating: Double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:32`
- `ProductEntity.ratingCount: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:33`
- `ProductEntity.sortOrder: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:34`
- `ProductEntity.refSku: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:35`
- `ProductEntity.rentalDuration: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:44`
- `ProductEntity.rentalPeriod: int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:45`
- `ProductSpecification.height: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:21`
- `ProductSpecification.weight: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:22`
- `ProductSpecification.length: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:23`
- `ProductSpecification.width: BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:24`
- `ProductSpecification.model: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:25`
- `ProductSpecification.manufacturer: String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:26`
- `ProductSpecification.dimensionUnitOfMeasure: com.salesmanager.shop.model.references.DimensionUnitOfMeasure` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:40`
- `ProductSpecification.weightUnitOfMeasure: com.salesmanager.shop.model.references.WeightUnitOfMeasure` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:41`

## Functions and methods
- `PersistableProduct.getDescriptions() -> List<ProductDescription>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:29`
- `PersistableProduct.setDescriptions(List<ProductDescription>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:32`
- `PersistableProduct.getImages() -> List<PersistableImage>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:36`
- `PersistableProduct.setImages(List<PersistableImage>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:39`
- `PersistableProduct.getCategories() -> List<Category>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:42`
- `PersistableProduct.setCategories(List<Category>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:45`
- `PersistableProduct.setAttributes(List<PersistableProductAttribute>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:48`
- `PersistableProduct.getAttributes() -> List<PersistableProductAttribute>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:51`
- `PersistableProduct.getType() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:54`
- `PersistableProduct.setType(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:57`
- `PersistableProduct.getInventory() -> PersistableProductInventory` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:60`
- `PersistableProduct.setInventory(PersistableProductInventory) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:63`
- `PersistableProduct.getVariants() -> List<PersistableProductVariant>` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:66`
- `PersistableProduct.setVariants(List<PersistableProductVariant>) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:69`
- `PersistableProductInventory.getSku() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:14`
- `PersistableProductInventory.setSku(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:17`
- `PersistableProductInventory.getQuantity() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:20`
- `PersistableProductInventory.setQuantity(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:23`
- `PersistableProductInventory.getPrice() -> PersistableProductPrice` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:26`
- `PersistableProductInventory.setPrice(PersistableProductPrice) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:29`
- `ProductEntity.getPrice() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:53`
- `ProductEntity.setPrice(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:57`
- `ProductEntity.getQuantity() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:61`
- `ProductEntity.setQuantity(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:65`
- `ProductEntity.getSku() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:69`
- `ProductEntity.setSku(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:73`
- `ProductEntity.isProductIsFree() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:78`
- `ProductEntity.setProductIsFree(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:82`
- `ProductEntity.getSortOrder() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:86`
- `ProductEntity.setSortOrder(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:90`
- `ProductEntity.setQuantityOrderMaximum(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:94`
- `ProductEntity.getQuantityOrderMaximum() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:98`
- `ProductEntity.setProductVirtual(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:102`
- `ProductEntity.isProductVirtual() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:106`
- `ProductEntity.getQuantityOrderMinimum() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:110`
- `ProductEntity.setQuantityOrderMinimum(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:114`
- `ProductEntity.getRatingCount() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:118`
- `ProductEntity.setRatingCount(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:122`
- `ProductEntity.getRating() -> Double` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:126`
- `ProductEntity.setRating(Double) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:130`
- `ProductEntity.isPreOrder() -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:134`
- `ProductEntity.setPreOrder(boolean) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:138`
- `ProductEntity.getRefSku() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:142`
- `ProductEntity.setRefSku(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:146`
- `ProductEntity.getRentalDuration() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:150`
- `ProductEntity.setRentalDuration(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:154`
- `ProductEntity.getRentalPeriod() -> int` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:158`
- `ProductEntity.setRentalPeriod(int) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:162`
- `ProductEntity.getProductSpecifications() -> ProductSpecification` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:166`
- `ProductEntity.setProductSpecifications(ProductSpecification) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductEntity.java:170`
- `ProductSpecification.getManufacturer() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:28`
- `ProductSpecification.setManufacturer(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:31`
- `ProductSpecification.getModel() -> String` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:34`
- `ProductSpecification.setModel(String) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:37`
- `ProductSpecification.getHeight() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:43`
- `ProductSpecification.setHeight(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:46`
- `ProductSpecification.getWeight() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:49`
- `ProductSpecification.setWeight(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:52`
- `ProductSpecification.getLength() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:55`
- `ProductSpecification.setLength(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:58`
- `ProductSpecification.getWidth() -> BigDecimal` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:61`
- `ProductSpecification.setWidth(BigDecimal) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:64`
- `ProductSpecification.getDimensionUnitOfMeasure() -> DimensionUnitOfMeasure` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:67`
- `ProductSpecification.setDimensionUnitOfMeasure(DimensionUnitOfMeasure) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:70`
- `ProductSpecification.getWeightUnitOfMeasure() -> WeightUnitOfMeasure` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:73`
- `ProductSpecification.setWeightUnitOfMeasure(WeightUnitOfMeasure) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:76`
- `ProductSpecification.getSerialversionuid() -> long` `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:79`

## Depends on
- [com.salesmanager.shop.model.catalog.category.Category](/modules/com.salesmanager.shop.model.catalog.category.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:24`
- [com.salesmanager.shop.model.catalog.product.PersistableImage](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:23`
- [com.salesmanager.shop.model.catalog.product.PersistableProductPrice](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProductInventory.java:13`
- [com.salesmanager.shop.model.catalog.product.ProductDescription](/modules/com.salesmanager.shop.model.catalog.product.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:21`
- [com.salesmanager.shop.model.catalog.product.attribute.PersistableProductAttribute](/modules/com.salesmanager.shop.model.catalog.product.attribute.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:22`
- [com.salesmanager.shop.model.catalog.product.product.variant.PersistableProductVariant](/modules/com.salesmanager.shop.model.catalog.product.product.variant.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/PersistableProduct.java:26`
- [com.salesmanager.shop.model.references.DimensionUnitOfMeasure](/modules/com.salesmanager.shop.model.references.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:40`
- [com.salesmanager.shop.model.references.WeightUnitOfMeasure](/modules/com.salesmanager.shop.model.references.md) `sm-shop-model/src/main/java/com/salesmanager/shop/model/catalog/product/product/ProductSpecification.java:41`
