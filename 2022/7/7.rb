input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

size_dict = {}

path = []
input.split("\n").each do |line|
  # puts line

  words = line.split(' ')

  if words[1] == 'cd'
    if words[2] == '..'
      path.pop
    elsif words[2] == '/'
      path = []
    else
      path << words[2]
    end

  elsif words[1] == 'ls'
    next
  elsif words[0] == 'dir'
    next
  else
    size = words[0].to_i

    puts "in else #{words.inspect}}"
    puts "path: #{path.inspect}"

    path.each do |p|
      puts "p: #{p}"
      size_dict[p] = size_dict[p].to_i + size
    end
  end
end

sum_of_dict_under_100000 = 0

size_dict.each do |_k, v|
  sum_of_dict_under_100000 += v if v < 100_000

  # puts "#{k} #{v}"
end

puts size_dict.inspect
puts sum_of_dict_under_100000
