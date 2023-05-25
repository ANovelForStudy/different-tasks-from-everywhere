/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    return arr.map(fn);
}


// ________________TESTING___________________

function func(number) {
    return number*number;
}

console.log(map([1, 2, 3, 4, 5], func))
