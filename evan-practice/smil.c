#include <stdio.h>
// https://open.kattis.com/problems/smil

int main() {
    char *name;
    size_t buf = 0;

    getline(&name, &buf, stdin);

    int currentSmileIndex = -1;
    int foundCharacters = 0;

    for (int i = 0; i < 2048; i++) {
        char c = name[i];
        if (c == '\0') break; // break at the end of input
        if (c == '-') continue;

        // start of a smile
        if (c == ':' || c == ';') {
            foundCharacters = 1;
            currentSmileIndex = i;
            continue;
        }

        // found a smile
        if (c == ')' && foundCharacters != 0) {
            printf("%d\n", currentSmileIndex);
            currentSmileIndex = -1;
            foundCharacters = 0;
            continue;
        }

        currentSmileIndex = -1;
        foundCharacters = 0;
    }

    return 0;
}