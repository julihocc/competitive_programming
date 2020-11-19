// oro.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

using namespace std;

// A utility function that returns 
// maximum of two integers 
int max(int a, int b) { return (a > b) ? a : b; }

// Returns the maximum value that 
// can be put in a knapsack of capacity W 
int knapSack(int W, vector<int> wt, vector<int> val, int n)
{

    // Base Case 
    if (n == 0 || W == 0)
        return 0;

    // If weight of the nth item is more 
    // than Knapsack capacity W, then 
    // this item cannot be included 
    // in the optimal solution 
    if (wt[n - 1] > W)
        return knapSack(W, wt, val, n - 1);

    // Return the maximum of two cases: 
    // (1) nth item included 
    // (2) not included 
    else
        return max(
            val[n - 1]
            + knapSack(W - wt[n - 1],
                wt, val, n - 1),
            knapSack(W, wt, val, n - 1));
}

int main()
{
    //cout << "Hello World!\n";
    int N;
    int B;
    cin >> N >> B;
    vector <int> val(N);
    for (int i = 0; i < N; i++) {
        cin >> val.at(i);
    }

    int S = 0;
    for (int i = 0; i < N; i++) {
        S = S + val.at(i);
    }
    cout << S - knapSack(S - B, val, val, N) - B;
}
