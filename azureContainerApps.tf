terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }
  backend "azurerm" {
    resource_group_name  = "thisstoragerg"
    storage_account_name = "dicestorage02"
    container_name       = "13form"
    key                  = "datascrapingState"
  }
}


resource "azurerm_resource_group" "resource_group" {
  name     = local.jobscraping-rg
  location = local.general-location
}

# resource "azurerm_log_analytics_workspace" "analytics_workspace" {
#   name                = "dicesaralapplyloganalyticsworkspace"
#   location            = azurerm_resource_group.resource_group.location
#   resource_group_name = azurerm_resource_group.resource_group.name
#   sku                 = "PerGB2018"
#   retention_in_days   = 30
# }

resource "azurerm_container_app_environment" "app_environment" {
  name                = local.jobscraping-app-environment
  location            = azurerm_resource_group.resource_group.location
  resource_group_name = azurerm_resource_group.resource_group.name
}

resource "azurerm_container_app_job" "job" {

  name                         = local.jobscraping-name
  location                     = azurerm_resource_group.resource_group.location
  container_app_environment_id = azurerm_container_app_environment.app_environment.id
  resource_group_name          = azurerm_resource_group.resource_group.name
  replica_timeout_in_seconds   = 300
  # Job scheduling: every 20 minutes, from 7 AM to 5 PM CT
  schedule_trigger_config {
    cron_expression = "*/20 12-23 * * *" # Converts to CT with UTC offset (-5 in Standard Time)
  }

  template {
    container {
      name   = "${local.acrName}-random-string"
      image  = local.acrUrl
      cpu    = 0.75
      memory = "1.5Gi"

      env {
        name  = "databaseServer"
        value = local.databaseServer
      }
      env {
        name  = "databaseName"
        value = local.databaseName
      }
      env {
        name  = "databaseUsername"
        value = local.databaseUsername
      }
      env {
        name  = "databasePassword"
        value = local.databasePassword
      }
      env {
        name  = "blobConnectionString"
        value = local.blobConnectionString
      }
      env {
        name  = "databaseContainer"
        value = local.databaseContainer
      }
      env {
        name  = "jobDataFile"
        value = local.jobDataFile
      }
      env {
        name  = "rawDataFile"
        value = local.rawDataFile
      }
    }
  }

  registry {
    server               = "${local.acrName}.azurecr.io"
    username             = local.acrName
    password_secret_name = "registry-credentials"
  }
}


# output "azurerm_container_app_url" {
#   value = azurerm_container_app.app.latest_revision_fqdn
# }

# output "azurerm_container_app_revision_name" {
#   value = azurerm_container_app.app.latest_revision_name

# }
