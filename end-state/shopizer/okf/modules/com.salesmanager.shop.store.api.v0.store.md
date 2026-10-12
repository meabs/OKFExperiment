---
type: Code Module
title: "com.salesmanager.shop.store.api.v0.store"
description: "com.salesmanager.shop.store.api.v0.store: StoreContactRESTController; 2 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java"
    sha256: "4555d3a7c1faca3b5e62c851f80311a7229dd12607c22e498bcedd625c9af5ae"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v0.store

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java`

## Types
- `StoreContactRESTController` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:42`

## Fields
- `StoreContactRESTController.languageService: LanguageService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:47`
- `StoreContactRESTController.merchantStoreService: MerchantStoreService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:50`
- `StoreContactRESTController.emailTemplatesUtils: EmailTemplatesUtils` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:53`
- `StoreContactRESTController.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:57`

## Functions and methods
- `StoreContactRESTController.store(String, HttpServletRequest, HttpServletResponse) -> AjaxResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:61`
- `StoreContactRESTController.contact(String, ContactForm, HttpServletRequest, HttpServletResponse) -> AjaxResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:107`

## HTTP routes
- `GET /services/public/{store}` handled by `com.salesmanager.shop.store.api.v0.store.StoreContactRESTController#store` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:61`
- `POST /services/public/{store}/contact` handled by `com.salesmanager.shop.store.api.v0.store.StoreContactRESTController#contact` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:107`

## Depends on
- [com.salesmanager.core.business.services.merchant.MerchantStoreService](/modules/com.salesmanager.core.business.services.merchant.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:49`
- [com.salesmanager.core.business.services.reference.language.LanguageService](/modules/com.salesmanager.core.business.services.reference.language.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:46`
- [com.salesmanager.shop.utils.EmailTemplatesUtils](/modules/com.salesmanager.shop.utils.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:52`

## Calls
- `StoreContactRESTController.contact` calls [com.salesmanager.shop.utils.EmailTemplatesUtils](/modules/com.salesmanager.shop.utils.md) `EmailTemplatesUtils.sendContactEmail` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/store/StoreContactRESTController.java:156`
