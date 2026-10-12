---
type: Code Module
title: "com.salesmanager.core.model.tax.taxclass"
description: "com.salesmanager.core.model.tax.taxclass: TaxClass"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java"
    sha256: "82eb7029873198f53d686054a39c53590132eb9405b571d76b5750ee871f08a9"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.model.tax.taxclass

Source: `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java`

## Types
- `TaxClass` (class) extends [com.salesmanager.core.model.generic.SalesManagerEntity](/modules/com.salesmanager.core.model.generic.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:28`

## Fields
- `TaxClass.DEFAULT_TAX_CLASS: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:38`
- `TaxClass.id: Long` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:49`
- `TaxClass.code: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:53`
- `TaxClass.title: String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:57`
- `TaxClass.products: List<Product>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:62`
- `TaxClass.merchantStore: MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:67`
- `TaxClass.taxRates: List<TaxRate>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:71`

## Functions and methods
- `TaxClass.getId() -> Long` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:77`
- `TaxClass.setId(Long) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:82`
- `TaxClass.getTitle() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:88`
- `TaxClass.setTitle(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:92`
- `TaxClass.getCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:96`
- `TaxClass.setCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:100`
- `TaxClass.getTaxRates() -> List<TaxRate>` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:104`
- `TaxClass.setTaxRates(List<TaxRate>) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:108`
- `TaxClass.getMerchantStore() -> MerchantStore` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:113`
- `TaxClass.setMerchantStore(MerchantStore) -> void` `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:117`

## Depends on
- [com.salesmanager.core.model.catalog.product.Product](/modules/com.salesmanager.core.model.catalog.product.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:61`
- [com.salesmanager.core.model.merchant.MerchantStore](/modules/com.salesmanager.core.model.merchant.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:65`
- [com.salesmanager.core.model.tax.taxrate.TaxRate](/modules/com.salesmanager.core.model.tax.taxrate.md) `sm-core-model/src/main/java/com/salesmanager/core/model/tax/taxclass/TaxClass.java:70`
