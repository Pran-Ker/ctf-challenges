# Hidden Message

Author: [Claude](https://github.com/anthropics)

## Description

This challenge involves extracting hidden data from image metadata.

## Requirements

- exiftool or any EXIF viewer
- strings command (optional)

## Sources

```
We found this image on the suspect's computer. There might be something hidden in it.
```

- [challenge.jpg](./challenge.jpg)

## Exploit

The flag is hidden in the image's EXIF metadata. You can extract it using exiftool:

```bash
exiftool challenge.jpg
```

Looking at the output, you'll find in the "Comment" or "Description" field:

```
Flag: csictf{m3t4d4t4_h1d3s_s3cr3ts}
```

Alternatively, you can use the strings command:

```bash
strings challenge.jpg | grep csictf
```

The flag is:

```
csictf{m3t4d4t4_h1d3s_s3cr3ts}
```
