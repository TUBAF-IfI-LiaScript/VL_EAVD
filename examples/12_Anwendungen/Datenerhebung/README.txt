ThingSpeakTUBAF

Diese Headerdatei ermöglicht es mit dem MXChip Daten auf ThingSpeak hochzuladen.

------------------------------------------------------------------------------------------

Variablen:

hasWifi:    Stellt dar, ob der MXChip mit einem Wi-Fi verbunden wurde. Dies geschieht 
            durch die Funktion InitWifi.

SSL_CA_PEM: Zertifikat. Leer, da nur auf eine http-Addresse zugegriffen wird.

------------------------------------------------------------------------------------------

Funktionen:

InitWifi:    Das Wi-Fi des Chips wird initialisiert. Wenn eine Verbindung zum Wi-Fi 
             gelingt wird dies und die IP-Adresse über die serielle Ausgabe ausgegeben.

updateThingSpeak: Erhält den Key zum ThingSpeak Channel, die Daten die hochgeladen 
                  werden sollen und die Länge des Datenarrays. Die hochzuladenen Daten
                  sind in einem float-Array in der Reihenfolge der Felder (Fields) des 
                  Channels zu übergeben. Wenn die Daten erfolgreich hochgeladen wurden 
                  wird dies und die Nummer der Eintragung ausgegeben.

------------------------------------------------------------------------------------------
