impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        nums.iter().fold(1, |a, &b| {
            let mut c: i32 = if b > 0 { 1 } else if b < 0 { -1 } else { 0 };
            a * c
        })
    }
}