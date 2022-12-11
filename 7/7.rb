input = ''
File.open('input.txt', 'r') do |f|
  input = f.read
end

path = []
input.split("\n").each do |line|
  # puts line

  words = line.split(' ')

  if words[1] == 'cd'
    if words[2] == '..'
      path.pop
    else
      path << words[2]
    end

  elsif words[1] == 'ls'
    next
  elsif words[1] == 'dir'
    next
  else
    puts words.inspect
    next
    # puts path.join('/') + '/' + words[1]
  end
end
