#include <bits/stdc++.h>
using namespace std;

int main()
{
   freopen("ladder.in", "r", stdin);
   freopen("ladder.out", "w", stdout);
   long long n;
   cin >> n;
   long long a[n + 1], dp[10000];
   for (int i = 1; i <= n; i++)
   {
      cin >> a[i];
   }

   dp[0] = 0;
   dp[1] = a[1];
   for (int i = 2; i <= n; i++)
   {
      dp[i] = max(dp[i - 1], dp[i - 2]) + a[i];
   }
   cout << dp[n];
}