input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

grid = []

# create grid from input
input.split("\n").each_with_index do |row, row_index|
  row.chars.each do |column|
    grid[row_index] = [] if grid[row_index].nil?
    grid[row_index] << column
  end
end

# created grid
puts grid.inspect

def check_if_visible_up(grid, row, column, value_to_check, visible_trees = 0)
  if row.zero?
    if grid[row][column] == value_to_check
      return { visible: false, visible_trees: visible_trees + 1 }
    elsif grid[row][column] >= value_to_check
      { visible: false, visible_trees: visible_trees }
    else
      return { visible: true, visible_trees: visible_trees }
    end
  end

  if grid[row - 1][column] == value_to_check
    { visible: false, visible_trees: visible_trees + 1 }
  elsif grid[row - 1][column] >= value_to_check
    { visible: false, visible_trees: visible_trees }
  else
    check_if_visible_up(grid, row - 1, column, value_to_check, visible_trees + 1)
  end
end

def check_if_visible_down(grid, row, column, value_to_check, visible_trees = 0)
  if row == grid.length - 1
    if grid[row][column] == value_to_check
      return { visible: false, visible_trees: visible_trees + 1 }
    elsif grid[row][column] >= value_to_check
      { visible: false, visible_trees: visible_trees }
    else
      return { visible: true, visible_trees: visible_trees }
    end
  end

  if grid[row + 1][column] == value_to_check
    { visible: false, visible_trees: visible_trees + 1 }
  elsif grid[row + 1][column] >= value_to_check
    { visible: false, visible_trees: visible_trees }
  else
    check_if_visible_down(grid, row + 1, column, value_to_check, visible_trees + 1)
  end
end

def check_if_visible_left(grid, row, column, value_to_check, visible_trees = 0)
  if column.zero?
    if grid[row][column] == value_to_check
      return { visible: false, visible_trees: visible_trees + 1 }
    elsif grid[row][column] >= value_to_check
      { visible: false, visible_trees: visible_trees }
    else
      return { visible: true, visible_trees: visible_trees }
    end
  end

  if grid[row][column - 1] == value_to_check
    { visible: false, visible_trees: visible_trees + 1 }
  elsif grid[row][column - 1] >= value_to_check
    { visible: false, visible_trees: visible_trees }
  else
    check_if_visible_left(grid, row, column - 1, value_to_check, visible_trees + 1)
  end
end

def check_if_visible_right(grid, row, column, value_to_check, visible_trees = 0)
  if column == grid[row].length - 1
    if grid[row][column] == value_to_check
      return { visible: false, visible_trees: visible_trees + 1 }
    elsif grid[row][column] >= value_to_check
      { visible: false, visible_trees: visible_trees }
    else
      return { visible: true, visible_trees: visible_trees }
    end
  end

  if grid[row][column + 1] == value_to_check
    { visible: false, visible_trees: visible_trees + 1 }
  elsif grid[row][column + 1] >= value_to_check
    { visible: false, visible_trees: visible_trees }
  else
    check_if_visible_right(grid, row, column + 1, value_to_check, visible_trees + 1)
  end
end

max_visible = 0
scenic_score = 0

max_scenic_score = 0

grid.each_with_index do |row, row_index|
  row.each_with_index do |column, col_index|
    # ignore edges of the grid
    next if row_index.zero? || row_index == grid.length - 1
    next if col_index.zero? || col_index == row.length - 1

    max_visible += 1 if check_if_visible_up(grid, row_index, col_index, column)[:visible] ||
                        check_if_visible_down(grid, row_index, col_index, column)[:visible] ||
                        check_if_visible_left(grid, row_index, col_index, column)[:visible] ||
                        check_if_visible_right(grid, row_index, col_index, column)[:visible]

    puts "---row: #{row_index}, col: #{col_index}"
    puts "scenic score up: #{check_if_visible_up(grid, row_index, col_index, column)[:visible_trees]}"
    puts "scenic score down: #{check_if_visible_down(grid, row_index, col_index, column)[:visible_trees]}"
    puts "scenic score left: #{check_if_visible_left(grid, row_index, col_index, column)[:visible_trees]}"
    puts "scenic score right: #{check_if_visible_right(grid, row_index, col_index, column)[:visible_trees]}"
    # calculate scenic score
    scenic_score = check_if_visible_up(grid, row_index, col_index, column)[:visible_trees] *
                   check_if_visible_down(grid, row_index, col_index, column)[:visible_trees] *
                   check_if_visible_left(grid, row_index, col_index, column)[:visible_trees] *
                   check_if_visible_right(grid, row_index, col_index, column)[:visible_trees]

    max_scenic_score = scenic_score if scenic_score > max_scenic_score
  end
end

puts "max scenic score: #{max_scenic_score}"
puts "max visible: #{max_visible}"
puts max_visible + grid.length * 2 + grid[0].length * 2 - 4 # -4 for the corners
