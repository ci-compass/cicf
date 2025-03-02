# terraform.tfvars

# A domain name for CICF cloud module.
domain_name = "cicf.cloud"

# Optional: override defaults if needed
region       = "nyc3"
droplet_size = "s-1vcpu-1gb"
space_name   = "cicf-object-store"
# data_dir     = "../data"
username     = "cicf"  # Common username set to "cicf"

# Define 18 users with their subdomains and SSH public keys
users = {
  "sajith" = {
    ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL5bFePtKg9/bTflbgT4Z+rXOS0X14PQgrs1ccqiBuFt sajith@hcoop.net"
  }
  # # "aidan" = {
  # #   ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key1@example.com"
  # # }
  # "anshuraj" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILI8DaKNkinpujbJ44R6TJyGegqnb1UZ1Mf4HeCKzHxv sedaianshuraj@gmail.com cicf"
  # }
  # # "baydan" = {
  # #   ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key3@example.com"
  # # }
  # "catherine" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBUZcBvlw3EEvUDs4+PaSwWBbazhX3oUOcnGVFX45UC+ celarson50@gmail.com cicf"
  # }
  # "dylan" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPDsFE4fD5u/GMNf/E1+arz/WkiFeS0Hv56yeCQ8Xr4Q dylanhermosillo@arizona.edu cicf"
  # }
  # "ejay" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBqfIs1P2MWGV0rotqR9s5FXPHxKB7xp5+iz/i+ENd2B ejay.aguirre04@gmail.com cicf"
  # }
  # # "elikem" = {
  # #   ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key7@example.com"
  # # }
  # "emma" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN7tGt5cLexNVvxdxVnEqiBUyneH5j8lId8kG5+kNH1p emma.stubby@gmail.com cicf"
  # }
  # "jasmine" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA4v+t5r2NdI1PxWN3e3chNzfArcyVr0eFYFcnvZqWLw fullofsunshine056@gmail.com cicf"
  # }
  # "joanna" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINiTm3WeizDX2X89V5izfySV7MgW5OPckoEJkTgTU7GB georgejoanna086@gmail.com"
  # }
  # "macy" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMUCPfjUMD143aZV7U5iARWRGrTSQxOJQ4ZMxl32A9z3 mjc81619@creighton.edu"
  # }
  # "naomi" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPZf8+iGfXohA8lz4CilAol/DpT1PomW7PyHPfIuYRzt kolodisner@arizona.edu cicf"
  # }
  # # "noe" = {
  # #   ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key13@example.com"
  # # }
  # "priscilla" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJknQAABgXNV/SaGFIP0v/E92vm9k/mm+Ct5n1B8E/Zw priscillazav27@gmail.com cicf"
  # }
  # # "rishi" = {
  # #   ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key15@example.com"
  # # }
  # # "spoorthi" = {
  # #   ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2E... key16@example.com"
  # # }
  # "tamara" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEQtQC+FvyHJ0W5Mf3kzobHl17e7H6KYQuF5yza8HEwe tamaracsegal@gmail.com cicf"
  # }
  # "xiuwen" = {
  #   ssh_public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPPxybtj1B8c1d6W4Od2TFTp0wAo+AcRm3aukX41klSK zhuxiuwen6@gmail.com cicf"
  # }
}

# Define SSH public keys for admin access as a map
admin_ssh_keys = {
  "don"    = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICYya82oSp8XKDFnQAxB+C6CeoAf7BXMV7OveIGXATOa dbrower@nd.edu cicf"
  "sajith" = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL5bFePtKg9/bTflbgT4Z+rXOS0X14PQgrs1ccqiBuFt sajith@hcoop.net"
}
