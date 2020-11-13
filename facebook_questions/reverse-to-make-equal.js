/*
Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.
*/
// Add any extra import statements you may need here


// Add any helper functions you may need here


function areTheyEqual(array_a, array_b){
  if(array_a.length != array_b.length) {
    return false
  }
  const mapOfValuesA = {}
  const mapOfValuesB = {}
  array_a.forEach(x => {
    if(mapOfValuesA.hasOwnProperty(x)) {
      mapOfValuesA[x] += 1
    } else {
      mapOfValuesA[x] = 1
    }
  })
  array_b.forEach(x => {
    if(mapOfValuesB.hasOwnProperty(x)) {
      mapOfValuesB[x] += 1
    } else {
      mapOfValuesB[x] = 1
    }
  })
  for(let k of Object.keys(mapOfValuesA)) {
    if(!mapOfValuesB.hasOwnProperty(k) || mapOfValuesB[k] != mapOfValuesA[k]) {
      return false
    }
  }
  return true
}











// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!
function printString(str) {
  var out = '["' + str + '"]';
  return out;
}

var test_case_number = 1;

function check(expected, output) {
  var result = (expected == output);
  var rightTick = "\u2713";
	var wrongTick = "\u2717";
  if (result) {
  	var out = rightTick + ' Test #' + test_case_number;
  	console.log(out);
  }
  else {
  	var out = '';
  	out += wrongTick + ' Test #' + test_case_number + ': Expected ';
  	out += printString(expected);
  	out += ' Your output: ';
  	out += printString(output);
  	console.log(out);
  }
  test_case_number++;
}

var array_a_1 = [1, 2, 3, 4];
var array_b_1 = [1, 4, 3, 2];
var expected_1 = true;
var output_1 = areTheyEqual(array_a_1, array_b_1);
check(expected_1, output_1);

var array_a_2 = [1, 2, 3, 4];
var array_b_2 = [1, 4, 3, 3];
var expected_2 = false;
var output_2 = areTheyEqual(array_a_2, array_b_2);
check(expected_2, output_2);

// Add your own test cases here
var array_a_3 = [1, 2, 3, 4];
var array_b_3 = [1, 4, 3];
var expected_3 = false;
var output_3 = areTheyEqual(array_a_3, array_b_3);
check(expected_3, output_3);
