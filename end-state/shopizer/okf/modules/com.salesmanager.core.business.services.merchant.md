---
type: Code Module
title: "com.salesmanager.core.business.services.merchant"
description: "com.salesmanager.core.business.services.merchant: MerchantStoreServiceImpl"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java"
    sha256: "e84dc7be8491fefd2699245ea68a6a0fafe8fb77571c1483663b0b9dd7e42d2c"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java"
    sha256: "995420994d9376ceb19d80492c3738afb438479ccf2bed4483bcb8c48ecd7906"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.services.merchant

Source: `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java`, `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java`

## Types
- `MerchantStoreService` (interface) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityService](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:14`
- `MerchantStoreServiceImpl` (class) extends [com.salesmanager.core.business.services.common.generic.SalesManagerEntityServiceImpl](/modules/com.salesmanager.core.business.services.common.generic.md) `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:24`

## Fields
- `MerchantStoreServiceImpl.productTypeService: ProductTypeService` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:29`
- `MerchantStoreServiceImpl.pageableMerchantRepository: PageableMerchantRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:32`
- `MerchantStoreServiceImpl.merchantRepository: MerchantRepository` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:34`

## Functions and methods
- `MerchantStoreService.getByCode(String) -> MerchantStore` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:17`
- `MerchantStoreService.getParent(String) -> MerchantStore` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:19`
- `MerchantStoreService.findAllStoreNames() -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:21`
- `MerchantStoreService.findAllStoreNames(String) -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:23`
- `MerchantStoreService.findAllStoreCodeNameEmail() -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:25`
- `MerchantStoreService.listAll(Optional<String>, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:27`
- `MerchantStoreService.listByGroup(Optional<String>, String, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:29`
- `MerchantStoreService.listAllRetailers(Optional<String>, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:31`
- `MerchantStoreService.listChildren(String, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:33`
- `MerchantStoreService.existByCode(String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:35`
- `MerchantStoreService.isStoreInGroup(String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:42`
- `MerchantStoreService.saveOrUpdate(MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:44`
- `MerchantStoreService.getByCriteria(MerchantStoreCriteria) -> GenericEntityList<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreService.java:46`
- `MerchantStoreServiceImpl.saveOrUpdate(MerchantStore) -> void` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:42`
- `MerchantStoreServiceImpl.getByCode(String) -> MerchantStore` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:48`
- `MerchantStoreServiceImpl.existByCode(String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:57`
- `MerchantStoreServiceImpl.getByCriteria(MerchantStoreCriteria) -> GenericEntityList<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:62`
- `MerchantStoreServiceImpl.listChildren(String, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:67`
- `MerchantStoreServiceImpl.listAll(Optional<String>, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:73`
- `MerchantStoreServiceImpl.findAllStoreCodeNameEmail() -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:84`
- `MerchantStoreServiceImpl.listAllRetailers(Optional<String>, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:89`
- `MerchantStoreServiceImpl.findAllStoreNames() -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:101`
- `MerchantStoreServiceImpl.getParent(String) -> MerchantStore` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:106`
- `MerchantStoreServiceImpl.findAllStoreNames(String) -> List<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:130`
- `MerchantStoreServiceImpl.listByGroup(Optional<String>, String, int, int) -> Page<MerchantStore>` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:142`
- `MerchantStoreServiceImpl.isStoreInGroup(String) -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:163`

## Depends on
- [com.salesmanager.core.business.repositories.merchant.MerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:34`
- [com.salesmanager.core.business.repositories.merchant.PageableMerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:31`
- [com.salesmanager.core.business.services.catalog.product.type.ProductTypeService](/modules/com.salesmanager.core.business.services.catalog.product.type.md) `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:28`

## Calls
- `MerchantStoreServiceImpl.existByCode` calls [com.salesmanager.core.business.repositories.merchant.MerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `MerchantRepository.existsByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:59`
- `MerchantStoreServiceImpl.findAllStoreCodeNameEmail` calls [com.salesmanager.core.business.repositories.merchant.MerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `MerchantRepository.findAllStoreCodeNameEmail` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:86`
- `MerchantStoreServiceImpl.findAllStoreNames` calls [com.salesmanager.core.business.repositories.merchant.MerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `MerchantRepository.findAllStoreNames` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:103`
- `MerchantStoreServiceImpl.getByCode` calls [com.salesmanager.core.business.repositories.merchant.MerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `MerchantRepository.findByCode` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:54`
- `MerchantStoreServiceImpl.getByCriteria` calls [com.salesmanager.core.business.repositories.merchant.MerchantRepositoryCustom](/modules/com.salesmanager.core.business.repositories.merchant.md) `MerchantRepositoryCustom.listByCriteria` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:64`
- `MerchantStoreServiceImpl.isStoreInGroup` calls [com.salesmanager.core.business.repositories.merchant.MerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `MerchantRepository.listByGroup` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:169`
- `MerchantStoreServiceImpl.listAll` calls [com.salesmanager.core.business.repositories.merchant.PageableMerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `PageableMerchantRepository.listAll` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:80`
- `MerchantStoreServiceImpl.listAllRetailers` calls [com.salesmanager.core.business.repositories.merchant.PageableMerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `PageableMerchantRepository.listAllRetailers` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:97`
- `MerchantStoreServiceImpl.listByGroup` calls [com.salesmanager.core.business.repositories.merchant.PageableMerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `PageableMerchantRepository.listByGroup` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:158`
- `MerchantStoreServiceImpl.listChildren` calls [com.salesmanager.core.business.repositories.merchant.PageableMerchantRepository](/modules/com.salesmanager.core.business.repositories.merchant.md) `PageableMerchantRepository.listByStore` `sm-core/src/main/java/com/salesmanager/core/business/services/merchant/MerchantStoreServiceImpl.java:70`
