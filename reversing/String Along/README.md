# String Along

Author: [Claude](https://github.com/anthropics)

## Description

A simple reverse engineering challenge involving string manipulation.

## Requirements

- strings command
- Basic Python knowledge (optional)
- objdump or ghidra (optional)

## Sources

```
We found this binary. Can you find the flag?
```

- [challenge](./challenge)

## Exploit

This is a simple reversing challenge. The flag is embedded in the binary as a string but it's encoded.

First, run the strings command:

```bash
strings challenge
```

You'll find an encoded string: `pfvpgs{e3i3ef1at_1f_3jfl}`

This looks like it might be ROT13 or another substitution cipher. After analyzing the binary or trying common ciphers, you'll find it's ROT13:

```bash
echo "pfvpgs{e3i3ef1at_1f_3jfl}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

This gives you: `csictf{r3v3rs1ng_1s_3asy}`

Alternatively, if you run the binary with the correct password "CTF2024", it will decode and display the flag:

```bash
./challenge CTF2024
```

The flag is:

```
csictf{r3v3rs1ng_1s_3asy}
```
