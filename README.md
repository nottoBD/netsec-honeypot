## Private Access 
```-A extends GPG agent to the tunnel```

```-i specifies privkey```
```
ssh -A -i ~/.ssh/ovh_vps ubuntu@vps-787fca07.vps.ovh.ca -p 61001
```

---

## Public Access
SSH Honeypot
```
ssh root@vps-787fca07.vps.ovh.ca -4
```
Telnet Honeypot
```
telnet vps-787fca07.vps.ovh.ca -4
```
HTTP Honeypot
```
http://51.79.248.60/admin
```

---
