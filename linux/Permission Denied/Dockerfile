FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create CTF user
RUN useradd -m -s /bin/bash ctfuser && \
    echo "ctfuser:ctfpassword" | chpasswd

# Create flag
RUN echo "csictf{sud0_m4k3s_m3_p0w3rful}" > /home/ctf/flag.txt && \
    chmod 400 /home/ctf/flag.txt && \
    chown root:root /home/ctf/flag.txt

# Create SUID binary for privilege escalation
COPY backup.c /tmp/backup.c
RUN gcc /tmp/backup.c -o /usr/local/bin/backup && \
    chmod 4755 /usr/local/bin/backup && \
    rm /tmp/backup.c

# Configure SSH
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
