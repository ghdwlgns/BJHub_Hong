#include <iostream>
#include <string>

using namespace std;

int main() {
    int cnt = 0, s_size = 0;
    string s;
    
    getline(cin, s);
    
    while(s_size < s.size()) {
        if(s[s_size] != ' ' && (s[s_size + 1] == ' ' || s_size + 1 == s.size()))    cnt++;
        s_size++;
    }
    
    cout << cnt;
    
    return 0;
}