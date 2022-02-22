# Automated Wirehole Droplet Install (Digital Ocean)

If you have a Digital Ocean account, you can use the items within this directory to whip up a Wirehole droplet quickly and comprehensively.

To get this whole thing rolled out, the following tools are required:

- [Terraform](https://www.terraform.io/downloads)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

## Why Wirehole?

I've previously [written](https://rooneymcnibnug.github.io/privacy/2019/08/30/CentOS7-Wireguard-PiHole.html) about creating a VPN in "the cloud" including ad/tracker-blocking by using a Pi-hole install. 

I found out about [Wirehole](https://github.com/IAmStoxe/wirehole) over a year ago, which does a much better job of coming pre-configured with a more thorough privacy-preserving setup:

- Pre-configured Pi-hole and Wireguard connection that works alongside all other components on a docker conatiner
- Unbound DNS set up for recursive queiries (more on why this is a good idea [here](https://docs.pi-hole.net/guides/dns/unbound/))

## Procedure

You will need a Digital Ocean account before running anything here. From your login, you will need to have the following handy:

- The fingerprint of a [currently existing SSH public key in your Digital Ocean login](https://cloud.digitalocean.com/account/security)
- Your Digital Ocean [API Key](https://cloud.digitalocean.com/api_access)

#### 1. Deployment of the Droplet via Terraform

If you are unfamiliar with Terrafrom, please do consult [the following article](https://www.terraform.io/intro/core-workflow) on standard workflow practice, but basically it will go something like this here:

`Init -> Plan -> Apply`

So, in the case of this repo, its:

```console
foo@bar:~$ terraform init
foo@bar:~$ terraform plan -out main.tfplan
foo@bar:~$ terraform apply -input main.tfplan
```

After you have completed this, make sure that your Droplet exists within Digital Ocean.

#### 2. Configurations via Ansible

We want to make sure we can reach our Droplet with Ansible, then run the main ansible configurations and others within the `ansible` folder in this repo. This will go as follows from the /ansible folder):

```console
foo@bar:~$ ansible do -m ping
foo@bar:~$ anible-playbook drop_main.yml
```

Please check the destination on the Dropley (Check the comment in `/ansible/taks/drop_wirehole.yml` for help!) to make sure your Wireguard peer connections have been properly generated/configured.

#### 3. Roll out!

Now copy the information from your `peer1..7` configs to any of the devices you want to connect to with Wireguard and you will have a nice VPN equipped with Wireguard, Pi-Hole, and Unbound!

You can obviously tweak the Wireguard/Pi-Hole settings per your liking from [here](https://github.com/RooneyMcNibNug/pihole-stuff/blob/master/adlists_config.txt). I highly recommend adding some blocklists, as a first step. I have a list of some of the ones I prefer to use, and I will be thrilled if you'd like to use my artisinally-crafted blocklist [here](https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt).

Safe travels 😶‍🌫️
