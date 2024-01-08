// Hier hatte ich keinen Ansatz gefunden, also habe ich versucht 
// mit den Aufzeichnungen aus ihrem Skript das Programm dafür "nachzubauen". 
// Allerdings funktioniert es nicht und ich verstehe nicht wieso? 

#include <iostream>
#include <math.h>
using namespace std;

int main(void)
{
	//alle Variablen
	int a[] = {1,2,3,1,4,5,1,1,2,2};
	int values = sizeof(a)/sizeof(int);

	double sum = 0;
	double streu = 0;


	//die Gesamtsumme
	for (int i=0; i<values; i++)
	{
		sum = sum + a[i];
	} 


	//Mittelwert
	double avg;
	avg = sum / (float)values;


	//Streuung
	for (int i=0; i<values; i++)
	{
		streu = streu + pow((a[i]-avg),2.);
	} 

	
	cout << "Die Summe beträgt: " << sum << "\n";
	cout << "Der Mittelwert beträgt: " << avg << "\n";
	cout << "Die Streuung beträgt: " << streu << "\n";

}