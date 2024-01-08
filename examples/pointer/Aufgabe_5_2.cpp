// Mein Programm hat erst funktioniert als mir die Übungsleiterin gesagt hat, 
// dass ich ein "&" in Zeile 7 beim "q" und beim "a" noch hinzufügen muss.
// Hier wieder die Fragen zu den Pointern: Was bewirkt das "&" und wieso 
// muss ich es dort einfügen das mit das Programm funktioniert? 

#include <iostream>
#include <math.h>
using namespace std;

             // input            // output
void funktion(double x, double y, int & q, double & a)
{
	if(x==0 && y==0){q=0;};
	if(x>=0 && y>=0){q=1;};
	if(x<=0 && y>=0){q=2;};
	if(x<=0 && y<=0){q=3;};
	if(x>=0 && y<=0){q=4;};

	a = atan(y/x) * 180 / M_PI;
}

// Variablen und Berechnung

int main()
{
	double a, x, y;
	int q;

	cin >> x >> y;

	funktion(x, y, q, a);

	cout << "Quadrant: " << q <<"\n"<< "Winkel: " << a <<"\n";
}