//C++ Program to implement Kadane's Algorithm

#include<iostream.h>

using namespace std;

int kadanes(int arr[],int length) {
   int highestMax = 0;
   int currEleMax = 0;
   for(int i = 0; i < length; i++){
      currEleMax =max(arr[i],currEleMax + arr[i]) ;
      highestMax = max(highestMax,currEleMax);
   }
   return highestMax;
}
int main() {
   cout << "Enter the array length: ";
   int l;
   cin >> l;
   int Arr[l];
   cout << "Enter the elements of array: ";
   for (int i = 0; i < l; i++) {
      cin >> Arr[i];
   }
   cout << "The Maximum Sum is: "<<kadanes(Arr,l) << endl;
   return 0;
}



