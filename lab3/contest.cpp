#include <bits/stdc++.h>
using namespace std;

int main() {
   int n;
   cin >> n;
   vector<int> v;
   v[0] = 0;
   v[1] = 1;
   for(int i = 2; i < n; i++) {
      v[i] = v[i-1] + v[i-2];
   }
   for(int i = 0;) {
      cout << v[i] << endl
   }
}