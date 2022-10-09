#include <iostream>
int main(){
    int size = 5;
    int arr[size] = {1, 2, 3, 4, 5};
    int deleteElement = 3;
    //printing original array
    for(int i = 0; i < size; i++){
        std::cout << arr[i] << " ";
    }
    //find element to delete
    for(int i = 0; i < size; i++){
        if(arr[i] == deleteElement){ // found, shift elements to delete
            for(int j = i; j < size - 1; j++){ 
                arr[j] = arr[j + 1];
            }
            break;
        }
    }
    //printing new array
    for(int i = 0; i < size - 1; i++){
        std::cout << arr[i] << " ";
    }
}