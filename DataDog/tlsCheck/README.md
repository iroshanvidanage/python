## TLS/SSL certificate check

- This script was made to check the expiration date of pem/cert files hosted on servers
- Issue began when I try to get the expiration date of a website using the web url.
- As we know some hosts their domains on CloudFlare or other WAF service and map their web hosting servers (EC2,VMs) for static contents.
- I used nginx as the web hosting service and there were multiple instances, hence checking and maintaining the certificate was hard.
- Datadog has an inbuilt config for certificates, but wasn't able to configure it to get the expiration date of the cert in the instance.
- Hence developed this script as an integration to the datadog agent.