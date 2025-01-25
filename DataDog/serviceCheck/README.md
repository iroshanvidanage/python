## Service Check

- A datadog integrated script for checking service availability.
- Example service is 'nginx'.
- Typical outputs are as follows.

```
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2025-01-26 02:34:01 IST; 30min ago
     Docs: man:nginx(8)
 Main PID: 1234 (nginx)
    Tasks: 2 (limit: 4915)
   CGroup: /system.slice/nginx.service
           ├─1234 nginx: master process /usr/sbin/nginx -g daemon on;
           └─1235 nginx: worker process


● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Sun 2025-01-26 01:54:00 IST; 1h 11min ago
     Docs: man:nginx(8)
  Process: 1234 ExecStart=/usr/sbin/nginx -g daemon on; (code=exited, status=0/SUCCESS)
  Process: 1235 ExecReload=/usr/sbin/nginx -g daemon on; -s reload (code=exited, status=0/SUCCESS)
  Process: 1236 ExecStop=/sbin/start-stop-daemon -o -K -q -p /run/nginx.pid (code=exited, status=0/SUCCESS)
 Main PID: 1234 (code=exited, status=0/SUCCESS)

```

- Notice that the Active line indicates that the service is inactive (dead). There are other possible states, like failed, and in such cases, additional diagnostic information will be provided further down in the output, which can include logs indicating why the service stopped or failed.