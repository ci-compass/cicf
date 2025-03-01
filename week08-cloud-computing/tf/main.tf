# main.tf

terraform {
  required_version = ">= 1.0"
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# Provider configuration
provider "digitalocean" {
  token             = var.do_token
  spaces_access_id  = var.do_spaces_access_id
  spaces_secret_key = var.do_spaces_secret_key
}

# Variables
variable "do_token" {
  description = "Digital Ocean API token"
  type        = string
  sensitive   = true
}

variable "do_spaces_access_id" {
  description = "Digital Ocean Spaces access ID"
  type        = string
  sensitive   = true
}

variable "do_spaces_secret_key" {
  description = "Digital Ocean Spaces secret key"
  type        = string
  sensitive   = true
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
  # validation {
  #   condition     = length(var.users) == 18
  #   error_message = "Exactly 18 users must be provided"
  # }
}

variable "admin_ssh_keys" {
  description = "Map of admin members and their SSH public keys"
  type        = map(string)
  validation {
    condition     = length(var.admin_ssh_keys) > 0
    error_message = "At least one admin SSH public key must be provided"
  }
}

variable "space_name" {
  description = "Name of the Digital Ocean Space"
  type        = string
  default     = "my-object-store"
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
    # Create user with subdomain name and set up SSH
    useradd -m -s /bin/bash ${each.key}
    mkdir -p /home/${each.key}/.ssh
    echo "${each.value.ssh_public_key}" > /home/${each.key}/.ssh/authorized_keys
    chown -R ${each.key}:${each.key} /home/${each.key}/.ssh
    chmod 700 /home/${each.key}/.ssh
    chmod 600 /home/${each.key}/.ssh/authorized_keys
    usermod -aG sudo ${each.key}

    # Create admin user and set up SSH
    useradd -m -s /bin/bash admin
    mkdir -p /home/admin/.ssh
    cat << 'ADMIN_KEYS' > /home/admin/.ssh/authorized_keys
    ${join("\n", values(var.admin_ssh_keys))}
    ADMIN_KEYS
    chown -R admin:admin /home/admin/.ssh
    chmod 700 /home/admin/.ssh
    chmod 600 /home/admin/.ssh/authorized_keys
    usermod -aG sudo admin

    # Disable password login in SSH configuration
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
    sed -i 's/#ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config

    # Ensure these settings are explicitly set
    echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
    echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
    echo "ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config

    # Restart SSH service to apply changes
    systemctl restart sshd
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

# Create a Digital Ocean Space (Object Storage)
resource "digitalocean_spaces_bucket" "object_store" {
  name   = var.space_name
  region = var.region
  acl    = "public-read"

  versioning {
    enabled = true
  }
}

# Outputs
output "droplet_info" {
  value = {
    for subdomain, user in var.users :
    subdomain => {
      ip        = digitalocean_droplet.debian_droplet[subdomain].ipv4_address
      subdomain = "${subdomain}.${var.domain_name}"
      ssh_key   = substr(user.ssh_public_key, 0, 20)
      username  = subdomain
    }
  }
}

output "admin_info" {
  value = {
    username  = "admin"
    ssh_keys  = { for admin_id, key in var.admin_ssh_keys : admin_id => substr(key, 0, 20) }
    access_to = "all droplets"
  }
}

output "space_info" {
  value = {
    name     = digitalocean_spaces_bucket.object_store.name
    region   = digitalocean_spaces_bucket.object_store.region
    endpoint = digitalocean_spaces_bucket.object_store.bucket_domain_name
    urn      = digitalocean_spaces_bucket.object_store.urn
  }
}
