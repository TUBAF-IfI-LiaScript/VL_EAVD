<!--
import:   import: https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
-->

# C++ Operatoren

Man kann sich Operatoren auch als Methoden vorstellen - ich hatte es in der Vorlesung angedeutet, aber nicht umgesetzt. Für das bessere Verständnis wurde das Beispiel aus der Vorlesung erweitert:   

Für weitere Fragen stehen wir gern zur Verfügung.

```c++ Operatoren.cpp
#include <iostream>

class Rectangle {
  private:
    float width, height;
  public:
    Rectangle(float w, float h): width{w}, height{h} {}
    float area() {return width*height;}
    Rectangle operator+=(Rectangle offset) {
       float ratio = (offset.area() + this->area()) / this->area();
       this->width = ratio *  this->width;
       return *this;    // <- Return für das angepasste "eigene" Objekt
    }
};

bool operator>(Rectangle a, Rectangle b){
    if (a.area() > b.area()) return true;
    else return false;
}

int main () {
  Rectangle rect_a(3,4);
  Rectangle rect_b(5,7);
  bool result = false;
  std::cout << "Fläche a : " << rect_a.area() << "\n";
  std::cout << "Fläche b : " << rect_b.area() << "\n";
  std::cout << "-------------------------" << std::endl << std::endl;

  // Aufruf des Operators, der "außerhalb" einer Klasse steht (Zeile 16)
  // mit zwei Paramtern (Rectangle a, Rectangle b)
  // Variante 1: über das Operatorsymbol
  result = (rect_a > rect_b);
  std::cout << "Funktionsoperator 1 (Vergleich): " << result << "\n";
  // Variante 2: über einen "funktionsähnlichen Aufruf" 
  result = operator>(rect_a, rect_b);
  std::cout << "Funktionsoperator 2 (Vergleich): " << result << "\n";

  // Aufruf des Operators, der innerhalb der Klasse definiert is (Zeile 9)
  // mit EINEM Paramtern (Rectangle b) über dem Objekt rect_a
  // Das Ergebnis wird auf rect_a geschrieben - entsprechend bewirken die 
  // Variante 1 und 2 jeweiles eine Vergrößerung des Areals
  // Variante 1: über das Operatorsymbol
  rect_a += rect_b;
  std::cout << "Methodenoperator  1 (Add)      : " << rect_a.area() << std::endl;
  // Variante 2: über einen "funktionsähnlichen Aufruf"
  rect_a.operator+=(rect_b);
  std::cout << "Methodenoperator  2 (Add)      : " << rect_a.area() << std::endl;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ main.cpp -o a.out`, `./a.out`)
