FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    gcc \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY vuln.c .
RUN gcc -m32 -fno-stack-protector -z execstack -no-pie vuln.c -o vuln && \
    chmod +x vuln

EXPOSE 9999

CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./vuln"]
