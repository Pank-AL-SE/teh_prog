#include <iostream>
#include <cmath>

using namespace std;

#define n 5
#define v 20

int I(int eta) {
    return static_cast<int>(std::log2(eta) / 3) + 1;
}

int K(int eta, int i) {
    double result = 1;
    for (int j = 1; j < i; ++j) {
        result += static_cast<double>(eta) / std::pow(8, j);
    }
    return static_cast<int>(result);
}

double eta2KFunc(int eta) {
    return static_cast<double>(eta) * std::log2(static_cast<double>(eta));
}

double NkFunc(double eta) {
    return 2 * eta * std::log2(eta);
}

double NFunc(int k, double Nk) {
    return static_cast<double>(k) * Nk;
}

double VFunc(int k, double Nk, double eta) {
    return static_cast<double>(k) * Nk * std::log2(2 * eta);
}

double PFunc(double N) {
    return 3 * N / 8;
}

double TFunc(double P) {
    return P / (static_cast<double>(n) * v);
}

double BFunc(double V) {
    return V / 3000;
}

double tauFunc(double T) {
    return T / 2;
}

double tnFunc(double tau, double B) {
    return tau / std::log(B);
}

int main()
{
    int eta[] = {8, 300, 400, 512};

    for (const auto& it : eta) {
        cout << "===============================================\n";
        int i = I(it);
        int k = K(it, i);
        double eta2k = eta2KFunc(it);
        double Nk = NkFunc(eta2k);
        double N = NFunc(k, Nk);
        double V = VFunc(k, Nk, eta2k);
        double P = PFunc(N);
        double T = TFunc(P);
        double B = BFunc(V);
        double tau = tauFunc(T);
        double tn = tnFunc(tau, B);
        
        cout << "eta = " << it << endl;
        cout << "i = " << i << endl;
        cout << "k = " << k << endl;
        cout << "eta2k = " << eta2k << endl;
        cout << "Nk = " << Nk << endl;
        cout << "N = " << N << endl;
        cout << "V = " << V << endl;
        cout << "P = " << P << endl;
        cout << "T = " << T << endl;
        cout << "B = " << B << endl;
        cout << "tau = " << tau << endl;
        cout << "tn = " << tn << endl;
    }

    return 0;
}