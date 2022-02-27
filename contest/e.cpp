#include <bits/stdc++.h>
using namespace std;
int dp[100][100];
int main() {
   int n; cin >> n;
   int a[n+1][n+1];
   for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= i; j++) {
         cin >> a[i][j];
      }
   }
   for(int i = 1; i <=n; i++) {
      for(int j = 1; j <= i; j++) {
         dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i][j];
      }
   }
   cout << dp[n][n];
}