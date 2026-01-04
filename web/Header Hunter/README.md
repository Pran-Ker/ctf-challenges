# Header Hunter

Author: [Claude](https://github.com/anthropics)

## Description

This challenge teaches HTTP header manipulation and custom header usage.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Python Flask
- curl or browser dev tools

## Sources

```
Our API only accepts requests from our internal admin application. Can you figure out how to access it?
```

## Exploit

The website displays a message saying access is denied. You need to inspect how the application validates requests.

Using curl or browser developer tools, you can see that the application checks for specific HTTP headers:

1. `X-Admin-Token: secret_admin_token_2024`
2. `User-Agent: AdminApp/1.0`

Send a request with both headers:

```bash
curl -H "X-Admin-Token: secret_admin_token_2024" -H "User-Agent: AdminApp/1.0" http://localhost:5000/
```

The flag is:

```
csictf{h34d3rs_c4n_b3_sp00f3d}
```
