---
type: Code Module
title: "com.salesmanager.core.business.services.shoppingcart"
description: "com.salesmanager.core.business.services.shoppingcart: ShoppingCartCalculationServiceImpl, ShoppingCartServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationService.java"
    sha256: "deb3e80517c4c2db0f36882da4528cf70a990a1cd57fba82e2fe5db34479f1b3"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java"
    sha256: "15efd71f1badeb0221ca46f6e5661c07e6c192c7e5f11c8ab499e0031b89cb2c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java"
    sha256: "cba8f9a0d89be419c8e6f65d0f96384fc6247dd2a5b629d334afe6653a1324be"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java"
    sha256: "0c561806ad02516ca6514bb66ff9ac41a4fbc39dd9870c40f8fe063866711d8c"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.shoppingcart

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java`

## Types
- `ShoppingCartCalculationService` (interface) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationService.java:21`
- `ShoppingCartCalculationServiceImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:33`
- `ShoppingCartService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:15`
- `ShoppingCartServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:36`

## Fields
- `ShoppingCartCalculationServiceImpl.LOG: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:36`
- `ShoppingCartCalculationServiceImpl.shoppingCartService: ShoppingCartService` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:39`
- `ShoppingCartCalculationServiceImpl.orderService: OrderService` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:42`
- `ShoppingCartServiceImpl.shoppingCartRepository: ShoppingCartRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:40`
- `ShoppingCartServiceImpl.productService: ProductService` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:43`
- `ShoppingCartServiceImpl.shoppingCartItemRepository: ShoppingCartItemRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:46`
- `ShoppingCartServiceImpl.shoppingCartAttributeItemRepository: ShoppingCartAttributeRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:49`
- `ShoppingCartServiceImpl.pricingService: PricingService` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:52`
- `ShoppingCartServiceImpl.productAttributeService: ProductAttributeService` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:55`
- `ShoppingCartServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:57`

## Functions and methods
- `ShoppingCartCalculationService.calculate(ShoppingCart, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationService.java:33`
- `ShoppingCartCalculationService.calculate(ShoppingCart, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationService.java:46`
- `ShoppingCartCalculationServiceImpl.calculate(ShoppingCart, Customer, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:65`
- `ShoppingCartCalculationServiceImpl.calculate(ShoppingCart, MerchantStore, Language) -> OrderTotalSummary` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:100`
- `ShoppingCartCalculationServiceImpl.getShoppingCartService() -> ShoppingCartService` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:113`
- `ShoppingCartCalculationServiceImpl.updateCartModel(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:117`
- `ShoppingCartService.getShoppingCart(Customer, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:17`
- `ShoppingCartService.saveOrUpdate(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:19`
- `ShoppingCartService.getById(Long, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:21`
- `ShoppingCartService.getByCode(String, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:23`
- `ShoppingCartService.createShippingProduct(ShoppingCart) -> List<ShippingProduct>` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:34`
- `ShoppingCartService.populateShoppingCartItem(Product, MerchantStore) -> ShoppingCartItem` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:43`
- `ShoppingCartService.deleteCart(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:45`
- `ShoppingCartService.removeShoppingCart(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:47`
- `ShoppingCartService.mergeShoppingCarts(ShoppingCart, ShoppingCart, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:57`
- `ShoppingCartService.deleteShoppingCartItem(Long) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartService.java:65`
- `ShoppingCartServiceImpl.getShoppingCart(Customer, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:69`
- `ShoppingCartServiceImpl.saveOrUpdate(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:103`
- `ShoppingCartServiceImpl.getById(Long, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:131`
- `ShoppingCartServiceImpl.getByCode(String, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:182`
- `ShoppingCartServiceImpl.deleteCart(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:208`
- `ShoppingCartServiceImpl.getPopulatedShoppingCart(ShoppingCart, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:230`
- `ShoppingCartServiceImpl.populateShoppingCartItem(Product, MerchantStore) -> ShoppingCartItem` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:276`
- `ShoppingCartServiceImpl.getPopulatedItem(ShoppingCartItem, MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:292`
- `ShoppingCartServiceImpl.createShippingProduct(ShoppingCart) -> List<ShippingProduct>` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:361`
- `ShoppingCartServiceImpl.removeShoppingCart(ShoppingCart) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:385`
- `ShoppingCartServiceImpl.mergeShoppingCarts(ShoppingCart, ShoppingCart, MerchantStore) -> ShoppingCart` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:390`
- `ShoppingCartServiceImpl.getShoppingCartItems(ShoppingCart, MerchantStore, ShoppingCart) -> Set<ShoppingCartItem>` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:440`
- `ShoppingCartServiceImpl.deleteShoppingCartItem(Long) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:491`

## Depends on
- [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartAttributeRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:48`
- [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartItemRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:45`
- [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:40`
- [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:51`
- [com.salesmanager.core.business.services.catalog.product.ProductService](/modules/com.salesmanager.core.business.services.catalog.product.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:42`
- [com.salesmanager.core.business.services.catalog.product.attribute.ProductAttributeService](/modules/com.salesmanager.core.business.services.catalog.product.attribute.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:54`
- [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:41`

## Calls
- `ShoppingCartCalculationServiceImpl.calculate` calls [com.salesmanager.core.business.services.order.OrderService](/modules/com.salesmanager.core.business.services.order.md) `OrderService.calculateShoppingCartTotal` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartCalculationServiceImpl.java:73`
- `ShoppingCartServiceImpl.deleteShoppingCartItem` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartAttributeRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartAttributeRepository.deleteById` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:499`
- `ShoppingCartServiceImpl.deleteShoppingCartItem` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartItemRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartItemRepository.deleteById`, `ShoppingCartItemRepository.findOne` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:507`
- `ShoppingCartServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:187`
- `ShoppingCartServiceImpl.getById` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartRepository.findById` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:136`
- `ShoppingCartServiceImpl.getPopulatedItem` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartAttributeRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartAttributeRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:342`
- `ShoppingCartServiceImpl.getPopulatedItem` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculateProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:352`
- `ShoppingCartServiceImpl.getShoppingCart` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartRepository.findByCustomer` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:75`
- `ShoppingCartServiceImpl.getShoppingCartItems` calls [com.salesmanager.core.model.shoppingcart.ShoppingCartItem](/modules/com.salesmanager.core.model.shoppingcart.md) `ShoppingCartItem.addAttributes` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:477`
- `ShoppingCartServiceImpl.populateShoppingCartItem` calls [com.salesmanager.core.business.services.catalog.pricing.PricingService](/modules/com.salesmanager.core.business.services.catalog.pricing.md) `PricingService.calculateProductPrice` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:286`
- `ShoppingCartServiceImpl.removeShoppingCart` calls [com.salesmanager.core.business.repositories.shoppingcart.ShoppingCartRepository](/modules/com.salesmanager.core.business.repositories.shoppingcart.md) `ShoppingCartRepository.delete` `sm-core/src/main/java/com/salesmanager/core/business/services/shoppingcart/ShoppingCartServiceImpl.java:387`
