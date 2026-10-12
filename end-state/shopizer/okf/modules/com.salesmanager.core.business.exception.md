---
type: Code Module
title: "com.salesmanager.core.business.exception"
description: "com.salesmanager.core.business.exception: ConversionException, ServiceException"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/business/exception/ConversionException.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/business/exception/ConversionException.java"
    sha256: "5e5f6232737ca8d5abca45cd0b1fd7849b500a9690639ebf7a60e5884e5e9f91"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java"
    sha256: "04cc93f03ed4441eb38875900e3aa4909ae4815296d0bee4f348f35a2f0c2cc0"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.exception

Source: `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ConversionException.java`, `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java`

## Types
- `ConversionException` (class) extends `Exception` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ConversionException.java:10`
- `ServiceException` (class) extends `Exception` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:6`

## Fields
- `ServiceException.exceptionType: int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:9`
- `ServiceException.EXCEPTION_ERROR: int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:12`
- `ServiceException.EXCEPTION_VALIDATION: int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:14`
- `ServiceException.EXCEPTION_PAYMENT_DECLINED: int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:15`
- `ServiceException.EXCEPTION_TRANSACTION_DECLINED: int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:16`
- `ServiceException.EXCEPTION_INVENTORY_MISMATCH: int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:17`
- `ServiceException.messageCode: String` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:19`

## Functions and methods
- `ServiceException.setMessageCode(String) -> void` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:23`
- `ServiceException.getExceptionType() -> int` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:60`
- `ServiceException.setExceptionType(int) -> void` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:64`
- `ServiceException.getMessageCode() -> String` `sm-core-model/src/main/java/com/salesmanager/core/business/exception/ServiceException.java:68`
