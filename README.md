## Private Access 
```-A extends GPG agent to the tunnel```

```-i specifies privkey```
```
# -A to extend GPG agent
ssh -A -i "cowrie-netsec.pem" ubuntu@16.171.78.147 -p 61001
```

---

## Public Access
SSH Honeypot
```
ssh root@16.171.78.147 
```
Telnet Honeypot
```
telnet 16.171.78.147
```
HTTP Honeypot
```
http://16.171.78.147/admin
```

---
