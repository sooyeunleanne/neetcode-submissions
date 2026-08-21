class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;

        int max_area = 0;

        while (left < right) {
            int left_height = heights[left];
            int right_height = heights[right];

            int area = min(left_height, right_height) * (right - left) ;

            max_area = max(max_area, area);
            
            if (left_height < right_height) {
                left++;
            }
            else {
                right--;
            }
        }
        
        return max_area;
    }
};
