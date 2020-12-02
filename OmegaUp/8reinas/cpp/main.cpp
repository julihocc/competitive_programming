#include <iostream>

void search(int y){
    if (y==n) {
        count++;
        return;
    }
    for (int x=0; x<n; x++) {
        if (col[x]||diag1[x+y]||diag2[x-y+n-1]) continue;
        col[x] = diag1[x+y] = diag2[x-y+n-1] = 1;
        search(y=1);
        col[x] = diag1[x+y] = diag2[x-y+n-1] = 0;
    }
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
