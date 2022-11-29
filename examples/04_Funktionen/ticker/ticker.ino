#include <OledDisplay.h>

void setup(){
    Screen.init();
    String text = " Das ist ein sehr langer Text, der nicht ins Display passt";
    String output = "";
    int signs_per_line = 16;
    for (int i = 0; i < text.length(); i++){
		 if (i <= text.length()-signs_per_line)
				output = text.substring(i, i+signs_per_line);
		 else
        output = text.substring(i, text.length()) +
                 text.substring(0, signs_per_line-(text.length()-i));
        char char_array[signs_per_line];
        output.toCharArray(char_array, signs_per_line);
        Screen.print(char_array, false);
        delay(300);
        Screen.clean();
    }
}

void loop(){}