#include <stdio.h>

int main()
{
    FILE *f = fopen("out.txt", "wt");
    fprintf(f, "CR: \r");
    fprintf(f, "LF: \n");
    fprintf(f, "CR+LF: \r\n");
    fclose(f);
    return 0;
}
