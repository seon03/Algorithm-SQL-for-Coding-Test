#include <stdio.h>

int main(void) {
	int i, j, temp;
	int array[10] ={2, 3, 4, 5, 6, 7, 8, 9, 10, 1};
	for (i = 0; i < 9; i++) {
		j = i;
		while(array[j] > array[j + 1]) {
			temp = array[j];
			array[j] = array[j + 1];
			array[j + 1] = temp;
			j--;
		}
	}
	for(i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}
	return 0;
}
