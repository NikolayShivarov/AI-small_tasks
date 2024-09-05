#include<iostream>
using namespace std;


class Game{
 public:
 char board[3][3];
 bool isComputerTurn;
 char computerSymbol;
 char personSymbol;

 Game(bool isFirst){
  for(int i=0;i<3;i++)for(int j=0;j<3;j++) board[i][j]=' ';
  if(isFirst){
    computerSymbol='o';
    personSymbol='x';
    isComputerTurn=false;
    printBoard();
  }
  else{
    computerSymbol='x';
    personSymbol='o';
    isComputerTurn=true;
  }

 }

 void printBoard() {

    cout << "-------------" << endl;

    for (int i = 0; i < 3; i++) {
        cout << "| ";
        for (int j = 0; j < 3; j++) {
            cout << board[i][j];
            cout << " | ";
        }
        cout << endl << "-------------" << endl;
    }
}

int evaluateBoard(int depth){
    //checking rows for victory
    for(int row = 0; row < 3; row++){
        if(board[row][0] == board[row][1] && board[row][1] == board[row][2]){
            if (board[row][0] == computerSymbol) return 10-depth;
            else if (board[row][0] == personSymbol) return (-10)+depth;
        }
    }
    //checking columns for victory
    for(int col = 0; col < 3; col++){
        if (board[0][col] == board[1][col] && board[1][col] == board[2][col]){
            if (board[0][col] == computerSymbol) return 10-depth;
            else if (board[0][col] == personSymbol) return (-10)+depth;
        }
    }

    //checking main diagonal for victory
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]){
        if (board[0][0] == computerSymbol) return 10-depth;
        else if (board[0][0] == personSymbol) return (-10)+depth;

    }

    //checking second diagonal for victory
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]){
        if (board[0][2] == computerSymbol) return 10-depth;
        else if (board[0][2] == personSymbol) return (-10)+depth;
        }
    //if it is tied => return 0
    return 0;
}

bool areThereMovesLeft(){
    for(int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ' ') return true;
    return false;
}

int maximizer(int a, int b, int depth){
    int curScore=evaluateBoard(depth);
    // check if some of the players is winning
    if(curScore != 0) return curScore;
    //no moves left and no winner => tied
    if(!areThereMovesLeft()) return 0;
    //init best score for max player is the smallest possible number
    int bestScore = -11;

    for(int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if(board[i][j] == ' '){
                board[i][j] = computerSymbol;
                //recursive call, maximizer
                bestScore = max(bestScore, minimizer(a, b, depth + 1));
                //undo so maximizer can try next possible moves
                board[i][j] = ' ';
                if (bestScore >= b) return bestScore;
                a = max(a, bestScore);
            }
        }
    }
    return bestScore;
}

int minimizer(int a, int b, int depth){
    int curScore=evaluateBoard(depth);
    // check if some of the players is winning
    if (curScore != 0) return curScore;
    if (!areThereMovesLeft()) return 0;
    //init best score for min player is the biggest possible number
    int bestScore = 11;

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(board[i][j] == ' '){
                board[i][j] = personSymbol;
                //recursive call, minimizer
                bestScore = min(bestScore, maximizer(a, b, depth + 1));
                //undo so minimizer can try next possible moves
                board[i][j] = ' ';
                if (bestScore <= a) return bestScore;
                b = min(b, bestScore);
            }
        }
    }
    return bestScore;
}

pair<int, int> findBestTurnForComputer(){
    int bestValue = 11;
    pair<int, int> bestNextTurn;

    bestNextTurn.first = -1;
    bestNextTurn.second = -1;

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(board[i][j] == ' '){
                board[i][j] = computerSymbol;

                int curTurnValue = maximizer(-11,11, 0);

                //undo
                board[i][j] = ' ';

                if (curTurnValue < bestValue){
                    bestNextTurn.first = i;
                    bestNextTurn.second = j;
                    bestValue = curTurnValue;
                }
            }
        }
    }
    return bestNextTurn;
}

bool isThereWinner(){
    if (evaluateBoard(0) != 0) return true;
    return false;
}


bool makeTurn(int i, int j){
    if (board[i][j] == ' '){
        if(isComputerTurn) board[i][j] = computerSymbol;
        else board[i][j] = personSymbol;

        cout << "==========" << endl;

        printBoard();

        if (isThereWinner()){
            if(isComputerTurn)cout << "YOU LOST!" << endl;
            else cout << "YOU WON!" << endl;

        }

        return true;
    }

    cout << "This cell is not empty! Choose another." << endl;
    return false;
}

void play(){
  while (areThereMovesLeft() && !isThereWinner()){
        int i, j;
        if (!isComputerTurn){
           do{
               cout << "Row:"; cin >> i;
               cout << "Column:"; cin >> j;
           } while (!makeTurn(i - 1, j - 1));
           isComputerTurn = !isComputerTurn;
           continue;
        }
        pair<int, int> bestTurn = findBestTurnForComputer();
        makeTurn(bestTurn.first, bestTurn.second);
        isComputerTurn = !isComputerTurn;
    }
    if(!isThereWinner()) cout<<"NO WINNER"<<endl;
}





};


int main(){
    bool isFirst;
    cout << "Do you want to start the game? yes/no : ";
    string input;
    getline (cin, input);
    while(input!=string("yes") && input!=string("no")){
          cout<<"Please write yes or no"<<endl;
          getline (cin, input);
          }
    if(input==string("yes")) isFirst=true;
    else isFirst=false;
    Game g(isFirst);
    g.play();

    bool want;
    do{
    cout<<"Do you want to play another game"<< endl;
    getline (cin, input);
    while(input!=string("yes") && input!=string("no")){
          cout<<"Please write yes or no"<<endl;
          getline (cin, input);
          }
    if(input==string("yes")) want=true;
    else want=false;
    if(want){
        cout << "Do you want to start the game? yes/no : ";
        getline (cin, input);
    while(input!=string("yes") && input!=string("no")){
          cout<<"Please write yes or no"<<endl;
          getline (cin, input);
          }
    if(input==string("yes")) isFirst=true;
    else isFirst=false;
    Game g(isFirst);
    g.play();
    }
    }while(want==true);

cout<<"Thanks for playing!";
return 0;
}
