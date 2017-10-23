#include <iostream>
#include <cstring>
#include <fstream>
#include <ctime>

using namespace std;

int main() {
	srand(time(0));
	ofstream ofile("test_data.txt");
	for (int i = 0; i<20; ++i) {
		int n = rand() % 59 + 2;
		ofile << n << endl;
		for (int j = 0; j<n; ++j)ofile << -1000+rand() % 2001 << " ";
		ofile << endl;
	}
	ofile.close();
	ifstream ifile("test_data.txt");
    int n;
    int arr[60];
	while (ifile >> n) {
		for (int i = 0; i<n; ++i)ifile >> arr[i];
		cout << n << endl;
		for (int i = 0; i<n; ++i)cout << arr[i] << " ";
        cout << endl;
        //add your function here
	    for (int i = 0; i<n; ++i)cout << arr[i] << " ";
		cout << endl;
	}
	system("pause");
	ifile.close();
	return 0;
}