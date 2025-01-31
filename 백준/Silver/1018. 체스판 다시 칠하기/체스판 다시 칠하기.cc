#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string board[50];
string Wchessboard[8] = {
    {"WBWBWBWB"},
    {"BWBWBWBW"},
    {"WBWBWBWB"},
    {"BWBWBWBW"},
    {"WBWBWBWB"},
    {"BWBWBWBW"},
    {"WBWBWBWB"},
    {"BWBWBWBW"}
};
string Bchessboard[8] {
    {"BWBWBWBW"},
    {"WBWBWBWB"},
    {"BWBWBWBW"},
    {"WBWBWBWB"},
    {"BWBWBWBW"},
    {"WBWBWBWB"},
    {"BWBWBWBW"},
    {"WBWBWBWB"}
};

int WstartCheck(int y, int x) {
    int cnt = 0;
    for(int i = y;i < y + 8;i++) {
        for(int j = x;j < x + 8;j++) {
            if(board[i][j] != Wchessboard[i - y][j - x])    cnt++;
        }
    }
    return cnt;
}

int BstartCheck(int y, int x) {
    int cnt = 0;
    for(int i = y;i < y + 8;i++) {
        for(int j = x;j < x + 8;j++) {
            if(board[i][j] != Bchessboard[i - y][j - x])    cnt++;
        }
    }
    return cnt;
}

int main() {
    int n, m;
    int Min = 251;
    
    cin >> n >> m;
    
    for(int i = 0;i < n;i++) {
        cin >> board[i];
    }
    
    for(int i = 0;i + 7 < n;i++) {
        for(int j = 0;j + 7 < m;j++) {
            Min = min(Min, min(BstartCheck(i, j), WstartCheck(i, j)));
        }
    }
    cout << Min << endl;
    return 0;
}