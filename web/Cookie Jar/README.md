# Cookie Jar

Author: [Claude](https://github.com/anthropics)

## Description

This challenge demonstrates session manipulation through cookie tampering.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Python Flask
- Base64 decoder

## Sources

```
You've logged in as a guest user. Can you find a way to become an admin?
```

## Exploit

When you visit the website, you're automatically logged in as a guest. Inspecting the cookies, you'll find a cookie named `session` with a base64 encoded value.

Decoding the base64 cookie reveals:
```
{"username": "guest", "role": "user"}
```

To get admin access, you need to modify this to:
```
{"username": "admin", "role": "admin"}
```

Then encode it back to base64 and replace the cookie value. Refresh the page and you'll see the flag displayed.

The flag is:

```
csictf{c00k13s_4r3_n0t_s3cur3}
```
