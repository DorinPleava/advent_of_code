# frozen_string_literal: true

input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

crates = input.split("\n\n")[0].split("\n")

crates_nr = crates.pop.split(' ').map(&:to_i)

puts crates.split(' ').map(

