#include <iostream>
int main(){
    int size = 5;
    int arr[size] = {1, 2, 3, 4, 5}; 
    int position = 3;
    int element = 6;
    //printing original array
    for(int i = 0; i < size; i++){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    //shifting elements
    for(int i = size; i >= position; i--){
        arr[i] = arr[i-1];
    }
    //inserting element
    arr[position - 1] = element;
    //printing modified array
    for(int i = 0; i < size + 1; i++){
        std::cout << arr[i] << " ";
    }
}