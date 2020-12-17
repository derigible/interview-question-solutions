# Given numbers n and k, divide n by k and return the quotient and remainder
# without using the divider (/) operator.

# Example:

# Input: 5, 2
# Output: [2, 1]

# Input: 4, 2
# Output: [2, 0]

def divide(n, k)
  top = n
  count = 0
  while top >= k
    top -= k
    count += 1
  end
  [count, top]
end

def check(input, expected)
  result = divide(*input)
  if result == expected
    puts "Correct: #{result} == #{expected}"
  else
    puts "FALSE!: #{result} != #{expected}"
  end
end

check [5, 2], [2, 1]
check [4, 2], [2, 0]
check [20, 11], [1, 9]
check [20, 11], [1, 10] # false case
