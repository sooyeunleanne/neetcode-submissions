class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";

        for (string& s : strs) {
            result += to_string(s.size()) + "#" + s;
        }

        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;

        int i = 0;

        while (i < s.size()) {
            int j = i;

            // find delimiter "#"
            while (s[j] != '#') {
                j++;
            }

            //convert length string to integer
            int length = stoi(s.substr(i, j - i));

            // get the word
            string word = s.substr(j + 1, length);

            // add the word to result array
            result.push_back(word);


            i = j + 1 + length;
        }

        return result;
    }
};
