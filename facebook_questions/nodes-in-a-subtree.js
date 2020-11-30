// Much better implementation found at - https://leetcode.com/discuss/interview-question/756125/facebook-recruiting-portal-nodes-in-a-subtree

// Added it here for reference:

// I think it takes O(n*m) if we loop thru n elements in queries and traverse the tree of size m for each query. A O(n+m) solution is possible if we use data structure to help.
// basic idea:

// use Map to store the count of each character under one node
// a node's Map is the consolidated result of all its children + itself
// once the Map is built, go thru queries and do lookup in the map
// here is my code:

//   private Map<Character, Integer> dfs(Node node, String s, Map<Integer, Map<Character, Integer>> countMap) {
//     Map<Character, Integer> charCountMap = new HashMap<>();
//     charCountMap.put(s.charAt(node.val - 1), 1);

//     for (Node child : node.children) {
//       for (Map.Entry<Character, Integer> entry : dfs(child, s, countMap).entrySet()) {
//         charCountMap.put(entry.getKey(), charCountMap.getOrDefault(entry.getKey(), 0) + entry.getValue());
//       }
//     }

//     countMap.put(node.val, charCountMap);
//     return charCountMap;
//   }

//   int[] countOfNodes(Node root, ArrayList<Query> queries, String s) {
//     int[] result = new int[queries.size()];

//     Map<Integer, Map<Character, Integer>> countMap = new HashMap<>();
//     dfs(root, s, countMap);

//     int index = 0;
//     for (Query q : queries) {
//       result[index++] = countMap.get(q.u).getOrDefault(q.c, 0);
//     }

//     return result;
//   }

// Definition for a Node
function Node(val, children) {
  this.val = val === undefined ? 0 : val;
  this.children = children === undefined ? [] : children;
};

function getIndexesFromTreeTraversal(subRoot) {
  const stack = [subRoot]
  const indxs = []
  while(stack.length > 0){
    const n = stack.pop()
    n.children && n.children.forEach(c => stack.push(c))
    indxs.push(n.val)
  }
  return indxs
}

function mapNodes(root, arraySize) {
  const nodeMap = new Array(arraySize)
  const stack = [root]
  while(stack.length > 0) {
    const node = stack.pop()
    node.children && node.children.forEach(c => stack.push(c))
    nodeMap[node.val - 1] = getIndexesFromTreeTraversal(node)
  }
  return nodeMap
}

function getCharCount(indxs, char, string) {
  let count = 0
  indxs.forEach(i => {
    if(string[i-1] == char){
      count += 1
    }
  })
  return count
}

function countOfNodes(root, queries, string) {
  // create mapping of nodes for constant time lookup
  // loop through queries
  // go to each position in string to compare against query
  // increment the count of that character
  // once all counted, put into the results
  // return results
  const results = []
  const nodeMap = mapNodes(root, string.length)
  queries.forEach(q => {
    // validate query here
    const idxs = nodeMap[q[0] - 1]
    results.push(getCharCount(idxs, q[1], string))
  })
  return results
}

// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!
function printintegerArray(array) {
  var size = array.length;
  var res = '';
  res += '[';
  var i = 0;
  for (i = 0; i < size; i++) {
    if (i !== 0) {
      res += ', ';
    }
    res += array[i];
  }
  res += ']';
  return res;
}

var test_case_number = 1;

function check(expected, output) {
  var expected_size = expected.length;
  var output_size = output.length;
  var result = true;
  if (expected_size != output_size) {
    result = false;
  }
  for (var i = 0; i < Math.min(expected_size, output_size); i++) {
    result &= (output[i] == expected[i]);
  }
  var rightTick = "\u2713";
  var wrongTick = "\u2717";
  if (result) {
    var out = rightTick + ' Test #' + test_case_number;
    console.log(out);
  }
  else {
    var out = '';
    out += wrongTick + ' Test #' + test_case_number + ': Expected ';
    out += printintegerArray(expected);
    out += ' Your output: ';
    out += printintegerArray(output);
    console.log(out);
  }
  test_case_number++;
}

// Testcase 1
var n_1 = 3, q_1 = 1;
var s_1 = "aba";
var node_1 = new Array(n_1 + 1);
for (var i = 1; i <= n_1; i++) {
  node_1[i] = new Node(i);
}
var root1 = node_1[1];
node_1[1].children = [node_1[2], node_1[3]];
var queries_1 = [[1, 'a']];
var output_1 = countOfNodes(root1, queries_1, s_1);
var expected_1 = [2];
check(expected_1, output_1);

// Testcase 2
var n_2 = 7, q_2 = 3;
var s_2 = "abaacab";
var node_2 = new Array(n_2 + 1);
for (var i = 1; i <= n_2; i++) {
  node_2[i] = new Node(i);
}
var root2 = node_2[1];
node_2[1].children = [node_2[2], node_2[3], node_2[7]];
node_2[2].children = [node_2[4], node_2[5]];
node_2[3].children = [node_2[6]];
var queries_2 = [[1, 'a'], [2, 'b'], [3, 'a']];
var output_2 = countOfNodes(root2, queries_2, s_2);
var expected_2 = [4, 1, 2];
check(expected_2, output_2);

// Add your own test cases here
