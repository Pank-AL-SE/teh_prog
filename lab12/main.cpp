#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

using namespace std;

// Функция поиска минимального элемента в одномерном массиве
pair<int, int> findMinElement(const vector<int>& arr) {
    int minValue = arr[0];
    int minIndex = 0;

    for (int i = 1; i < arr.size(); ++i) {
        if (arr[i] < minValue) {
            minValue = arr[i];
            minIndex = i;
        }
    }

    return { minValue, minIndex };
}

// Функция сортировки пузырьком
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Функция бинарного поиска (массив должен быть отсортирован)
int binarySearch(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

// Функция поиска минимального элемента в двумерном массиве
pair<int, pair<int, int>> findMinElement2D(const vector<vector<int>>& arr) {
    int minValue = numeric_limits<int>::max();
    int minRow = -1, minCol = -1;

    for (int i = 0; i < arr.size(); ++i) {
        for (int j = 0; j < arr[i].size(); ++j) {
            if (arr[i][j] < minValue) {
                minValue = arr[i][j];
                minRow = i;
                minCol = j;
            }
        }
    }

    return { minValue, { minRow, minCol } };
}

// Функция переворота массива
void reverseArray(vector<int>& arr) {
    int size = arr.size();
    for (int i = 0; i < size / 2; ++i) {
        swap(arr[i], arr[size - 1 - i]);
    }
}

// Функция циклического сдвига массива влево
void leftRotate(vector<int>& arr, int d) {
    int n = arr.size();
    d %= n;
    rotate(arr.begin(), arr.begin() + d, arr.end());
}

// Функция замены значения в массиве
void replaceValue(vector<int>& arr, int oldValue, int newValue) {
    for (auto& value : arr) {
        if (value == oldValue) {
            value = newValue;
        }
    }
}

// Функция для вычисления различных значений
void findSome(double nD, double n1, double n2, double N1, double N2) {
    double S = 11;

    double n = n1 + n2;
    double N = N1 + N2;

    double ngal = n1 * log2(n1) + n2 * log2(n2);
    double vD = (2 + nD) * log2(2 + nD);
    double v = N * log2(n);
    double L = vD / v;
    double lgal = (2 / n1) * (n2 / N2);
    double I = (2 / n1) * (2 / N2) * (N1 + N2) * log2(n1 + n2);
    double tgal1 = (v * v) / (S * vD);
    double tgal2 = (n1 * N2 * (n1 * log(n1) * n2 * log2(n2)) * log2(n)) / (2 * S * n2);
    double tgal3 = (n1 * N2 * N * log2(n)) / (2 * S * n2);
    double pusto1 = lgal * lgal * v;
    double pusto2 = (vD * vD) / v;

    cout << "nD " << nD << endl;
    cout << "n1 " << n1 << endl;
    cout << "n2 " << n2 << endl;
    cout << "n " << n << endl;
    cout << "N1 " << N1 << endl;
    cout << "N2 " << N2 << endl;
    cout << "N " << N << endl;
    cout << "ngal " << ngal << endl;
    cout << "vD " << vD << endl;
    cout << "v " << v << endl;
    cout << "L " << L << endl;
    cout << "lgal " << lgal << endl;
    cout << "I " << I << endl;
    cout << "tgal1 " << tgal1 << endl;
    cout << "tgal2 " << tgal2 << endl;
    cout << "tgal3 " << tgal3 << endl;
    cout << "pusto1 " << pusto1 << endl;
    cout << "pusto2 " << pusto2 << endl;
}

int main() {
    findSome(2, 23, 5, 46, 19); // findMin
    findSome(1, 19, 7, 43, 26); // bubbleSort
    findSome(3, 22, 9, 53, 28); // binarySearch
    findSome(1, 25, 9, 102, 35); // findMinElement2D
    findSome(1, 16, 5, 54, 23); // reverseArray
    findSome(2, 16, 4, 32, 12); // leftRotate
    findSome(3, 15, 5, 22, 11); // replaceValue
}