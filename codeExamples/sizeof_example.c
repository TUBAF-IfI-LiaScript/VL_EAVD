#include <stdio.h>
#include <limits.h>   /* INT_MIN und INT_MAX */

int main() {
   printf("int size : %d Byte\n", (int) sizeof( int ) );
   printf("Wertebereich von %d bis %d\n", INT_MIN, INT_MAX);
   printf("char size : %d Byte\n", (int) sizeof( char ) );
   printf("Wertebereich von %d bis %d\n", CHAR_MIN, CHAR_MAX);
   return 0;
}
