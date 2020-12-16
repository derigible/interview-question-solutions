// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

// Follow up: The overall run time complexity should be O(log (m+n)).



// Example 1:

// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.

// Example 2:

// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

// Example 3:

// Input: nums1 = [0,0], nums2 = [0,0]
// Output: 0.00000

// Example 4:

// Input: nums1 = [], nums2 = [1]
// Output: 1.00000

// Example 5:

// Input: nums1 = [2], nums2 = []
// Output: 2.00000



// Constraints:

//     nums1.length == m
//     nums2.length == n
//     0 <= m <= 1000
//     0 <= n <= 1000
//     1 <= m + n <= 2000
//     -106 <= nums1[i], nums2[i] <= 106

// Note that this code is linear in time and space complexity.
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  const newArray = mergeArrays(nums1, nums2)
  const isEven = newArray.length % 2 == 0
  if (isEven) {
      const right = newArray.length / 2
      return (newArray[right] + newArray[right - 1]) / 2
  } else {
      const middle = Math.floor((newArray.length) / 2)
      return newArray[middle]
  }
};

function mergeArrays(nums1, nums2) {
  const newArray = new Array(nums1.length + nums2.length)
  let ptr = 0
  let i = 0
  let j = 0
  while(ptr < newArray.length) {
      if(i < nums1.length && nums1[i] < nums2[j] || j == nums2.length) {
          newArray[ptr] = nums1[i]
          i += 1
      } else if(j < nums2.length) {
          newArray[ptr] = nums2[j]
          j += 1
      }
      ptr += 1
  }
  console.log(newArray)
  return newArray
}
