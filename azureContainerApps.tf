provider "azurerm" {
  features {
    
  }
}

resource "azurerm_resource_group" "resource_group" {
  name     = "thatresourcegroup"
  location = "East US"
}

# resource "azurerm_log_analytics_workspace" "analytics_workspace" {
#   name                = "dicesaralapplyloganalyticsworkspace"
#   location            = azurerm_resource_group.resource_group.location
#   resource_group_name = azurerm_resource_group.resource_group.name
#   sku                 = "PerGB2018"
#   retention_in_days   = 30
# }

resource "azurerm_container_app_environment" "app_environment" {
  name                       = "dicesaralapplycontainerenvi"
  location                   = azurerm_resource_group.resource_group.location
  resource_group_name        = azurerm_resource_group.resource_group.name
#   log_analytics_workspace_id = azurerm_log_analytics_workspace.analytics_workspace.id
}
resource "azurerm_container_app" "app" {
  name                         = "dicesaralapply"
  container_app_environment_id = azurerm_container_app_environment.app_environment.id
  resource_group_name          = azurerm_resource_group.resource_group.name
  revision_mode                = "Single"
  
  secret {
    name  = "registry-credentials"
    value = "U9+ivfherZPq3+UWDnj1fxftpOqWUgXqspIc90YYFI+ACRBkerUy"
  }
  template {
    container {
      name   = "dicesaralapply112"
      image  = "thisacr.azurecr.io/imagename:latest"
      cpu    = 0.75
      memory = "1.5Gi"
    }
  }
  registry {
    server = "thisacr.azurecr.io"
    username = "thisacr"
    password_secret_name = "registry-credentials"
  }
  ingress {
     allow_insecure_connections = false
     target_port = 50505
     traffic_weight {
      percentage = 100
      latest_revision = true
     }
     external_enabled = true
   }
}

# output "azurerm_container_app_url" {
#   value = azurerm_container_app.app.latest_revision_fqdn
# }

# output "azurerm_container_app_revision_name" {
#   value = azurerm_container_app.app.latest_revision_name
  
# }