# You are given a set of students represented by a tuple of (relative_height, # of students taller than student ahead in line)
# In other words, the first value of the tuple represents the relative height
# of the student in the class with 1 being the shortest, and the second value
# is the number of other students ahead of the given student that are taller
# than them. Each student only knows how many students are taller.

# Given this set, reconstruct the original line order and return the order in an array with
# the first element being the front of the line.

# Example:

# Input: Set({(4,1), (3,0), (5,0), (2,3), (1,3)})
# Output: This pretty much will give away the algorithm, but below is an example:

# [3, 5, 4, 1, 2]

# this solution is n^2 runtime. :(

require 'set'

def swap(arr, idx_a, idx_b)
  arr[idx_a], arr[idx_b] = arr[idx_b], arr[idx_a]
end

def reconstruct_line_order(children)
  ordered_set = children.to_a.sort_by { |c| c.first }.reverse!

  (0..ordered_set.size - 1).each do |i|
    child = ordered_set[i]
    # impossible to say more in front than its ordered height index
    return -1 if child[1] > i

    current_index = i
    while child[1] != current_index
      swap(ordered_set, current_index, current_index - 1)
      current_index -= 1
    end
  end
  ordered_set.map { |c| c.first }
end

def check(input, expected)
  out = reconstruct_line_order(input)
  if out == expected
    puts "Correct: #{out} == #{expected}"
  else
    puts "FALSE!: #{out} != #{expected}"
  end
end

check Set.new([[4, 1], [3, 0], [5, 0], [2, 3], [1, 3]]), [3, 5, 4, 1, 2]
check Set.new([[4, 0], [3, 0], [5, 0], [2, 0], [1, 0]]), [1, 2, 3, 4, 5]
check Set.new([[4, 0], [3, 0], [5, 1], [2, 0], [1, 0]]), -1

def reconstruct_line_order_2(input)
  ordered_set = input.to_a.sort_by { |c| c.first }.sort! { |a, b| a[1] > b[1] ? -1 : 1 }

  ordered_set.each_with_object([]) do |c, out|
    puts c if c.first.nil?
    out.insert c[1], c.first
  end.compact
end

def check2(input, expected)
  out = reconstruct_line_order_2(input)
  if out == expected
    puts "Correct: #{out} == #{expected}"
  else
    puts "FALSE!: #{out} != #{expected}"
  end
end

check2 Set.new([[4, 1], [3, 0], [5, 0], [2, 3], [1, 3]]), [3, 5, 4, 1, 2]
check2 Set.new([[4, 0], [3, 0], [5, 0], [2, 0], [1, 0]]), [1, 2, 3, 4, 5]
