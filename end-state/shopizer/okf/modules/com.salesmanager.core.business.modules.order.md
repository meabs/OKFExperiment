---
type: Code Module
title: "com.salesmanager.core.business.modules.order"
description: "com.salesmanager.core.business.modules.order: ODSInvoiceModule"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/InvoiceModule.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/InvoiceModule.java"
    sha256: "616e75b85489bdbe376d70bea8fbf2833bbebe6a57c9d6531f248b491363fe29"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java"
    sha256: "0c31a497c0da719979a4fb8942f680462b33f0e771a39825e73b9dd56752601d"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.order

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/order/InvoiceModule.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java`

## Types
- `InvoiceModule` (interface) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/InvoiceModule.java:10`
- `ODSInvoiceModule` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:21`

## Fields
- `ODSInvoiceModule.INVOICE_TEMPLATE: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:23`
- `ODSInvoiceModule.INVOICE_TEMPLATE_EXTENSION: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:24`
- `ODSInvoiceModule.TEMP_INVOICE_SUFFIX_NAME: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:25`
- `ODSInvoiceModule.ADDRESS_ROW_START: int` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:26`
- `ODSInvoiceModule.ADDRESS_ROW_END: int` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:27`
- `ODSInvoiceModule.BILLTO_ROW_START: int` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:29`
- `ODSInvoiceModule.BILLTO_ROW_END: int` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:30`
- `ODSInvoiceModule.PRODUCT_ROW_START: int` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:32`
- `ODSInvoiceModule.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:34`
- `ODSInvoiceModule.zoneService: ZoneService` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:37`
- `ODSInvoiceModule.countryService: CountryService` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:40`
- `ODSInvoiceModule.priceUtil: ProductPriceUtils` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:43`

## Functions and methods
- `InvoiceModule.createInvoice(MerchantStore, Order, Language) -> ByteArrayOutputStream` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/InvoiceModule.java:12`
- `ODSInvoiceModule.createInvoice(MerchantStore, Order, Language) -> ByteArrayOutputStream` `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:45`

## Depends on
- [com.salesmanager.core.business.services.reference.country.CountryService](/modules/com.salesmanager.core.business.services.reference.country.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:39`
- [com.salesmanager.core.business.services.reference.zone.ZoneService](/modules/com.salesmanager.core.business.services.reference.zone.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:36`
- [com.salesmanager.core.business.utils.ProductPriceUtils](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/modules/order/ODSInvoiceModule.java:42`
