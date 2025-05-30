#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n; cin>>n;
    int arr[n];
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }

    int item; cin>>item;

    int loc=-1;

   for(int j=0;j<n;j++)
   {
       int l=0,r=n-1;
       while(l<=r)
       {
           int mid=l+((r-l)/2);

           if(arr[mid] == item)
           {
               loc=mid;
               break;
           }
           else if(arr[mid]<item)
           {
               l=mid+1;
           }
           else
           {
               r=mid-1;
           }
       }
   }

     if(loc==-1)
     {
         cout<<"not in the array"<<endl;
     }

     else
     {
         cout<<loc<<" is the index"<<endl;
     }

}


