# Permission Denied

Author: [Claude](https://github.com/anthropics)

## Description

A Linux challenge focusing on file permissions and privilege escalation.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Basic Linux commands
- Understanding of file permissions

## Sources

```
You've logged into a system, but the flag file is locked. Can you find a way to read it?

SSH into the server and find the flag in /home/ctf/flag.txt
```

## Exploit

When you log in to the system, you'll find that /home/ctf/flag.txt has restricted permissions:

```bash
ls -la /home/ctf/flag.txt
-r-------- 1 root root 35 Jan 1 12:00 /home/ctf/flag.txt
```

You can't read it directly. However, if you explore the system, you'll find:

1. Check for SUID binaries:
```bash
find / -perm -4000 -type f 2>/dev/null
```

2. You'll find a suspicious binary at /usr/local/bin/backup that has SUID permissions.

3. Running `strings` on it reveals it executes `/bin/cat /home/ctf/flag.txt`

4. Since it runs with root privileges (SUID), you can read the flag:

```bash
/usr/local/bin/backup
```

Alternatively, check for:
- Files in /tmp or /var/tmp
- Backup files (.bak, .old)
- Hidden files that might contain the flag

The flag is:

```
csictf{sud0_m4k3s_m3_p0w3rful}
```
