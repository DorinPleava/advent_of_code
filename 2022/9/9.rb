input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

# create 1000x1000 grid
grid = Array.new(10) { Array.new(10, 0) }
head_position = { x: 4, y: 4 } # start at center
tail_position = { x: 4, y: 4 } # start at center
tail_visited_grid = Array.new(10) { Array.new(10, 0) }

tail_visited_grid[4][4] = 1

last_head_position = { x: 4, y: 4 }

def check_if_head_is_touching_tail(head_position, tail_position)

  puts "head_position: #{head_position}"
  puts "tail_position: #{tail_position}"
  if head_position[:x] == tail_position[:x] && head_position[:y] == tail_position[:y]
    puts 'tail overlaps head, do nothing'
    true
  elsif head_position[:x] == tail_position[:x] + 1 && head_position[:y] == tail_position[:y]
    puts 'head is touching to the right of tail'
    true
  elsif head_position[:x] == tail_position[:x] - 1 && head_position[:y] == tail_position[:y]
    puts 'head is touching to the left of tail'
    true
  elsif head_position[:x] == tail_position[:x] && head_position[:y] == tail_position[:y] + 1
    puts 'head is touching to the top of tail'
    true
  elsif head_position[:x] == tail_position[:x] && head_position[:y] == tail_position[:y] - 1
    puts 'head is touching to the bottom of tail'
    true
  elsif head_position[:x] == tail_position[:x] + 1 && head_position[:y] == tail_position[:y] + 1
    puts 'head is touching to tail diagonally top right'
    true
  elsif head_position[:x] == tail_position[:x] - 1 && head_position[:y] == tail_position[:y] - 1
    puts 'head is touching to tail diagonally bottom left'
    true
  elsif head_position[:x] == tail_position[:x] + 1 && head_position[:y] == tail_position[:y] - 1
    puts 'head is touching to tail diagonally bottom right'
    true
  elsif head_position[:x] == tail_position[:x] - 1 && head_position[:y] == tail_position[:y] + 1
    puts 'head is touching to tail diagonally top left'
    true
  end
  false
end

input.split("\n").each do |command_line|
  direction = command_line.split(' ')[0]
  times = command_line.split(' ')[1].to_i

  case direction
  when 'R'
    times.times do |_i|
      head_position[:x] += 1
      if check_if_head_is_touching_tail(head_position, tail_position)
        puts 'do nothing as head is touching taila'
      else
        puts "head is not touching tail, so move tail to #{last_head_position}"
        tail_visited_grid[last_head_position[:x]][last_head_position[:y]] = 1
        tail_position = { x: last_head_position[:x], y: last_head_position[:y] }
      end
      last_head_position = { x: head_position[:x], y: head_position[:y] }
    end
  when 'L'
    times.times do |_i|
      head_position[:x] -= 1
      if check_if_head_is_touching_tail(head_position, tail_position)
        puts 'do nothing as head is touching taila'
      else
        puts "head is not touching tail, so move tail to #{last_head_position}"
        tail_visited_grid[last_head_position[:x]][last_head_position[:y]] = 1
        tail_position = { x: last_head_position[:x], y: last_head_position[:y] }
      end
      last_head_position = { x: head_position[:x], y: head_position[:y] }
    end
  when 'U'
    times.times do |_i|
      head_position[:y] -= 1
      if check_if_head_is_touching_tail(head_position, tail_position)
        puts 'do nothing as head is touching taila'
      else
        puts "head is not touching tail, so move tail to #{last_head_position}"
        tail_visited_grid[last_head_position[:x]][last_head_position[:y]] = 1
        tail_position = { x: last_head_position[:x], y: last_head_position[:y] }
      end
      last_head_position = { x: head_position[:x], y: head_position[:y] }
    end
  when 'D'
    times.times do |_i|
      head_position[:y] += 1
      if check_if_head_is_touching_tail(head_position, tail_position)
        puts 'do nothing as head is touching taila'
      else
        puts "head is not touching tail, so move tail to #{last_head_position}"
        tail_visited_grid[last_head_position[:x]][last_head_position[:y]] = 1
        tail_position = { x: last_head_position[:x], y: last_head_position[:y] }
      end
      last_head_position = { x: head_position[:x], y: head_position[:y] }
    end
  end

  # # display visited grid
  # tail_visited_grid.each do |row|
  #   row.each do |cell|
  #     print cell
  #   end
  #   puts
  # end

  # count visited grid
  count = 0
  tail_visited_grid.each do |row|
    row.each do |cell|
      count += 1 if cell == 1
    end
  end
  puts "count is #{count}"

end
