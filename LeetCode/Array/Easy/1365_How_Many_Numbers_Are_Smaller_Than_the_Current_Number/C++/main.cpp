
#include <iostream>
#include <vector>


using std::vector;
using std::cout;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            int counter = 0;
            for (int j = 0; j < nums.size(); j++)
            {
                if (i == j)
                    continue;
                if (nums[i] > nums[j])
                    counter++;
            }
            result.push_back(counter);
        }
        return result;
    }
};


int main()
{
    // Expected: [4,0,1,1,3]
    vector<int> test = {8,1,2,2,3};
    Solution a;
    
    vector<int> result = a.smallerNumbersThanCurrent(test);

    for (auto i = result.begin(); i != result.end(); ++i)
    {
        cout << *i << " ";
    }
    cout << "\n";

    return 0;
}
