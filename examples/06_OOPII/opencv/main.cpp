// Beispielprogramm zur Bildsegmentierung mit OpenCV
// Kompilieren mit:
// g++ main.cpp -o demo `pkg-config --cflags --libs opencv4`

#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // Bild laden (graustufen ist für Canny sinnvoll)
    cv::Mat img = cv::imread("./images/Q001792_002-5x-xpol-preview.png", cv::IMREAD_GRAYSCALE);

    if (img.empty()) {
        std::cerr << "Bild konnte nicht geladen werden!" << std::endl;
        return -1;
    }

    if (img.empty()) return -1;

    cv::Mat segmented;

    // Einfache Schwellenwertsegmentierung
    // Pixelwerte über 120 werden auf 255 gesetzt, andere auf 0
    //             Input, Output, Schwellenwert, Maximalwert, Typ   
    cv::threshold(img, segmented, 120, 255, cv::THRESH_BINARY);

    cv::imshow("Original", img);
    cv::imshow("Segmentiert", segmented);
    cv::waitKey(0);
    return 0;
}

// Weitere Informationen zu OpenCV und Bildverarbeitung:
// - OpenCV Dokumentation: https://docs.opencv.org/4.x/
// - Tutorials zu Bildverarbeitung: https://learnopencv.com/getting-started-with-opencv/
