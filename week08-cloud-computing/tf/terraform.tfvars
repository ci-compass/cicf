# terraform.tfvars

# Add your domain name
domain_name = "example.com"

# Optional: override defaults if needed
region      = "nyc3"
droplet_size = "s-1vcpu-1gb"
space_name  = "my-object-store"

# Define 18 users with their subdomains and SSH public keys
users = {
  "aidan" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key1@example.com"
  }
  "anshuraj" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key2@example.com"
  }
  "baydan" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key3@example.com"
  }
  "catherine" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key4@example.com"
  }
  "dylan" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key5@example.com"
  }
  "ejay" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key6@example.com"
  }
  "elikem" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key7@example.com"
  }
  "emma" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key8@example.com"
  }
  "jasmine" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key9@example.com"
  }
  "joanna" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key10@example.com"
  }
  "macy" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key11@example.com"
  }
  "naomi" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key12@example.com"
  }
  "noe" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key13@example.com"
  }
  "priscilla" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key14@example.com"
  }
  "rishi" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key15@example.com"
  }
  "spoorthi" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key16@example.com"
  }
  "tamara" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key17@example.com"
  }
  "xiuwen" = {
    ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key18@example.com"
  }
}

# Define SSH public keys for admin access as a map
admin_ssh_keys = {
  "alice"  = "ssh-rsa AAAAB3NzaC1yc2E... alice@example.com"
  "bob"    = "ssh-rsa AAAAB3NzaC1yc2E... bob@example.com"
}
