---
type: Code Module
title: "com.salesmanager.core.business.repositories.merchant"
description: "com.salesmanager.core.business.repositories.merchant: MerchantRepositoryImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java"
    sha256: "49ca70645f3babf62173d40b6f4ae54d93729311ab9c56732c0aa83640362236"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryCustom.java"
    sha256: "81a759c4ce6d67c23a4493d558d6aee17af28db7671e47d6930433646f6e4ab9"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java"
    sha256: "fd9155d8ab5cf1c3523e19552c341c704da53889b906bd63d95571dd16af7b85"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java"
    sha256: "7992caac9e1abc6b2fcf60b2591fa39e82afc93a8cc3cb78eb7ed13692ed9fe3"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.repositories.merchant

Source: `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryCustom.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java`

## Types
- `MerchantRepository` (interface) extends `org.springframework.data.jpa.repository.JpaRepository`, [com.salesmanager.core.business.repositories.merchant.MerchantRepositoryCustom](/modules/com.salesmanager.core.business.repositories.merchant.md) `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:10`
- `MerchantRepositoryCustom` (interface) `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryCustom.java:8`
- `MerchantRepositoryImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java:19`
- `PageableMerchantRepository` (interface) extends `org.springframework.data.repository.PagingAndSortingRepository` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java:10`

## Fields
- `MerchantRepositoryImpl.em: EntityManager` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java:22`
- `MerchantRepositoryImpl.LOGGER: Logger` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java:24`

## Functions and methods
- `MerchantRepository.findByCode(String) -> MerchantStore` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:13`
- `MerchantRepository.getById(int) -> MerchantStore` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:22`
- `MerchantRepository.getByParent(String) -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:26`
- `MerchantRepository.existsByCode(String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:29`
- `MerchantRepository.findAllStoreNames() -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:32`
- `MerchantRepository.findAllStoreNames(String) -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:35`
- `MerchantRepository.findAllStoreNames(List<String>) -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:39`
- `MerchantRepository.findAllStoreCodeNameEmail() -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:43`
- `MerchantRepository.listByGroup(String, Integer) -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepository.java:46`
- `MerchantRepositoryCustom.listByCriteria(MerchantStoreCriteria) -> GenericEntityList<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryCustom.java:10`
- `MerchantRepositoryImpl.listByCriteria(MerchantStoreCriteria) -> GenericEntityList` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java:27`
- `PageableMerchantRepository.listByStore(String, Pageable) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java:15`
- `PageableMerchantRepository.listAll(String, Pageable) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java:18`
- `PageableMerchantRepository.listAllRetailers(String, Pageable) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java:21`
- `PageableMerchantRepository.listChilds(String, String, Pageable) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java:28`
- `PageableMerchantRepository.listByGroup(String, Integer, String, Pageable) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/PageableMerchantRepository.java:35`

## Calls
- `MerchantRepositoryImpl.listByCriteria` calls [com.salesmanager.core.business.utils.RepositoryHelper](/modules/com.salesmanager.core.business.utils.md) `RepositoryHelper.paginateQuery` `sm-core/src/main/java/com/salesmanager/core/business/repositories/merchant/MerchantRepositoryImpl.java:77`
