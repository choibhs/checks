#include <stdio.h>
#include <cs50.h>

void PrintArray(int array[], int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%i", array[i]);
        if (i < length - 1)
        {
            printf(", ");
        }
    }
    printf("\n");
}

// Assume iteration_num starts with 0 as the first one.
// Note that this function returns the index of the smallest element,
// not the value of the element itself.
int GetIndexOfSmallestElement(int array[], int length, int iteration_num)
{
    int min_index = iteration_num;
    for (int i = iteration_num+1; i < length; i++)
    {
      if (array[i] < array[min_index])
      {
        min_index = i;
      }
    }
    return min_index;
}

void SelectionSort(int array[], int length)
{
    int num_swaps = 0;
    int min_index = -1;
    int temp = -1;
    for (int i=0; i < length; i++)
    {
        // Fill in the rest of the code for this for loop here.
        // You should be able to accomplish this in 8 lines,
        // two of which are the lines for the { }.
        min_index = GetIndexOfSmallestElement(array, length, i);
        if (min_index != i)
        {
            temp = array[min_index];
            array[min_index] = array[i];
            array[i] = temp;
            num_swaps++;
        }
    }
    printf("Number of swaps: %i\n", num_swaps);
}

int main(void)
{
   	int array[5] = { 19, 77, -11, -8, 24 };
	printf("Original array: ");
	PrintArray(array, 5);
	SelectionSort(array, 5);
    printf("Sorted array: ");
    PrintArray(array, 5);
}