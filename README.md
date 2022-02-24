# pihole-stuff

### [The SNAFU Blocklist](https://github.com/RooneyMcNibNug/pihole-stuff/blob/master/SNAFU.txt):
An ever-evolving blocklist of ads, analytics, tracker, and other domains. Artisinally crafted - attempting to find and include "new" domains that have yet to be added in the default Ublock Origin list(s) or in other popular hosted blocklists.

Add the following link to your pi-hole adlists management config or other blocklist setup: https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt

If you run into a problem loading critical elements of a page due to a domain being included within this blocklist, please [submit an issue](https://github.com/RooneyMcNibNug/pihole-stuff/issues) and I will tend to it as soon as possible. 

### ["Marketing Technology Landscape" Mosaics](https://github.com/RooneyMcNibNug/pihole-stuff/tree/master/martech_landscape_imgs)
One of the more painful illustrations conveying just how massive the user-targeting industry has become. At least it helps with discovering new domains to enumerate for the blocklist.

### [Adlists I use](https://github.com/RooneyMcNibNug/pihole-stuff/blob/master/adlists_config.txt)
A compilation of lists I use within different environments, sorted by "type".

### [Python Scripts](https://github.com/RooneyMcNibNug/pihole-stuff/tree/master/python_scripts)
A few poorly cobbled together `.py` scripts to find possible URLs to add to the blocklist.

### [Unbound DNS server configuration](https://github.com/RooneyMcNibNug/pihole-stuff/blob/master/unbound.conf.d/pi-hole.conf)
A quick configuration for a recursive Unbound DNS server running on the same machine as pi-hole. As [noted](https://docs.pi-hole.net/guides/dns/unbound/#configure-unbound), Unbound creates a more comprehensively private alternative to relying on trusting third-party authorities, and pairs very well with pi-hole ad/tracker blocking.

### [Wirehole Setup](https://github.com/RooneyMcNibNug/pihole-stuff/tree/master/wirehole_setup)
A Terraform and Ansible-powered deployment of a [Wirehole](https://github.com/IAmStoxe/wirehole) VPN (equipped with Pi-Hole blocking) for DigitalOcean.

<a href="https://www.buymeacoffee.com/rooneymcnibnug" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-blue.png" alt="Buy Me A Coffee" height="38" width="132"></a>
