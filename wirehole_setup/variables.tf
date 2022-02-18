# Your Digital Ocean user token goes here
variable "drop_token" {}

# (One of) your current SSH key fingerprints from the Digital Ocean Console
# Find it at Settings > Security > SSH Keys
variable "drop_ssh_key" {}

# Path to your local SSH key(s)
variable "ssh_private_key_path" {
    default = "~/.ssh/id_rsa.pub"
}

variable "region" {
    default = "nyc2"
}

variable "drop_name" {
    default = "wirehole"
}

# Latest Ubuntu distrib image available
variable "drop_img" {
    default = "ubuntu-20-04-x64"
}

# 1VCP/1GB is more than enough for this, but feel free to change
variable "drop_size" {
    default = "s-1vcpu-1gb"
}