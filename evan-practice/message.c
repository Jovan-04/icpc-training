#include <stdio.h>
// https://open.kattis.com/problems/meddelande
int main() {
    int n;
    int m;

    scanf("%d", &n);
    scanf("%d", &m);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m+1; j++) { // why do i need to put a +1 here??
            char c;
            scanf("%c", &c);
            if (c != '.' && c != '\n') putchar(c);
        }
    }

    printf("\n");

    return 0;
}
