---
type: Code Module
title: "com.salesmanager.shop.store.api.v0.system"
description: "com.salesmanager.shop.store.api.v0.system: SystemRESTController; 4 route(s)"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java"
    sha256: "6ccba9ad97a4d855ec625f7c0ff4be1b63c782a0e683ebd40e6a036d9e54f051"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.store.api.v0.system

Source: `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java`

## Types
- `SystemRESTController` (class) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:25`

## Fields
- `SystemRESTController.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:31`
- `SystemRESTController.moduleConfigurationService: ModuleConfigurationService` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:34`

## Functions and methods
- `SystemRESTController.createOrUpdateModule(String, HttpServletRequest, HttpServletResponse) -> AjaxResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:58`
- `SystemRESTController.createOptin(String, HttpServletRequest, HttpServletResponse) -> AjaxResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:87`
- `SystemRESTController.deleteOptin(String, HttpServletRequest, HttpServletResponse) -> AjaxResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:110`
- `SystemRESTController.createOptinCustomer(String, HttpServletRequest, HttpServletResponse) -> AjaxResponse` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:133`

## HTTP routes
- `POST /services/private/system/module` handled by `com.salesmanager.shop.store.api.v0.system.SystemRESTController#createOrUpdateModule` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:58`
- `POST /services/private/system/optin` handled by `com.salesmanager.shop.store.api.v0.system.SystemRESTController#createOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:87`
- `DELETE /services/private/system/optin/{code}` handled by `com.salesmanager.shop.store.api.v0.system.SystemRESTController#deleteOptin` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:110`
- `POST /services/private/system/optin/{code}/customer` handled by `com.salesmanager.shop.store.api.v0.system.SystemRESTController#createOptinCustomer` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:133`

## Depends on
- [com.salesmanager.core.business.services.system.ModuleConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:33`

## Calls
- `SystemRESTController.createOrUpdateModule` calls [com.salesmanager.core.business.services.system.ModuleConfigurationService](/modules/com.salesmanager.core.business.services.system.md) `ModuleConfigurationService.createOrUpdateModule` `sm-shop/src/main/java/com/salesmanager/shop/store/api/v0/system/SystemRESTController.java:71`
