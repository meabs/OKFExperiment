---
type: Code Module
title: "com.salesmanager.shop.controller"
description: "com.salesmanager.shop.controller: FilesController, ImagesController; 6 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java"
    sha256: "cc584be4e7f66d59011e6686d29f278d1e541105025c40aa5ddfc0e88cc888b1"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java"
    sha256: "3a92f169b5f87eaf9bf50c9272294e6ff23dcc682e2a5cc35bc09d6637961523"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.controller

Source: `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java`, `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java`

## Types
- `FilesController` (class) extends [com.salesmanager.shop.store.controller.AbstractController](/modules/com.salesmanager.shop.store.controller.md) `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:22`
- `ImagesController` (class) `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:32`

## Fields
- `FilesController.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:25`
- `FilesController.contentService: ContentService` `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:30`
- `ImagesController.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:35`
- `ImagesController.contentService: ContentService` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:40`
- `ImagesController.productImageService: ProductImageService` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:43`
- `ImagesController.tempImage: byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:45`

## Functions and methods
- `FilesController.downloadFile(String, String, String, HttpServletRequest, HttpServletResponse) -> byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:41`
- `FilesController.downloadProduct(String, String, String, HttpServletRequest, HttpServletResponse) -> byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:70`
- `ImagesController.init() -> void` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:47`
- `ImagesController.printImage(String, String, String, String) -> byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:71`
- `ImagesController.printImage(String, String, String, String, String) -> byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:113`
- `ImagesController.printImage(String, String, String, String, String, HttpServletRequest) -> byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:161`
- `ImagesController.printImage(String, String, String, String, HttpServletRequest) -> byte[]` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:211`

## HTTP routes
- `ANY /admin/files/downloads/{storeCode}/{fileName}.{extension}` handled by `com.salesmanager.shop.controller.FilesController#downloadProduct` `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:70`
- `ANY /static/files/{storeCode}/{fileName}.{extension}` handled by `com.salesmanager.shop.controller.FilesController#downloadFile` `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:41`
- `ANY /static/files/{storeCode}/{imageType}/{imageName}.{extension}` handled by `com.salesmanager.shop.controller.ImagesController#printImage` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:71`
- `ANY /static/products/{storeCode}/{productCode}/{imageName}.{extension}` handled by `com.salesmanager.shop.controller.ImagesController#printImage` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:211`
- `ANY /static/products/{storeCode}/{productCode}/{imageSize}/{imageName}.{extension}` handled by `com.salesmanager.shop.controller.ImagesController#printImage` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:161`
- `ANY /static/{storeCode}/{imageType}/{productCode}/{imageName}.{extension}` handled by `com.salesmanager.shop.controller.ImagesController#printImage` `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:113`

## Depends on
- [com.salesmanager.core.business.services.catalog.product.image.ProductImageService](/modules/com.salesmanager.core.business.services.catalog.product.image.md) `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:42`
- [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `sm-shop/src/main/java/com/salesmanager/shop/controller/FilesController.java:29`
- [com.salesmanager.core.business.services.content.ContentService](/modules/com.salesmanager.core.business.services.content.md) `sm-shop/src/main/java/com/salesmanager/shop/controller/ImagesController.java:39`
