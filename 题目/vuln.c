#include <stdio.h>
#include <string.h>
#include<stdlib.h>

int getshell()
{
        return system("/bin/sh");
}

int main(int argc, char* argv[]) {
        char buf[8];
        strcpy(buf,argv[1]);
        printf("Input:%s\n",buf);
        return 0;
}