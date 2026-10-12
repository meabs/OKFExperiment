---
type: Code Module
title: "com.salesmanager.core.business.modules.cms.product"
description: "com.salesmanager.core.business.modules.cms.product: ProductFileManager, ProductFileManagerImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductAssetsManager.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductAssetsManager.java"
    sha256: "5add53449a0417f4b4ce10e48867ad96372a6530d55f81ac37ed37aee22ae4b4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManager.java"
    sha256: "de655899ebc5bac7a44abd96c98c22dbd3f3338fc2358057c8da7e8b663a9986"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java"
    sha256: "aeae76daa0230129834a144fc43c59e7e7c89605d606a0c84404be6cd9745e25"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java"
    sha256: "81aa7406aa9f75b35959a116b3604a885c91a5b1092cd6f12f5a6860028db834"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImagePut.java"
    sha256: "8612c2682f7e109b6a6278433cb672f79f65c1ccdb1228836baad5b14ee10ffd"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageRemove.java"
    sha256: "3334e82991897bf2671256e682f00e6639018711ba1c059fa450678ef5769089"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.cms.product

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductAssetsManager.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManager.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImagePut.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageRemove.java`

## Types
- `ProductAssetsManager` (interface) extends `java.io.Serializable`, [com.salesmanager.core.business.modules.cms.common.AssetsManager](/modules/com.salesmanager.core.business.modules.cms.common.md), [com.salesmanager.core.business.modules.cms.product.ProductImageGet](/modules/com.salesmanager.core.business.modules.cms.product.md), [com.salesmanager.core.business.modules.cms.product.ProductImagePut](/modules/com.salesmanager.core.business.modules.cms.product.md), [com.salesmanager.core.business.modules.cms.product.ProductImageRemove](/modules/com.salesmanager.core.business.modules.cms.product.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductAssetsManager.java:6`
- `ProductFileManager` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManager.java:5`
- `ProductFileManagerImpl` (class) extends [com.salesmanager.core.business.modules.cms.product.ProductFileManager](/modules/com.salesmanager.core.business.modules.cms.product.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:29`
- `ProductImageGet` (interface) extends [com.salesmanager.core.business.modules.cms.common.ImageGet](/modules/com.salesmanager.core.business.modules.cms.common.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java:11`
- `ProductImagePut` (interface) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImagePut.java:8`
- `ProductImageRemove` (interface) extends [com.salesmanager.core.business.modules.cms.common.ImageRemove](/modules/com.salesmanager.core.business.modules.cms.common.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageRemove.java:9`

## Fields
- `ProductFileManagerImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:31`
- `ProductFileManagerImpl.uploadImage: ProductImagePut` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:34`
- `ProductFileManagerImpl.getImage: ProductImageGet` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:35`
- `ProductFileManagerImpl.removeImage: ProductImageRemove` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:36`
- `ProductFileManagerImpl.configuration: CoreConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:38`
- `ProductFileManagerImpl.PRODUCT_IMAGE_HEIGHT_SIZE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:40`
- `ProductFileManagerImpl.PRODUCT_IMAGE_WIDTH_SIZE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:41`
- `ProductFileManagerImpl.CROP_UPLOADED_IMAGES: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:42`

## Functions and methods
- `ProductFileManagerImpl.getConfiguration() -> CoreConfiguration` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:45`
- `ProductFileManagerImpl.setConfiguration(CoreConfiguration) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:50`
- `ProductFileManagerImpl.getRemoveImage() -> ProductImageRemove` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:55`
- `ProductFileManagerImpl.setRemoveImage(ProductImageRemove) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:60`
- `ProductFileManagerImpl.addProductImage(ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:65`
- `ProductFileManagerImpl.getProductImage(ProductImage) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:273`
- `ProductFileManagerImpl.getImages(String, FileContentType) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:279`
- `ProductFileManagerImpl.getImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:286`
- `ProductFileManagerImpl.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:293`
- `ProductFileManagerImpl.removeProductImages(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:313`
- `ProductFileManagerImpl.removeImages(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:321`
- `ProductFileManagerImpl.getUploadImage() -> ProductImagePut` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:329`
- `ProductFileManagerImpl.setUploadImage(ProductImagePut) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:334`
- `ProductFileManagerImpl.getGetImage() -> ProductImageGet` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:340`
- `ProductFileManagerImpl.setGetImage(ProductImageGet) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:345`
- `ProductFileManagerImpl.getProductImage(String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:350`
- `ProductFileManagerImpl.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:358`
- `ProductImageGet.getProductImage(String, String, String) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java:22`
- `ProductImageGet.getProductImage(String, String, String, ProductImageSize) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java:25`
- `ProductImageGet.getProductImage(ProductImage) -> OutputContentFile` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java:28`
- `ProductImageGet.getImages(Product) -> List<OutputContentFile>` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageGet.java:30`
- `ProductImagePut.addProductImage(ProductImage, ImageContentFile) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImagePut.java:10`
- `ProductImageRemove.removeProductImage(ProductImage) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageRemove.java:11`
- `ProductImageRemove.removeProductImages(Product) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductImageRemove.java:13`

## Depends on
- [com.salesmanager.core.business.utils.CoreConfiguration](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:38`

## Calls
- `ProductFileManagerImpl.addProductImage` calls [com.salesmanager.core.business.utils.ProductImageSizeUtils](/modules/com.salesmanager.core.business.utils.md) `ProductImageSizeUtils.resizeWithRatio` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:184`
- `ProductFileManagerImpl.removeImages` calls [com.salesmanager.core.business.modules.cms.common.ImageRemove](/modules/com.salesmanager.core.business.modules.cms.common.md) `ImageRemove.removeImages` `sm-core/src/main/java/com/salesmanager/core/business/modules/cms/product/ProductFileManagerImpl.java:324`
