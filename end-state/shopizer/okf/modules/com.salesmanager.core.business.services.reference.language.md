---
type: Code Module
title: "com.salesmanager.core.business.services.reference.language"
description: "com.salesmanager.core.business.services.reference.language: LanguageServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java"
    sha256: "eb811d073ee52f96caf75b617d4345ec0077654fae31b634b839e3c66b1dadf4"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java"
    sha256: "a48bf6a7383a915f033ee8044714e20b1389caa2465ffd38ce3d2753d0db876b"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.reference.language

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java`

## Types
- `LanguageService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:12`
- `LanguageServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:29`

## Fields
- `LanguageServiceImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:33`
- `LanguageServiceImpl.cache: CacheUtils` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:36`
- `LanguageServiceImpl.languageRepository: LanguageRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:38`

## Functions and methods
- `LanguageService.getByCode(String) -> Language` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:14`
- `LanguageService.getLanguagesMap() -> Map<String, Language>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:16`
- `LanguageService.getLanguages() -> List<Language>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:18`
- `LanguageService.toLocale(Language, MerchantStore) -> Locale` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:20`
- `LanguageService.toLanguage(Locale) -> Language` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:22`
- `LanguageService.defaultLanguage() -> Language` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageService.java:24`
- `LanguageServiceImpl.getByCode(String) -> Language` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:47`
- `LanguageServiceImpl.toLocale(Language, MerchantStore) -> Locale` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:53`
- `LanguageServiceImpl.toLanguage(Locale) -> Language` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:68`
- `LanguageServiceImpl.getLanguagesMap() -> Map<String,Language>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:83`
- `LanguageServiceImpl.getLanguages() -> List<Language>` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:97`
- `LanguageServiceImpl.defaultLanguage() -> Language` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:122`

## Depends on
- [com.salesmanager.core.business.repositories.reference.language.LanguageRepository](/modules/com.salesmanager.core.business.repositories.reference.language.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:38`
- [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:35`

## Calls
- `LanguageServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.reference.language.LanguageRepository](/modules/com.salesmanager.core.business.repositories.reference.language.md) `LanguageRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:50`
- `LanguageServiceImpl.getLanguages` calls [com.salesmanager.core.business.utils.CacheUtils](/modules/com.salesmanager.core.business.utils.md) `CacheUtils.putInCache` `sm-core/src/main/java/com/salesmanager/core/business/services/reference/language/LanguageServiceImpl.java:110`
