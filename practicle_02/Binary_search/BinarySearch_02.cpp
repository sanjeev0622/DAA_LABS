#include <iostream>
using namespace std;

// Function to perform binary search
// Returns the index of target if found, otherwise returns -1
int binarySearch(int array[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        // Safe way to find the middle index without overflow
        int mid = low + (high - low) / 2;

        // Check if target is present at mid
        if (array[mid] == target) {
            return mid;
        }
        
        // If target is greater, ignore the left half
        if (target > array[mid]) {
            low = mid + 1;
        } 
        // If target is smaller, ignore the right half
        else {
            high = mid - 1;
        }
    }

    // Target was not present in the array
    return -1;
}

int main() {
    // Binary search strictly requires a SORTED array
    int array[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int size = sizeof(array) / sizeof(array[0]);
    int target = 23;

    int result = binarySearch(array, size, target);

    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found in the array." << endl;
    }

    return 0;
}
