#include <iostream>
#include <algorithm>
int main(){
    int size = 5;
    int arr[size] = {5, 4, 3, 2, 1};
    //printing original array
    for(int i = 0; i < size; i++){
        std::cout << arr[i] << " ";
    }
    std::sort(arr, arr + size); // function for sorting
    //print new array
    for(int i = 0; i < size; i++){
        std::cout << arr[i] << " ";
    }
}