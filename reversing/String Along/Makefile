CC=gcc
CFLAGS=-O2

all: challenge

challenge: challenge.c
	$(CC) $(CFLAGS) challenge.c -o challenge
	strip challenge

clean:
	rm -f challenge
