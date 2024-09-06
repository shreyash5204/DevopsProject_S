// C++ program to add two number
// using addition operator
#include <iostream>
using namespace std;

// Function to return sum
// of two number
int addTwoNumber(int A, int B)
{
    // Return sum of A and B
    return A + B;
}

// Driver Code
int main()
{
    // Given two number
    int A = 5, B = 10;

    // Function call
    cout << "sum of two number = " << addTwoNumber(A, B);
    return 0;
}