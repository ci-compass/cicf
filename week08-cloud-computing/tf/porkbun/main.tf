terraform {
  required_version = ">= 1.0"
  required_providers {
    porkbun = {
      source  = "jianyuan/porkbun"
      version = "~> 0.2"
    }
  }
}

provider "porkbun" {
  api_key        = var.porkbun_api_key
  secret_api_key = var.porkbun_secret_key
}

variable "porkbun_api_key" {
  description = "Porkbun API key"
  type        = string
  sensitive   = true
}

variable "porkbun_secret_key" {
  description = "Porkbun secret API key"
  type        = string
  sensitive   = true
}

variable "domain" {
  description = "Your Porkbun domain"
  type        = string
  default     = "cicf.cloud"
}

resource "porkbun_nameservers" "do_nameservers" {
  domain = var.domain
  nameservers = [
    "ns1.digitalocean.com",
    "ns2.digitalocean.com",
    "ns3.digitalocean.com"
  ]
}
