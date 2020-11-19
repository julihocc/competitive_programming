#include <iostream>
#include <cstdio>

int step_function(int x){
   int result = 0;
   if (x < 0){
       result = -1;
   } else if (x>0) {
       result = 1;
   }
    return result;
}

int main() {
    int n = 100;
    int value = step_function(n);
    printf("Número: %d \n Tipo: %d", n, value);
}
