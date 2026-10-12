---
type: Code Module
title: "com.salesmanager.shop.validation"
description: "com.salesmanager.shop.validation: BeanUtils, EnumValidator, FieldMatchValidator"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java"
    sha256: "ddeab4f2728db6e76eccea6f8bba8ee609f7e643f9f3823da145ecdc1f81c253"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/validation/Enum.java"
    sha256: "41d37601b23f3e86f9f356061cb408ed4b6104d9f869415652bb05554e28589a"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/validation/EnumValidator.java"
    sha256: "7480e1a9c4c261eb0a65ececf6e2048407045c4f309df6fc636e51f906567926"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatch.java"
    sha256: "aa1a02b6c95deaf3eb91155ddb8b5183ebc6281787df72b3b0b935f477ae121b"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java"
    sha256: "c203a7cc26d55a4a40af6b0a64469adcef9a249659561f67a1fdf316bb491848"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.validation

Source: `sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/validation/Enum.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/validation/EnumValidator.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatch.java`, `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java`

## Types
- `BeanUtils` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java:10`
- `Enum` (annotation) `sm-shop-model/src/main/java/com/salesmanager/shop/validation/Enum.java:12`
- `EnumValidator` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/validation/EnumValidator.java:13`
- `FieldMatch` (annotation) `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatch.java:35`
- `List` (annotation) `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatch.java:63`
- `FieldMatchValidator` (class) `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:9`

## Fields
- `EnumValidator.annotation: Enum` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/EnumValidator.java:15`
- `FieldMatchValidator.LOG: Logger` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:12`
- `FieldMatchValidator.firstFieldName: String` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:13`
- `FieldMatchValidator.secondFieldName: String` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:14`
- `FieldMatchValidator.beanUtils: BeanUtils` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:15`

## Functions and methods
- `BeanUtils.newInstance() -> BeanUtils` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java:16`
- `BeanUtils.getPropertyValue(Object, String) -> Object` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java:20`
- `BeanUtils.getPropertyDescriptor(Class<?>, String) -> PropertyDescriptor` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/BeanUtils.java:47`
- `EnumValidator.initialize(Enum) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/EnumValidator.java:18`
- `EnumValidator.isValid(String, ConstraintValidatorContext) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/EnumValidator.java:24`
- `FieldMatchValidator.initialize(FieldMatch) -> void` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:17`
- `FieldMatchValidator.isValid(Object, ConstraintValidatorContext) -> boolean` `sm-shop-model/src/main/java/com/salesmanager/shop/validation/FieldMatchValidator.java:24`
