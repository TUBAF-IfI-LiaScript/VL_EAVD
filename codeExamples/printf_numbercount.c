#include <stdio.h>

int main(){
  printf("rechtsbuendig      : %5d, %5d, %5d\n",34, 343, 3343);
  printf("rechtsbuendig mit 0: %05d, %05d, %05d\n",34, 343, 3343);
  printf("linksbuendig       : %-5d, %-5d, %-5d\n",34, 343, 3343);
  printf("Zu klein gedacht   : %5d\n", 234534535);
  printf("Ohnehin besser     : %*d\n", 12, 234534535);
  return 0;
}
