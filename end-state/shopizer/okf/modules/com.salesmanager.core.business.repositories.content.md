---
type: Code Module
title: "com.salesmanager.core.business.repositories.content"
description: "com.salesmanager.core.business.repositories.content: ContentRepositoryImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java"
    sha256: "bf4cff9583b57fa44c11a724ce34cc9cd2e9e971c4bb2dbc6ae5603503f9f353"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryCustom.java"
    sha256: "f1ba99999ca72729dfcf64ec355f97b2a66b9075da23820fcd675054ae06bc82"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryImpl.java"
    sha256: "02e113df1c2401e9273211899cc9eebcd66d4b993d6fb94703e4e433c28c3304"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/content/PageContentRepository.java"
    sha256: "6a21274e08d8a4e6d4dde996e3542565d61d5d48e69147452918a122ca243bbf"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.content

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryCustom.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/PageContentRepository.java`

## Types
- `ContentRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository`, [com.salesmanager.core.business.repositories.content.ContentRepositoryCustom](/modules/com.salesmanager.core.business.repositories.content.md) `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:11`
- `ContentRepositoryCustom` (interface) `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryCustom.java:11`
- `ContentRepositoryImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryImpl.java:17`
- `PageContentRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/PageContentRepository.java:12`

## Fields
- `ContentRepositoryImpl.em: EntityManager` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryImpl.java:21`

## Functions and methods
- `ContentRepository.findByType(ContentType, Integer, Integer) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:14`
- `ContentRepository.findByType(ContentType, Integer) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:17`
- `ContentRepository.findByCodeAndType(String, ContentType, Integer) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:20`
- `ContentRepository.findByTypes(List<ContentType>, Integer, Integer) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:23`
- `ContentRepository.findByTypes(List<ContentType>, Integer) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:26`
- `ContentRepository.findByCode(String, Integer) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:29`
- `ContentRepository.findByCodeLike(ContentType, String, Integer, Integer) -> List<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:32`
- `ContentRepository.findByCode(String, Integer, Integer) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:35`
- `ContentRepository.findByIdAndLanguage(Long, Integer) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:38`
- `ContentRepository.findOne(Long) -> Content` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepository.java:41`
- `ContentRepositoryCustom.listNameByType(List<ContentType>, MerchantStore, Language) -> List<ContentDescription>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryCustom.java:13`
- `ContentRepositoryCustom.getBySeUrl(MerchantStore, String) -> ContentDescription` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryCustom.java:16`
- `ContentRepositoryImpl.listNameByType(List<ContentType>, MerchantStore, Language) -> List<ContentDescription>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryImpl.java:23`
- `ContentRepositoryImpl.getBySeUrl(MerchantStore, String) -> ContentDescription` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/ContentRepositoryImpl.java:65`
- `PageContentRepository.findByContentType(ContentType, Integer, Pageable) -> Page<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/PageContentRepository.java:16`
- `PageContentRepository.findByContentType(ContentType, Integer, Integer, Pageable) -> Page<Content>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/content/PageContentRepository.java:20`
