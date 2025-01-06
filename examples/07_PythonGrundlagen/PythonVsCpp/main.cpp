// hello world c++ programm
// compile: g++ main.cpp -o main
// run: ./main

#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::cout << "Hello World!" << std::endl;
    std::string name;
    std::cout << "Bitte geben Sie Ihren Namen ein: ";
    std::cin >> name;
    std::cout << "Hallo " << name << std::endl;
    return 0;
}