input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

priority_values_lower = ('a'..'z').to_a.each.with_index(1).map { |v, index| [v, index] }.to_h
priority_values_upper = ('A'..'Z').to_a.each.with_index(27).map { |v, index| [v, index] }.to_h

priority_values = priority_values_lower.merge(priority_values_upper)

total_sum = 0

# party 1

# input.split("\n").each do |rucksack|
#   first_part = rucksack[0...rucksack.length / 2]
#   second_part = rucksack[rucksack.length / 2..]

#   puts first_part
#   puts second_part

#   first_part.chars.each do |c|

#     if second_part.include?(c)
#       puts "Found #{c} with value #{priority_values[c]}"
#       total_sum += priority_values[c]
#       break
#     end
#   end

#   puts total_sum

# Part 2

input.split("\n").each_slice(3).each do |three_ruchsack_group|
  three_ruchsack_group[0].chars.select do |c|
    next unless three_ruchsack_group[1].include?(c) && three_ruchsack_group[2].include?(c)

    puts "Found #{c} with value #{priority_values[c]}"
    total_sum += priority_values[c]
    break
  end

  puts total_sum
end

# end
