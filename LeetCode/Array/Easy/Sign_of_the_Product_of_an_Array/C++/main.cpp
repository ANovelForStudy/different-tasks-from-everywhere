class Solution {
public:
    int arraySign(std::vector<int>& n) {
        return std::accumulate(n.begin(), n.end(), 1, [](int a, int b) {return b > 0 ? a : b < 0 ? -a : 0;});
    }
};