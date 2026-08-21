class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        sort(nums.begin(), nums.end());

        for (int first = 0; first < nums.size() - 2; first++) {
            //skip duplicate first numbers
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }

            //two pointers
            int second = first + 1;
            int third = nums.size() - 1;

            while (second < third) {
                int sum = nums[first] + nums[second] + nums[third];

                if (sum == 0) {
                    result.push_back({
                        nums[first], nums[second], nums[third]
                    });

                    second++;
                    third--;

                    while (second < third && nums[second] == nums[second - 1]) {
                        second++;
                    }
                    while (second < third && nums[third] == nums[third + 1]) {
                        third--;
                    }
                }
                else if (sum < 0) {
                    second++;
                }
                else {
                    third--;
                }
            }
        }

        return result;
    }
};
