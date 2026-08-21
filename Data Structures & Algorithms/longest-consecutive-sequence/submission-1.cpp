class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());

        int longest = 0;
        for (int num: nums_set) {
            if (nums_set.count(num - 1)) { 
                continue;
            }

            int length = 1;

            while (nums_set.count(num + length)) {
                length++;
            }

            longest = max(longest, length);
        }

        return longest;
    }
};
