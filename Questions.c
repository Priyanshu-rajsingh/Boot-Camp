/*
Q1 : finding weather a number is odd or even without using mod operator
#include <stdio.h>

void main(){
    int n ;
    printf("Enter n value :");
    scanf("%d",&n);
    if((n & 1) == 0)
        printf("Even\n");
    else
        printf("Odd\n"); 
}
*/

/*//Q2 : check weather two numbers of the same sign or not 
#include <stdio.h>

void main(){
    int x = 12, y = -13;
    (x^y) < 0 ? printf("Opposite") : printf("Same") ;
}*/

/*
//# Q3 : Find the missing number
#include <stdio.h>

int findmissingnumber(int arr[], int n){
    
    int x1 = arr[0], x2 = 1;

    for (int i = 1; i < n; i++)
        x1 = x1 ^ arr[i];
    for (int i = 2; i < n + 2; i ++)
        x2 = x2 ^ i;

    return (x1 ^ x2);
}

void main(){
    int arr[4] = {1,2,3,5};
    printf("%d",findmissingnumber(arr,4));

}
*/

/*
//# Q4 : Odd occuring number
#include <stdio.h>

int oddoccuringelement(int arr[],int n){
    int a = arr[0];
    for (int i = 1; i < n; i++){
        a = a ^ arr[i];
    }
    return a;
}

void main(){
    int arr[5] = {2,4,3,2,4};
    printf("%d\n",oddoccuringelement(arr,5));
}*/

#include <stdio.h>

int alternatebitnumber(int arr, int n){

}

void main(){
    int arr[5];
    printf("");
}