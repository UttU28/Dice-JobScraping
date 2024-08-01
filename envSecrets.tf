data "azurerm_key_vault_secret" "databaseServer" {
  name         = "databaseServer"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "databaseName" {
  name         = "databaseName"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "databaseUsername" {
  name         = "databaseUsername"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "databasePassword" {
  name         = "databasePassword"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "blobConnectionString" {
  name         = "blobConnectionString"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "databaseContainer" {
  name         = "databaseContainer"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "jobDataFile" {
  name         = "jobDataFile"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

data "azurerm_key_vault_secret" "rawDataFile" {
  name         = "rawDataFile"
  key_vault_id = data.azurerm_key_vault.thiskeyvault.id
}

locals {
  databaseServer              = data.azurerm_key_vault_secret.databaseServer.value
  databaseName                = data.azurerm_key_vault_secret.databaseName.value
  databaseUsername            = data.azurerm_key_vault_secret.databaseUsername.value
  databasePassword            = data.azurerm_key_vault_secret.databasePassword.value
  blobConnectionString        = data.azurerm_key_vault_secret.blobConnectionString.value
  databaseContainer           = data.azurerm_key_vault_secret.databaseContainer.value
  jobDataFile                 = data.azurerm_key_vault_secret.jobDataFile.value
  rawDataFile                 = data.azurerm_key_vault_secret.rawDataFile.value
}