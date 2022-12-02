module InputFileReader
  def readInput(filename = 'input.txt')
    File.open(filename, 'r') do |f|
      f.read
    end
  end
end
