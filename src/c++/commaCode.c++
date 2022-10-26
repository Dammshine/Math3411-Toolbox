#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

string commaCodeDecodeHelper(string code, int pos, vector<string> &vs) {
    if (pos == code.size()) return "";
    string tmp;
    for (int i = pos; i < code.size(); i++) {
        tmp.push_back(code[i]);
        for (int j = 0; j < vs.size(); j++) {
            if (tmp == vs[j]) {
                string result = commaCodeDecodeHelper(code, i + 1, vs);
                // cout << tmp << " " << result << endl;
                if (result != "Invalid") return "s" + to_string(j + 1) + result;
            }
        }
    }
    return "Invalid";
}


string commaCodeDecode(string code, int len) {
    vector<string> vs;
    for (int i = 0; i <= len; i++) {
        if (i == 0) vs.push_back("0");
        else if (i == len) vs.push_back(std::string(len, '1'));
        else vs.push_back("1" + vs[vs.size() - 1]);
    }
    for (auto i : vs) cout << i << endl;

    return commaCodeDecodeHelper(code, 0, vs);
}

/* int main() {
    cout << commaCodeDecode("01110111111101111", 4);
} */