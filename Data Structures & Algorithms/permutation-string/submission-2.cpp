class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }
        
        vector<int> count1(26, 0);
        vector<int> count2(26, 0);

        for (char c : s1) {
            count1[c - 'a']++;
        }

        int windowSize = s1.size();

        //first window
        for (int i = 0; i < windowSize; i++) {
            count2[s2[i] - 'a']++;
        }

        if (count1 == count2) {
            return true;
        }

        //slide windows
        for (int right = windowSize; right < s2.size(); right++) {
            count2[s2[right] - 'a']++;

            //adjust left to keep window size
            int left = right - windowSize;
            count2[s2[left] - 'a']--;

            if (count1 == count2) {
                return true;
            }
        }

        return false;
    }
};
