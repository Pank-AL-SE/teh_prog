#include <iostream> // 3
#include <math.h>	// 1
#include <time.h>	// 1

using namespace std;	// 3

double lengthFunc(int eta1, int eta2) { // 5, 3
	return 0.9 * (eta1 + eta2) * log2(eta1 + eta2); //5, 1 
}

double dispersionFunc(int eta) {	//0, 2
	return (3.14 * 3.14 * eta * eta) / 6; // 1, 2
}

int exceptionLengthFunc(int eta) { // 1, 0
	bool* dictionary = new bool[eta]; // 4, 1
	for (int i = 0; i < eta; i++) { // 3, 2 
		dictionary[i] = false;	// 1, 0
	}
	int fill = 0; //0 , 1
	int length = 0; // 0, 1
	while (fill < eta) { // 1, 0
		int randIndex = rand() % eta; //2, 1
		if (!dictionary[randIndex]) { // 2, 0
			dictionary[randIndex] = true; //1, 0
			fill++; // 0, 0
		}
		length++;//0,0
	}
	return length; //0,0
}

int main() //1, 0
{
	srand(time(NULL)); //3 ,0

	int dictionaty[5] = { 16, 32, 64, 128, 80}; // 0, 7

	cout << "-----------------------------------------\n"; //5, 1

	for (int i = 0; i < 5; i++) { //0,0
		int exceptionLength = exceptionLengthFunc(dictionaty[i]);//0, 1
		
		double length = lengthFunc(dictionaty[i] / 2, dictionaty[i] / 2); // 0, 1

		double dispersion = dispersionFunc(dictionaty[i]); // 0, 1

		double deviation = sqrt(dispersion); //1, 1

		double delta = 1.0 / (2 * log2(dictionaty[i])); // 1,1

		cout << "dictionary length: " << dictionaty[i] << endl; //1, 1

		cout << "exception length: " << exceptionLength << endl; //0, 1

		cout << "teory length: " << length << endl; // 0, 1

		cout << "Dispersion length: " << dispersion << endl; //0 , 1

		cout << "Avg sqrt deviation: " << deviation << endl; //0, 1

		cout << "Error: " << delta << endl;	// 0, 1

		cout << "-----------------------------------------\n"; // 0, 0

	}

	return 0;	//0 , 0
}
