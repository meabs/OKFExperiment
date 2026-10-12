---
type: Code Module
title: "com.salesmanager.shop.filter"
description: "com.salesmanager.shop.filter: CorsFilter, XssFilter, XssHttpServletRequestWrapper"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/filter/CorsFilter.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/filter/CorsFilter.java"
    sha256: "4a8608ee839ae817e6c4bf17c0b977edd8ed5cc70f2e007593e654e182762c5f"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java"
    sha256: "d3b580f6462cd3e17ef48ca49fcd02ace3018d9d7bfbc576859a934d166b8de4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java"
    sha256: "366fd0a8e5dae47644c97e9619c1d414c9fa6ffdc54783d88c15f3074ed94316"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.shop.filter

Source: `sm-shop/src/main/java/com/salesmanager/shop/filter/CorsFilter.java`, `sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java`, `sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java`

## Types
- `CorsFilter` (class) extends `org.springframework.web.servlet.handler.HandlerInterceptorAdapter` `sm-shop/src/main/java/com/salesmanager/shop/filter/CorsFilter.java:17`
- `XssFilter` (class) `sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java:19`
- `XssHttpServletRequestWrapper` (class) extends `javax.servlet.http.HttpServletRequestWrapper` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java:13`

## Fields
- `XssFilter.LOGGER: Logger` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java:26`

## Functions and methods
- `CorsFilter.preHandle(HttpServletRequest, HttpServletResponse, Object) -> boolean` `sm-shop/src/main/java/com/salesmanager/shop/filter/CorsFilter.java:26`
- `XssFilter.init(FilterConfig) -> void` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java:28`
- `XssFilter.doFilter(ServletRequest, ServletResponse, FilterChain) -> void` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java:34`
- `XssFilter.destroy() -> void` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssFilter.java:44`
- `XssHttpServletRequestWrapper.getHeader(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java:22`
- `XssHttpServletRequestWrapper.getParameterValues(String) -> String[]` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java:31`
- `XssHttpServletRequestWrapper.getParameter(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java:44`
- `XssHttpServletRequestWrapper.cleanXSS(String) -> String` `sm-shop/src/main/java/com/salesmanager/shop/filter/XssHttpServletRequestWrapper.java:53`
