#include <bits/stdc++.h>

int main(){
    int mat[5][5]={0};

    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            mat[i][j]=i+j;
        }
    }
    
    return 0;
}