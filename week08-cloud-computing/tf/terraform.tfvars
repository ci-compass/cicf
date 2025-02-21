# terraform.tfvars

# Add your domain name
domain_name = "example.com"

# Optional: override defaults if needed
username    = "debianuser"
region      = "nyc3"
droplet_size = "s-1vcpu-1gb"

# Define 18 users with their subdomains and SSH public keys
users = {
  "web1" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key1@example.com"
  }
  "web2" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key2@example.com"
  }
  "web3" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key3@example.com"
  }
  "api1" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key4@example.com"
  }
  "api2" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key5@example.com"
  }
  "api3" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key6@example.com"
  }
  "db1" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key7@example.com"
  }
  "db2" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key8@example.com"
  }
  "db3" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key9@example.com"
  }
  "cache1" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key10@example.com"
  }
  "cache2" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key11@example.com"
  }
  "cache3" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key12@example.com"
  }
  "worker1" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key13@example.com"
  }
  "worker2" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key14@example.com"
  }
  "worker3" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key15@example.com"
  }
  "monitor1" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key16@example.com"
  }
  "monitor2" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key17@example.com"
  }
  "monitor3" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key18@example.com"
  }
}
