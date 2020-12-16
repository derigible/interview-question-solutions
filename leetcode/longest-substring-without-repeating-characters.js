// Given a string s, find the length of the longest substring without repeating characters.



// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.

// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.

// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// Example 4:

// Input: s = ""
// Output: 0



// Constraints:

//     0 <= s.length <= 5 * 104
//     s consists of English letters, digits, symbols and spaces.

function removeCharsUntilUniqueSet(charSet, s, c, start) {
  let i = start
  while(charSet.has(c)){
      charSet.delete(s[i])
      i += 1
  }
  return i
}

/**
* @param {string} s
* @return {number}
*/
var lengthOfLongestSubstring = function(s) {
  let max = 0
  let currStart = 0
  const charSet = new Set()
  for(let i = 0; i < s.length; i++) {
      const c = s[i]
      if (charSet.has(c)) {
          currStart = removeCharsUntilUniqueSet(charSet, s, c, currStart)
      }  else if(i - currStart + 1 > max) {
          max = i - currStart + 1
      }
      charSet.add(c)
  }
  return max
};
