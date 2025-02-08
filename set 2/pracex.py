#include <stdio.h>
#include <time.h>
void main (void)
{ 
    time_t curent_time = time (NULL);
    char date_string[20];
    strftime(date_string,20,"%Y-%m-%d",localtime(&curent_time));
    printf("the curent dateis:%s\n",date_string);
}
