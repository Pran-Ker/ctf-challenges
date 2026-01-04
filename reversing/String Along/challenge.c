#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void rot13(char *str) {
    for (int i = 0; str[i]; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = ((str[i] - 'a' + 13) % 26) + 'a';
        } else if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = ((str[i] - 'A' + 13) % 26) + 'A';
        }
    }
}

int main(int argc, char *argv[]) {
    // Encoded flag (ROT13 of csictf{r3v3rs1ng_1s_3asy})
    char encoded[] = "pfvpgs{e3i3ef1at_1f_3jfl}";

    if (argc < 2) {
        printf("Usage: %s <password>\n", argv[0]);
        return 1;
    }

    if (strcmp(argv[1], "CTF2024") == 0) {
        rot13(encoded);
        printf("Correct password! Flag: %s\n", encoded);
    } else {
        printf("Wrong password!\n");
    }

    return 0;
}
