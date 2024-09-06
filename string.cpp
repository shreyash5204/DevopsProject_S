#include <iostream>
#include <string>  // Include the string library

int main() {
    // Declare and initialize a string
    std::string greeting = "Hello, World!";

    // Output the string
    std::cout << greeting << std::endl;

    // Get user input for a string
    std::string name;
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);  // Get the entire line

    // Output the user-provided string with a greeting
    std::cout << "Hello, " << name << "!" << std::endl;

    return 0;
}
