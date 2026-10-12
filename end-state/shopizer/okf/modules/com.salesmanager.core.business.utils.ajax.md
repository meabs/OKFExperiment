---
type: Code Module
title: "com.salesmanager.core.business.utils.ajax"
description: "com.salesmanager.core.business.utils.ajax: AjaxPageableResponse, AjaxResponse"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java"
    sha256: "326393fc0572f037d981c2be11c97ec4220c493f36101b0bfbb92cce98d8ae4e"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java"
    sha256: "6f478d6c30baae3508d3be95999c186510cacfd40cd306e9cdaeb89f91e3c661"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.utils.ajax

Source: `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java`, `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java`

## Types
- `AjaxPageableResponse` (class) extends [com.salesmanager.core.business.utils.ajax.AjaxResponse](/modules/com.salesmanager.core.business.utils.ajax.md) `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:8`
- `AjaxResponse` (class) `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:13`

## Fields
- `AjaxPageableResponse.startRow: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:11`
- `AjaxPageableResponse.endRow: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:24`
- `AjaxPageableResponse.totalRow: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:25`
- `AjaxResponse.RESPONSE_STATUS_SUCCESS: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:15`
- `AjaxResponse.RESPONSE_STATUS_FAIURE: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:16`
- `AjaxResponse.RESPONSE_STATUS_VALIDATION_FAILED: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:17`
- `AjaxResponse.RESPONSE_OPERATION_COMPLETED: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:18`
- `AjaxResponse.CODE_ALREADY_EXIST: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:19`
- `AjaxResponse.status: int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:21`
- `AjaxResponse.data: List<Map<String,String>>` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:22`
- `AjaxResponse.dataMap: Map<String,String>` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:23`
- `AjaxResponse.validationMessages: Map<String,String>` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:24`
- `AjaxResponse.statusMessage: String` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:63`

## Functions and methods
- `AjaxPageableResponse.getStartRow() -> int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:12`
- `AjaxPageableResponse.setStartRow(int) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:18`
- `AjaxPageableResponse.getPageInfo() -> String` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:27`
- `AjaxPageableResponse.toJSONString() -> String` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:40`
- `AjaxPageableResponse.getEndRow() -> int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:86`
- `AjaxPageableResponse.setEndRow(int) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:92`
- `AjaxPageableResponse.getTotalRow() -> int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:98`
- `AjaxPageableResponse.setTotalRow(int) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxPageableResponse.java:104`
- `AjaxResponse.getValidationMessages() -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:25`
- `AjaxResponse.setValidationMessages(Map<String, String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:28`
- `AjaxResponse.getStatus() -> int` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:31`
- `AjaxResponse.setStatus(int) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:34`
- `AjaxResponse.getData() -> List<Map<String,String>>` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:37`
- `AjaxResponse.addDataEntry(Map<String,String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:41`
- `AjaxResponse.addEntry(String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:45`
- `AjaxResponse.setErrorMessage(Throwable) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:50`
- `AjaxResponse.setErrorString(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:54`
- `AjaxResponse.addValidationMessage(String, String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:59`
- `AjaxResponse.getStatusMessage() -> String` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:66`
- `AjaxResponse.setStatusMessage(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:69`
- `AjaxResponse.getJsonInfo() -> String` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:74`
- `AjaxResponse.toJSONString() -> String` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:88`
- `AjaxResponse.getDataMap() -> Map<String,String>` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:179`
- `AjaxResponse.setDataMap(Map<String,String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/utils/ajax/AjaxResponse.java:182`
