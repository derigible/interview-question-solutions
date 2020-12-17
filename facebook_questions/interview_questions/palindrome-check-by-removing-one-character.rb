# Given a string, check if that string can become a palindrome if
# a single character is removed from that string. Return true if so, false otherwise.

# Example:

# Input: 'tacocats'
# Output: true

# Input: 'tacoscats'
# Output: false

# Input: 'tacocat'
# Output: false

def become_palindrome?(input)
  left = 0
  right = input.size - 1
  removed = 0
  while left < right && removed < 2
    if input[left] == input[right]
      left += 1
      right -= 1
    elsif input[left + 1] == input[right]
      left += 2
      right -= 1
      removed += 1
    elsif input[left] == input[right - 1]
      left += 1
      right -= 2
      removed += 1
    else
      return false
    end
  end
  removed == 1
end

def check(input)
  if become_palindrome? input
    puts "Correct: #{input}"
  else
    puts "FALSE!: #{input}"
  end
end

check 'tacocats'
check 'tacoscats'
check 'tacocat'
check ''
check 'a'
check 'aa'
check 'abca'
check 'abcda'
check 'right'
