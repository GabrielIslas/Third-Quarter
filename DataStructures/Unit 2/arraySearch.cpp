#include <iostream>
int main(){
    int size = 5;
    int arr[size] = {1, 2, 3, 4, 5};
    int find = 3;
    int index = -1;
    bool found = false;
    for(int i = 0; i < size; i++){
        if (arr[i] == find){ // element found
            std::cout << "Found";
            found = true;
            index = i;
            break;
        }
    }
    if(!found){ // element not found
        std::cout << "Not Found";
    }
}