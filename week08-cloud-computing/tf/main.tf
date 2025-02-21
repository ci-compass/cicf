# main.tf

# Provider configuration
provider "digitalocean" {
  token = var.do_token
}

# Variables
variable "do_token" {
  description = "Digital Ocean API token"
  type        = string
  sensitive   = true
}

variable "username" {
  description = "Default username for SSH access"
  type        = string
  default     = "debianuser"
}

variable "region" {
  description = "Digital Ocean region"
  type        = string
  default     = "nyc3"
}

variable "droplet_size" {
  description = "Droplet size slug"
  type        = string
  default     = "s-1vcpu-1gb"
}

variable "domain_name" {
  description = "Base domain name for subdomains"
  type        = string
}

variable "users" {
  description = "Map of users with their subdomains and SSH public keys"
  type = map(object({
    ssh_public_key = string
  }))
  validation {
    condition     = length(var.users) == 18
    error_message = "Exactly 18 users must be provided"
  }
}

# Resources
# Create SSH keys in Digital Ocean
resource "digitalocean_ssh_key" "droplet_key" {
  for_each   = var.users
  name       = "${each.key}-key"
  public_key = each.value.ssh_public_key
}

# Create Domain
resource "digitalocean_domain" "main_domain" {
  name = var.domain_name
}

# Create 18 Droplets
resource "digitalocean_droplet" "debian_droplet" {
  for_each = var.users
  name     = "${each.key}-droplet"
  region   = var.region
  size     = var.droplet_size
  image    = "debian-12-x64"
  ssh_keys = [digitalocean_ssh_key.droplet_key[each.key].id]

  user_data = <<-EOF
    #!/bin/bash
    useradd -m -s /bin/bash ${var.username}
    mkdir -p /home/${var.username}/.ssh
    echo "${each.value.ssh_public_key}" > /home/${var.username}/.ssh/authorized_keys
    chown -R ${var.username}:${var.username} /home/${var.username}/.ssh
    chmod 700 /home/${var.username}/.ssh
    chmod 600 /home/${var.username}/.ssh/authorized_keys
    usermod -aG sudo ${var.username}
    EOF
}

# Create DNS A records for each droplet
resource "digitalocean_record" "subdomain" {
  for_each = var.users
  domain   = digitalocean_domain.main_domain.name
  type     = "A"
  name     = each.key
  value    = digitalocean_droplet.debian_droplet[each.key].ipv4_address
  ttl      = 300
}

# Outputs
output "droplet_info" {
  value = {
    for subdomain, user in var.users : 
    subdomain => {
      ip        = digitalocean_droplet.debian_droplet[subdomain].ipv4_address
      subdomain = "${subdomain}.${var.domain_name}"
      ssh_key   = substr(user.ssh_public_key, 0, 20) # Partial key for reference
    }
  }
}
