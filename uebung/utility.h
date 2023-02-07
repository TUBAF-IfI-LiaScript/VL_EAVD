//  For testing purposes only!
namespace Utility
{
    //  Für Aufgabenblatt 12, Aufgabe 3
    //  Funktion zum testen ohne wissenschaftliche Bedeutung / Korrektheit
    double simulation(int frost_dauer, double frost_tiefe, double pH_wert)
    {
        return (14 - pH_wert) / (frost_dauer * frost_tiefe * 0.01);
    }
}
