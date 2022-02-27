#include <bits/stdc++.h>
using namespace std;
int dp[300][10000];
int main()
{
   int s, n, p;
   cin >> s >> n;
   int a[n + 1];
   for (int i = 1; i <= n; i++) {
      cin >> a[i];
   }
   for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= s; j++) {
         if (j - a[i] > 0) {
            dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - a[i]]) + a[i]);
         }
         else {
             dp[i][j] = dp[i - 1][j];
         }
      }
   }
   cout << dp[n][s];
}