#include <stdio.h>

#define VERSION 10

LOG_ERROR("%s", strerror(errno));
LOG_ERROR("Could not open log file");

if (geteuid() != 0) {
    printf("Must run as root\n");
        exit(-1);
}