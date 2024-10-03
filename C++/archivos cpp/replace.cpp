#include<iostream>
#include<vector>
template<typename T>
extern "C" int* replace(int array[], int size, int item1, int item2){
	for(int i=0; i<size; i++){
		if (array[i] == item1){
			array[i] = item2;
			break;
		}
	}
	return array;
}
