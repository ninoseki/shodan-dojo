# GhostDNS

Create a query to find GhostDNS hosts.

## Background & hints

GhostDNS is a name of a large scale DNS hijacking campaign.

- [70+ different types of home routers(all together 100,000+) are being hijacked by GhostDNS](https://blog.netlab.360.com/70-different-types-of-home-routers-all-together-100000-are-being-hijacked-by-ghostdns-en/)
- [GhostDNS Exploit Kit Strikes Back](https://decoded.avast.io/simonamusilova/ghostdns-exploit-kit-strikes-back/)
- [GhostDNS Source Code Leaked](https://decoded.avast.io/simonamusilova/ghostdns-source-code-leaked/)

Interestingly, some of GhostDNS DNS changer hosts were enabled directory listing.

![](https://i.imgur.com/OUahYvz.jpg)
![](https://i.imgur.com/PBHM3jO.jpg)

You might find active GhostDNS hosts by leveraging known directory structure of GhostDNS.

- https://github.com/andreistefan87/GhostDNSBrut
- https://github.com/reaperb0t/GhostDNS
