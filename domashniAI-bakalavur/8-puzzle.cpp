
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <ctime>
#include <iomanip>
//#include <bits/stdc++.h>
using namespace std;

 class Board {

public:
    vector<vector<int>> tiles;
    int size_of_board;
    int empty_row_pos;
    int empty_col_pos;
    int curr_empty_row;
    int curr_empty_col;
    Board(vector<vector<int>> input,int input_size,int input_row,int input_col){
       size_of_board=input_size;
       empty_row_pos=input_row;
       empty_col_pos=input_col;
       tiles.resize(size_of_board);
       for(int i=0;i<size_of_board;i++) tiles[i].resize(size_of_board);
       for(int i=0;i<size_of_board;i++)
        for(int j=0;j<size_of_board;j++){
          tiles[i][j]= input[i][j];
       }
        curr_empty_row=find_empty_row();
        curr_empty_col=find_empty_col();
    }
    Board(){
    }


    void operator=(const Board& other){
       size_of_board=other.size_of_board;
       empty_row_pos=other.empty_row_pos;
       empty_col_pos=other.empty_col_pos;
       tiles.resize(size_of_board);
       for(int i=0;i<size_of_board;i++) tiles[i].resize(size_of_board);
       for(int i=0;i<size_of_board;i++)
        for(int j=0;j<size_of_board;j++){
          tiles[i][j]= other.tiles[i][j];
       }
       curr_empty_row=other.curr_empty_row;
       curr_empty_col=other.curr_empty_col;

    }

     bool is_solved() const{
       if(manhattan()==0) return true;
       return false;
     }

     int manhattan() const{
        int result=0;
        for(int i=0;i<size_of_board;i++)
         for(int j=0;j<size_of_board;j++){
            result+=manhattan_of(i,j);
         }
        return result;

    }
    int manhattan_of(int row,int col) const{
      if(tiles[row][col]==0) return 0;
      int zero=empty_row_pos*size_of_board+empty_col_pos;
      int target_row,target_col;
      if(zero<tiles[row][col]){
       target_row=tiles[row][col]/size_of_board;
       target_col=tiles[row][col]%size_of_board;
      }
      else{
        target_row=(tiles[row][col]-1)/size_of_board;
        target_col=(tiles[row][col]-1)%size_of_board;
      }
      return abs(target_row-row)+abs(target_col-col);
    }


     bool operator==(const Board& other) const{
        for(int i=0;i<size_of_board;i++)
        for(int j=0;j<size_of_board;j++){
          if(tiles[i][j]!=other.tiles[i][j]) return false;
       }
       return true;
    }
      bool isSolvable() const{
      int inversions= count_inversions();
      if(size_of_board%2==1){
        if(inversions%2==1) return false;
      }
      int row=find_empty_row();
      if(size_of_board%2==0){
        if((inversions+row)%2==0) return false;
      }
      return true;
    }

     int count_inversions_of(int row,int col)const{
       int result=0;
       int current=tiles[row][col];
       for(int j=col+1;j<size_of_board;j++)
        if(tiles[row][j]!=0 && current>tiles[row][j]) result++;
       for(int i=row+1;i<size_of_board;i++)
            for(int j=0;j<size_of_board;j++)
                if(tiles[i][j]!=0 && current>tiles[i][j]) result++;
       return result;
    }

     int count_inversions() const{
      int result=0;
      for(int i=0;i<size_of_board;i++)
        for(int j=0;j<size_of_board;j++){
            if(tiles[i][j]!=0) result+=count_inversions_of(i,j);
        }

     return result;
    }

     int find_empty_row() const{
        for(int i=0;i<size_of_board;i++)
         for(int j=0;j<size_of_board;j++){
            if (tiles[i][j]==0) return i;
         }
    }

   const int find_empty_col() const{
        for(int i=0;i<size_of_board;i++)
         for(int j=0;j<size_of_board;j++){
            if (tiles[i][j]==0) return j;
         }
    }

    Board generate_left(){
     Board b=*this;
     swap(b.tiles[curr_empty_row][curr_empty_col+1],b.tiles[curr_empty_row][curr_empty_col]);
     b.curr_empty_col++;
     return b;
    }
    Board generate_right(){
     Board b=*this;
     swap(b.tiles[curr_empty_row][curr_empty_col-1],b.tiles[curr_empty_row][curr_empty_col]);
     b.curr_empty_col--;
     return b;
    }
    Board generate_up(){
     Board b=*this;
     swap(b.tiles[curr_empty_row+1][curr_empty_col],b.tiles[curr_empty_row][curr_empty_col]);
     b.curr_empty_row++;
     return b;
    }
    Board generate_down(){
     Board b=*this;
     swap(b.tiles[curr_empty_row-1][curr_empty_col+1],b.tiles[curr_empty_row][curr_empty_col]);
     b.curr_empty_row--;
     return b;
    }
};

class BoardNode{
  public:
    Board board;
    vector<string> path;
    int distance;
    string prev;
    BoardNode(const Board& b,int d,string& dir,vector<string>& history){
        board=b;
        distance=d;
        prev=dir;
        path.resize(history.size());
        for(int i=0;i<history.size();i++){
        path[i]=history[i];
      }

    }
    BoardNode(const Board& b){
        board=b;
        distance=0;
        prev="";
    }
    BoardNode(){
    }

    void operator=(const BoardNode& other){
      board=other.board;
      path.resize(other.path.size());
      for(int i=0;i<other.path.size();i++){
        path[i]=other.path[i];
      }
      distance=other.distance;
      prev=other.prev;
    }
     int h() const{
      return distance+ board.manhattan();
    }

    void generate_neighbours(priority_queue<BoardNode>& v){
         if(prev!="right" && board.curr_empty_col!=board.size_of_board-1){
            string dir="left";
            vector<string> history;
            for(int i=0;i<path.size();i++){
            history.push_back(path[i]);
            }
            history.push_back(dir);
            v.push(BoardNode(board.generate_left(),distance+1,dir,history));
         }
         if(prev!="left" && board.curr_empty_col!=0){
            string dir="right";
            vector<string> history;
            for(int i=0;i<path.size();i++){
            history.push_back(path[i]);
            }
            history.push_back(dir);
            v.push(BoardNode(board.generate_right(),distance+1,dir,history));
         }
         if(prev!="up" && board.curr_empty_row!=0){
            string dir="down";
            vector<string> history;
            for(int i=0;i<path.size();i++){
            history.push_back(path[i]);
            }
            history.push_back(dir);
            v.push(BoardNode(board.generate_down(),distance+1,dir,history));
         }
         if(prev!="down" && board.curr_empty_row!=board.size_of_board-1){
            string dir="up";
            vector<string> history;
            for(int i=0;i<path.size();i++){
            history.push_back(path[i]);
            }
            history.push_back(dir);
            v.push(BoardNode(board.generate_up(),distance+1,dir,history));
         }
    }

    int solve(){
       clock_t Start, End;
       Start=clock();
       if (board.is_solved()){
        return 0;
       }
       if(!board.isSolvable()){
        cout<<"Not solvable";
        return -1;
       }
       BoardNode minimal=*this;
       priority_queue<BoardNode> Q;
       generate_neighbours(Q);
       bool ready=false;
       int curr_min=h()+10000;
       while (!Q.empty() && !ready){
        BoardNode curr = Q.top();
        Q.pop();
        if(curr.h()>curr_min) ready=true;
        if(curr.board.is_solved() && curr.h()<curr_min){
            minimal=curr;
            curr_min=minimal.distance;
        }
        curr.generate_neighbours(Q);
       }
       End=clock();
       double time_taken = double(End - Start) / double(CLOCKS_PER_SEC);
       cout << "Time taken by program is : " << fixed
         << time_taken << setprecision(2);
         cout << " sec " << endl;
       cout<<minimal.distance<<endl;
       for(int i=0;i<minimal.path.size();i++){
        cout<<minimal.path[i];
        cout<<endl;
       }
       return minimal.distance;
    }




};

 bool operator<(const BoardNode& bn1,const BoardNode& bn2){
      return bn1.h()>bn2.h();
    }


int main(){
  cout<<"Enter size: ";
  int N;
  cin>>N;
  int n=sqrt(N+1);
  cout<<"Enter index: ";
  int index,empty_row,empty_col;
  cin>>index;
  if(index==-1){
    empty_row=n-1;
    empty_col=n-1;
  }
    else{
    empty_row=index/n;
    empty_col=index%n;

  }
  if(index>N){
    cout<<"Index too BIG";
    return -1;
  }

  vector<vector<int>> v;
  v.resize(n);
  cout<<"Enter Board: "<<endl;
  for(int i=0;i<n;i++) v[i].resize(n);
  for(int i=0;i<n;i++)for(int j=0;j<n;j++) cin>> v[i][j];
  Board b(v,n,empty_row,empty_col);
  BoardNode bn(b);
  bn.solve();
  return 0;
}

 /* 102
    367
    845 */

