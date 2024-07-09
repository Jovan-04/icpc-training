#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FRECKLES 1000

typedef struct freckle {
    double x, y;
} Freckle;

int freckleCount;

int connected[MAX_FRECKLES];

Freckle readCoordinates(void) {
    Freckle f;
    scanf("%lf %lf\n", &f.x, &f.y);
    return f;
}

Freckle * readCase(void) {
    scanf("\n%d\n", &freckleCount);
    
    Freckle *array = malloc(freckleCount * sizeof *array);
    if (!array) { exit(EXIT_FAILURE); }
    for (int i = 0; i < freckleCount; i++) {
        array[i] = readCoordinates();
    }
    
    return array;
}

int main(void) {
    int n;
    scanf("%d\n", &n);
    
    for (int i = 0; i < n; i++) {
        Freckle *freckles = readCase();
        memset(connected, 0, MAX_FRECKLES * sizeof *connected);
        
        double ink = 0;
        
        for (int j = 0; j < freckleCount; j++) {
            if (connected[j]) {
                continue;
            }
            
            Freckle a = freckles[j];
            double min = 1e6;
            int connect;

            for (int k = 0; k < freckleCount; k++) {
                if (k == j) {
                    continue;
                }
                
                Freckle b = freckles[k];

                double h = hypot(a.x - b.x, a.y - b.y);
                if (h < min) {
                    min = h;
                    connect = k;
                }
            }
            
            ink += min;
            connected[j]++;
            connected[connect]++;
        }
        
        printf("%.2f\n\n", ink);
	free(freckles);
    }

    return 0;
}
