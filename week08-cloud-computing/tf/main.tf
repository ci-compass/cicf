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
  # spaces_access_id  = var.do_spaces_access_id
  # spaces_secret_key = var.do_spaces_secret_key
}

# Variables
variable "do_token" {
  description = "Digital Ocean API token"
  type        = string
  sensitive   = true
}

# variable "do_spaces_access_id" {
#   description = "Digital Ocean Spaces access ID"
#   type        = string
#   sensitive   = true
# }

# variable "do_spaces_secret_key" {
#   description = "Digital Ocean Spaces secret key"
#   type        = string
#   sensitive   = true
# }

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

variable "username" {
  description = "Common username for subdomain-specific users"
  type        = string
  default     = "cicf"
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

# variable "data_dir" {
#   description = "Path to local data directory to copy to users' home dirs"
#   type        = string
#   default     = "../data"
# }

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
  ipv6     = true  # Enable IPv6

  # Add tags to each droplet
  tags = [
    "environment:cicf",
    "os:debian",
  ]

  user_data = <<-EOF
    #!/bin/bash

    # Set hostname and domain name
    hostnamectl set-hostname ${each.key}
    echo "${each.key}.${var.domain_name}" > /etc/hostname
    echo "127.0.0.1 localhost" > /etc/hosts
    echo "127.0.1.1 ${each.key}.${var.domain_name} ${each.key}" >> /etc/hosts

    # Create '${var.username}' user.
    useradd -m -s /bin/bash ${var.username}
    mkdir -p /home/${var.username}/.ssh
    echo "${each.value.ssh_public_key}" > /home/${var.username}/.ssh/authorized_keys
    chown -R ${var.username}:${var.username} /home/${var.username}/.ssh
    chmod 700 /home/${var.username}/.ssh
    chmod 600 /home/${var.username}/.ssh/authorized_keys
    usermod -aG sudo ${var.username}

    # Create an admin user.
    useradd -m -s /bin/bash admin
    mkdir -p /home/admin/.ssh
    cat << 'ADMIN_KEYS' > /home/admin/.ssh/authorized_keys
    ${join("\n", values(var.admin_ssh_keys))}
    ADMIN_KEYS
    chown -R admin:admin /home/admin/.ssh
    chmod 700 /home/admin/.ssh
    chmod 600 /home/admin/.ssh/authorized_keys
    usermod -aG sudo admin

    # Configure sudoers for passwordless sudo
    echo "${var.username} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${var.username}
    echo "admin ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/admin
    chmod 440 /etc/sudoers.d/${var.username}
    chmod 440 /etc/sudoers.d/admin

    # Disable password login in SSH configuration
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
    sed -i 's/#ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config

    # Ensure these settings are explicitly set
    echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
    echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
    echo "ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config

    # # Move uploaded data directory to user home directories
    # if [ -d "/tmp/data" ]; then
    #   cp -r /tmp/data /home/${var.username}/data
    #   cp -r /tmp/data /home/admin/data
    #   chown -R ${var.username}:${var.username} /home/${var.username}/data
    #   chown -R admin:admin /home/admin/data
    #   rm -rf /tmp/data
    # fi

    # Restart SSH service to apply changes
    systemctl restart sshd
    EOF

  # # Provisioner to upload the data directory
  # provisioner "file" {
  #   source      = var.data_dir
  #   destination = "/tmp/data"

  #   connection {
  #     type        = "ssh"
  #     user        = var.username
  #     private_key = file("~/.ssh/id_ed25519")
  #     host        = self.ipv4_address  # Using IPv4 for initial connection
  #   }
  # }
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

# Create AAAA records for IPv6
resource "digitalocean_record" "subdomain_aaaa" {
  for_each = var.users
  domain   = digitalocean_domain.main_domain.name
  type     = "AAAA"
  name     = each.key
  value    = digitalocean_droplet.debian_droplet[each.key].ipv6_address
  ttl      = 300
}

# # Create a Digital Ocean Space (Object Storage)
# resource "digitalocean_spaces_bucket" "object_store" {
#   name   = var.space_name
#   region = var.region
#   acl    = "public-read"

#   versioning {
#     enabled = true
#   }
# }

# Outputs
output "droplet_info" {
  value = {
    for subdomain, user in var.users :
    subdomain => {
      ipv4_address = digitalocean_droplet.debian_droplet[subdomain].ipv4_address
      ipv6_address = digitalocean_droplet.debian_droplet[subdomain].ipv6_address      
      subdomain    = "${subdomain}.${var.domain_name}"
      ssh_key      = substr(user.ssh_public_key, 0, 20)
      username     = var.username
      tags         = digitalocean_droplet.debian_droplet[subdomain].tags
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

# output "space_info" {
#   value = {
#     name     = digitalocean_spaces_bucket.object_store.name
#     region   = digitalocean_spaces_bucket.object_store.region
#     endpoint = digitalocean_spaces_bucket.object_store.bucket_domain_name
#     urn      = digitalocean_spaces_bucket.object_store.urn
#   }
# }
