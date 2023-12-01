require './priorityQueue.rb'
input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

# puts input

queue = PriorityQueue.new()

max_calories = 0

input.split("\n\n").each do |elf_calories|
  total_calories = 0
  elf_calories.split("\n").each do |calories|
    total_calories += calories.to_i
  end

  queue << total_calories

  if total_calories > max_calories
    max_calories = total_calories
  end
end

# puts "---------------------"
# puts "Max calories: #{queue.pop}"

three_elfes_sum = 0
3.times do
  three_elfes_sum += queue.pop
end

puts "---------------------"
puts "Top 3 elfs with calories summed up: #{three_elfes_sum}"
