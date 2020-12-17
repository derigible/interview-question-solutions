# Given a text (such as a book, user input, etc.), find the top n
# words of the text.
#
# Example:
#
# Input: "The quick brown fox ran quick to the brown thickets over by the brook.", n = 3
# Output: ["the", "quick", "brown"]
#
# Note that words which are a tie can come in any order and if there are more words
# that are a tie than what is asked for then any of those words are valid outputs.

# Definition of a word is a string of characters surrounded by spaces. Punctuation
# at the end of the word does not make a new word.

# For example, "end" and "end." are the same word; "end-time" and "end-time" are the same
# word; "endzone" and "endzone.\n" are the same. Note that '' is not considered a word.

# "end\nzone" will be two words - "end" and "zone"

# "end1" is considered a word. "@gmail.com" is considered one word.

# capitalization does not matter - "one" and "One" are the same word.

# if n is greater than the number of unique words, return all words - ie "the and only", n = 4 will
# return ["the", "and", "only"]

def normalize_word(word)
  new_word = word.downcase
  new_word[new_word.size - 1] =~ /[\w\d]/ ? new_word : new_word.slice(0, new_word.size - 1)
end

def top_n_words(input, n)
  word_map = {}
  words = input.split
  words.each do |w|
    normalized = normalize_word(w)
    if normalized.size.positive?
      word_map.key?(normalized) ? word_map[normalized] += 1 : word_map[normalized] = 1
    end
  end

  count_map = {}
  word_map.each do |word, count|
    count_map.key?(count) ? count_map[count] << word : count_map[count] = [word]
  end

  count = 0
  sorted_counts = count_map.keys.sort.reverse
  out = []
  sorted_counts.each do |c|
    count_map[c].each do |word|
      return out if count == n

      out << word
      count += 1
    end
  end
  out
end

def check(input, n, expected)
  out = top_n_words(input, n)
  if out == expected
    puts "Correct: #{out} == #{expected}"
  else
    puts "FALSE!: #{out} != #{expected}"
  end
end

check('The quick brown fox ran quick to the brown thickets over by the brook.', 3, %w[the quick brown])
check('the and only', 4, %w[the and only])
check('the and only is. is a start', 4, %w[is the and only])
check('the and only1 is. is a start only', 4, %w[is the and only1])
check("the end\nzone is the endzone is", 2, %w[the is])
check('One one two TwO three three three', 3, %w[three one two])
check('@gmail.com derigible@gmail.com @outlook.com @outlook.com1 derigible@gmail.com. derigible@gmail.com,', 3, %w[derigible@gmail.com @gmail.com @outlook.com])
