#include<iostream>
#include<bits/stdc++.h>
#define ll long long int 
using namespace std;
void dfs(int src,int dest,map<int,vector<int>> &mp,map<int,bool> &visited)
{
    
    visited[src]=true;
    for(auto x:mp[src])
    {
        if(visited[x]==false)
        dfs(x,dest,mp,visited);
    }
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    map<int,bool> visited;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        visited[arr[i]]=false;
    }
    
    map<int,vector<int>> mp;
    int x,y;
    int l;
    cin>>l;
    for(int i=0;i<l;i++)
    {
        cin>>x;
        cin>>y;
        mp[x].push_back(y);
    }
   int src,dest;
   cin>>src>>dest;
   dfs(src,dest,mp,visited);
   for(auto x:visited)
   cout<<x.first<<" "<<x.second<<endl;
   if(visited[dest]==true)
   cout<<"1"<<endl;
   else
   cout<<"0"<<endl;
   
   return 0;
}