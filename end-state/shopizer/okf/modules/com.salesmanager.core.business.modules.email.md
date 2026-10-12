---
type: Code Module
title: "com.salesmanager.core.business.modules.email"
description: "com.salesmanager.core.business.modules.email: DefaultEmailSenderImpl, Email, EmailComponent, EmailConfig"
resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java"
tags: ["generated", "code"]
generated:
  by: "kgen/0.4.0"
  at: "2025-03-23T12:16:56-04:00"
sources:
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java"
    sha256: "88880ec0948595714bc9b993ccda82069bc928c64eb05739e0b2a45fd41d0b45"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java"
    sha256: "c58ad55c8f54e52d004e4ec62760e06f34ea97658bf10b90c95e174279937cd6"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java"
    sha256: "398ff81889cb71fd00d06f4228a6bcc939bfc6d308294afc86206c84f2e63718"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java"
    sha256: "4cb5acab683442cd59cf55955d24efd2a109a562cab292f051e630cf94227800"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailModule.java"
    sha256: "95d562f9143209178dc0b8c7f1de722865fdc999a4e0104b345fb4599dd825e3"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/HtmlEmailSender.java"
    sha256: "0f490d520e487648391379d802ca3445e1d92bfa85ed4da3ffaf854199cec509"
    last_modified: "2025-03-23T12:16:56-04:00"
  - resource: "https://github.com/shopizer-ecommerce/shopizer/blob/6a4a0a65a3408ee8f62597b51d1b3aac24b77dee/sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java"
    sha256: "1743dc3fd35c7fed34a039fbeb5c284b0e735dae4e249ba368055e1551db1ae1"
    last_modified: "2025-03-23T12:16:56-04:00"
status: stable
---

# com.salesmanager.core.business.modules.email

Source: `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailModule.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/email/HtmlEmailSender.java`, `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java`

## Types
- `DefaultEmailSenderImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:28`
- `Email` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:7`
- `EmailComponent` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java:7`
- `EmailConfig` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:6`
- `EmailModule` (interface) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailModule.java:3`
- `HtmlEmailSender` (interface) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/HtmlEmailSender.java:4`
- `SESEmailSenderImpl` (class) `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:27`

## Fields
- `DefaultEmailSenderImpl.freemarkerMailConfiguration: Configuration` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:32`
- `DefaultEmailSenderImpl.mailSender: JavaMailSender` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:35`
- `DefaultEmailSenderImpl.CHARSET: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:37`
- `DefaultEmailSenderImpl.emailConfig: EmailConfig` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:38`
- `DefaultEmailSenderImpl.TEMPLATE_PATH: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:40`
- `Email.from: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:14`
- `Email.fromEmail: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:15`
- `Email.to: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:16`
- `Email.subject: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:17`
- `Email.templateName: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:18`
- `Email.templateTokens: Map<String,String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:20`
- `EmailComponent.emailSender: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java:11`
- `EmailComponent.defaultEmailSender: EmailModule` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java:14`
- `EmailComponent.sesEmailSender: EmailModule` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java:17`
- `EmailConfig.host: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:8`
- `EmailConfig.port: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:9`
- `EmailConfig.protocol: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:10`
- `EmailConfig.username: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:11`
- `EmailConfig.password: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:12`
- `EmailConfig.smtpAuth: boolean` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:13`
- `EmailConfig.starttls: boolean` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:14`
- `EmailConfig.emailTemplatesPath: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:16`
- `SESEmailSenderImpl.freemarkerMailConfiguration: Configuration` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:31`
- `SESEmailSenderImpl.region: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:34`
- `SESEmailSenderImpl.TEMPLATE_PATH: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:36`
- `SESEmailSenderImpl.TEXTBODY: String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:45`

## Functions and methods
- `DefaultEmailSenderImpl.send(Email) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:42`
- `DefaultEmailSenderImpl.getFreemarkerMailConfiguration() -> Configuration` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:164`
- `DefaultEmailSenderImpl.setFreemarkerMailConfiguration(Configuration) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:168`
- `DefaultEmailSenderImpl.getMailSender() -> JavaMailSender` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:172`
- `DefaultEmailSenderImpl.setMailSender(JavaMailSender) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:176`
- `DefaultEmailSenderImpl.getEmailConfig() -> EmailConfig` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:180`
- `DefaultEmailSenderImpl.setEmailConfig(EmailConfig) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/DefaultEmailSenderImpl.java:184`
- `Email.getFrom() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:22`
- `Email.setFrom(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:26`
- `Email.getTo() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:30`
- `Email.setTo(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:34`
- `Email.getSubject() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:38`
- `Email.setSubject(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:42`
- `Email.getTemplateName() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:46`
- `Email.setTemplateName(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:50`
- `Email.getTemplateTokens() -> Map<String, String>` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:54`
- `Email.setTemplateTokens(Map<String, String>) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:58`
- `Email.setFromEmail(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:62`
- `Email.getFromEmail() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/Email.java:66`
- `EmailComponent.send(Email) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java:19`
- `EmailComponent.setEmailConfig(EmailConfig) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailComponent.java:35`
- `EmailConfig.toJSONString() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:18`
- `EmailConfig.isSmtpAuth() -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:34`
- `EmailConfig.setSmtpAuth(boolean) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:37`
- `EmailConfig.isStarttls() -> boolean` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:40`
- `EmailConfig.setStarttls(boolean) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:43`
- `EmailConfig.setEmailTemplatesPath(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:46`
- `EmailConfig.getEmailTemplatesPath() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:49`
- `EmailConfig.getHost() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:55`
- `EmailConfig.setHost(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:61`
- `EmailConfig.getPort() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:67`
- `EmailConfig.setPort(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:73`
- `EmailConfig.getProtocol() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:79`
- `EmailConfig.setProtocol(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:85`
- `EmailConfig.getUsername() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:91`
- `EmailConfig.setUsername(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:97`
- `EmailConfig.getPassword() -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:103`
- `EmailConfig.setPassword(String) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailConfig.java:109`
- `EmailModule.send(Email) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailModule.java:5`
- `EmailModule.setEmailConfig(EmailConfig) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/EmailModule.java:7`
- `HtmlEmailSender.send(Email) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/HtmlEmailSender.java:6`
- `HtmlEmailSender.setEmailConfig(EmailConfig) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/HtmlEmailSender.java:8`
- `SESEmailSenderImpl.send(Email) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:48`
- `SESEmailSenderImpl.prepareHtml(Email) -> String` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:76`
- `SESEmailSenderImpl.setEmailConfig(EmailConfig) -> void` `sm-core/src/main/java/com/salesmanager/core/business/modules/email/SESEmailSenderImpl.java:93`
