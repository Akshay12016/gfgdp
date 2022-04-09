#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int t;
    cin >> t;
    int d[n], pos[n], pos1[n], count = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> d[i];
    }
    for (int i = 0; i < n - 1; i++)
    {
        if (d[i] <= d[i + 1])
        {
            pos[i] = 1;
        }
        else
        {
            pos[i] = 0;
        }
    }
    if (pos[n - 1] >= pos[n - 2])
        pos[n - 1] = 1;
    else
        pos[n - 1] = 0;
    int v[n];
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < n; j++)
        {
            d[j] = d[j] + v[j];
        }
    }
    for (int i = 0; i < n - 1; i++)
    {
        if (d[i] <= d[i + 1])
        {
            pos1[i] = 1;
        }
        else
        {
            pos1[i] = 0;
        }
    }
    if (pos1[n - 1] >= pos1[n - 2])
        pos1[n - 1] = 1;
    else
        pos1[n - 1] = 0;
    for (int i = 0; i < n; i++)
    {
        if (pos[i] != pos1[i])
        {
            count = count + 1;
        }
    }
    cout << count << endl;
}