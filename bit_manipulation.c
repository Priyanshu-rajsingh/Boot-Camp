/*  Bit Manipulation
        n = number on which operations are performed
        i = position
        k = changing value number
*/

#include<stdio.h>



int getbit(int n, int i){
    if(((1 << i) & n ) != 0)
        return 1;
    else
        return 0;
}

int setbit(int n, int i){
    return (n | (1 << i));
}

int clearbit(int n, int i){
    return (n & ~(1 << i));
}

int togglebit(int n, int i){
    return (n ^ (1 << i));
}

int updatebit(int n, int i, int k){
    int mask = ~(1 << i);
    n = n & mask;
    return (n | (k << i));
}

void main(){
    
    printf("%d\n",getbit(5,1));
    printf("%d\n",setbit(5,1));
    printf("%d\n",clearbit(5,1));
    printf("%d\n",togglebit(5,1));
    printf("%d\n",updatebit(5,1,1));
}
