#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAG "csictf{buff3r_0v3rfl0ws_4r3_d4ng3r0us}"

void secret() {
    printf("Congratulations! You found the secret function!\n");
    printf("Flag: %s\n", FLAG);
    exit(0);
}

void vulnerable() {
    char buffer[64];
    printf("Enter your name: ");
    gets(buffer);  // Dangerous! Buffer overflow vulnerability
    printf("Hello, %s!\n", buffer);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    printf("Welcome to Stack Overflow 101!\n");
    printf("Can you find a way to call the secret function?\n\n");

    vulnerable();

    printf("Goodbye!\n");
    return 0;
}
