# Minimize the number of transactions by compressing
# the transfers between banks using a central bank
# to ensure the transfers
def central_bank_algorithm(input)
  bank_map = {}
  input.each do |b|
    out_bank = b[0]
    in_bank = b[1]
    payment = b[2..b.length].to_i
    unless bank_map.key? out_bank
      bank_map[out_bank] = 0
    end
    unless bank_map.key? in_bank
      bank_map[in_bank] = 0
    end
    bank_map[out_bank] -= payment
    bank_map[in_bank] += payment
  end

  # bank = bank_map.find {bankwith highest}

  out = bank_map.keys.map do |k|
    next if k == 'A' || bank_map[k] == 0
    if bank_map[k].negative?
      "#{k}A#{bank_map[k].abs}"
    else
      "A#{k}#{bank_map[k].abs}"
    end
  end.compact

end


def test(input, expected)
  output = central_bank_algorithm(input)
  if output == expected
    puts 'correct'
  else
    puts 'incorrect!!!'
    puts "Expected #{expected} got #{output}"
  end
end


# test(%w(AB1 BA2 BC1), %w(BA2 AC1))

# test(%w(AB1 BA2 BC1 AC2), %w(BA2 AC3))

# test(%w(AB1 BA2 BC1 AB2), %w(AC1))

# test(%w(AB11 BA2), %w(AB9))

# test(%w(AB1 BC1 CA1), %w())

test(%w(BC1), %w())
test(%w(DE1 ED1 BC1 GF1), %w(BA1 AC1 GA1 AF1))
