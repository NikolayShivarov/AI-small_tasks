//#include<bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

class Board{
  public:
  int board_size;
  vector<int> queens; //the row of the queen on column i
  vector<int> queens_in_row;//number of queens
  vector<int> queens_in_main_diag;
  vector<int> queens_in_sec_diag;
  vector<int> helper;
  int conflicts;
  Board(int N){
    board_size=N;
    helper.resize(N);
    queens.resize(N);
    queens_in_row.resize(N);
    queens_in_main_diag.resize(2*N);
    queens_in_sec_diag.resize(2*N);
    for(int i=0;i<2*N;i++){
       queens_in_main_diag[i]=0;
       queens_in_sec_diag[i]=0;
    }
    for(int i=0;i<N;i++){
       queens_in_row[i]=0;
       helper[i]=0;
    }
    for(int i=0;i<N;i++){
        queens[i]=rand()%N;
        queens_in_row[queens[i]]++;
        queens_in_main_diag[i-queens[i]+N]++;
        queens_in_sec_diag[i+queens[i]]++;
    }
    conflicts=count_conflicts();
  }

  int count_conflicts(){
    int N=board_size;
    int sum=0;
    for(int i=0;i<N;i++) sum+= (queens_in_row[i]*(queens_in_row[i]-1))/2;
    for(int i=0;i<2*N;i++) sum+= (queens_in_main_diag[i]*(queens_in_main_diag[i]-1))/2;
    for(int i=0;i<2*N;i++) sum+= (queens_in_sec_diag[i]*(queens_in_sec_diag[i]-1))/2;
    return sum;
  }

  bool is_solved(){
    if (conflicts==0) return true;
    return false;
  }

  int count_new_conflicts(int col,int new_row){
      int sum=0;
      sum+=queens_in_row[new_row];
      sum+=queens_in_main_diag[col-new_row+board_size];
      sum+=queens_in_sec_diag[col+new_row];
      return sum;
  }

  int count_removed_conflicts(int col){
      int sum=0;
      sum+=queens_in_row[queens[col]];
      sum+=queens_in_main_diag[col-queens[col]+board_size];
      sum+=queens_in_sec_diag[col+queens[col]];
      sum-=3;
      return sum;
  }

  bool  is_in_conflict(int col){
    return queens_in_row[queens[col]]!=1 || queens_in_main_diag[col-queens[col]+board_size]!=1 || queens_in_sec_diag[col+queens[col]]!=1;
  }

  void step(){
    int col=rand()%board_size;
    int count_min=0;
    while(!is_in_conflict(col)){
        col=rand()%board_size;
    }
    int minimal=board_size+1,min_row;
    vector<int> minimals;
    for(int i=0;i<board_size;i++){
        if(i==queens[col]){
                helper[i]=-1;
                continue;
        }
        int curr=count_new_conflicts(col,i);
        helper[i]=curr;
        if(curr==minimal) count_min++;
        if(curr<minimal){
            minimal=curr;
            min_row=i;
            count_min=1;
        }
    }
    minimals.resize(count_min);
    int j=0;
    for(int i=0;i<board_size;i++){
        if(i==queens[col]) continue;
        if(minimal==helper[i]){
           minimals[j]=i;
           j++;
        }
    }
    min_row=minimals[rand()%count_min];
    int prev=count_removed_conflicts(col);
    if (minimal<=prev){
        conflicts-=prev;
        conflicts+=minimal;
        queens_in_row[queens[col]]--;
        queens_in_main_diag[col-queens[col]+board_size]--;
        queens_in_sec_diag[col+queens[col]]--;
        queens[col]=min_row;
        queens_in_row[queens[col]]++;
        queens_in_main_diag[col-queens[col]+board_size]++;
        queens_in_sec_diag[col+queens[col]]++;
    }

  }

  void solve(){
    while(!is_solved()){
        step();
    }
  }
  void print(){
     for(int i=0;i<board_size;i++){
     cout<<endl;
     for(int j=0;j<board_size;j++){
         if(queens[j]==i) cout<<"*";
         else cout<<"-";
     }
     }
  }


};




int main(){
Board b(20);
b.solve();
b.print();
Board b2(10000);
b2.solve();
cout<<"solved"<<endl;

return 0;
}
