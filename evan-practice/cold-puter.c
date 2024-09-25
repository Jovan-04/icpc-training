#include <stdio.h>

int main() {
    int n;
    int totalNegative = 0;

    scanf("%d", &n);

    int nums[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    for (int i = 0; i < n; i++) {
        if (nums[i] < 0) {
            totalNegative++;
        }
    }

    printf("%d\n", totalNegative);

    return 0;
}