# Barcode Bonanza

Author: [Claude](https://github.com/anthropics)

## Description

A challenge involving QR code and barcode scanning.

## Requirements

- QR code scanner (online or mobile app)
- Barcode decoder

## Sources

```
We intercepted these codes from the enemy. Scan them in the correct order to reveal the flag!
```

- [code1.png](./code1.png) - QR Code
- [code2.png](./code2.png) - QR Code
- [code3.png](./code3.png) - QR Code

## Exploit

You need to scan three QR codes in sequence. Each QR code contains a part of the flag.

**QR Code 1** contains: `csictf{qr_c`
**QR Code 2** contains: `0d3s_4r3`
**QR Code 3** contains: `_fun_2_sc4n}`

Combine them in order to get the complete flag.

Alternatively, there might be a hint in the file names or metadata that indicates the correct order.

The flag is:

```
csictf{qr_c0d3s_4r3_fun_2_sc4n}
```
