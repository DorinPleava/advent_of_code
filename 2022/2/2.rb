input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

# A for Rock, B for Paper, and C for Scissors
def add_points(opponent_choice, my_choice)
  scores = {
    'A' => 1,
    'B' => 2,
    'C' => 3,
    'X' => 1,
    'Y' => 2,
    'Z' => 3
  }

  if opponent_choice == my_choice
    scores[my_choice] + 3
    # return 'draw'
  elsif opponent_choice == 'A'
    if my_choice == 'B'
      scores[my_choice] + 6
      # return 'win'
    else
      scores[my_choice]
      # return 'lose'
    end
  elsif opponent_choice == 'B'
    if my_choice == 'C'
      scores[my_choice] + 6

      # return 'win'
    else
      scores[my_choice]

      # return 'lose'
    end
  elsif opponent_choice == 'C'
    if my_choice == 'A'
      scores[my_choice] + 6

      # return 'win'
    else
      scores[my_choice]

      # return 'lose'
    end
  end
end

total_score = 0

input.split("\n").each do |round|
  opponent_choice = round.split(' ')[0]

  my_choice = ''
  case round.split(' ')[1]
  when 'X'
    case opponent_choice
    when 'A'
      my_choice = 'C'
    when 'B'
      my_choice = 'A'
    when 'C'
      my_choice = 'B'
    end

  when 'Y'
    my_choice = opponent_choice
  when 'Z'
    case opponent_choice
    when 'A'
      my_choice = 'B'
    when 'B'
      my_choice = 'C'
    when 'C'
      my_choice = 'A'
    end
  end

  # if my_choice == 'X'
  #   my_choice = 'A'
  # elsif my_choice == 'Y'
  #   my_choice = 'B'
  # elsif my_choice == 'Z'
  #   my_choice = 'C'
  # end

  total_score += add_points(opponent_choice, my_choice)

  # total_score += scores[my_choice]

  # check who won
  puts total_score
end
