resource "digitalocean_droplet" "wirehole" {
    image = var.drop_img
    name = var.drop_name
    region = var.region
    size = var.drop_size
    private_networking = true
    #monitoring = true
    ssh_keys = [
      var.drop_ssh_key
    ]
}