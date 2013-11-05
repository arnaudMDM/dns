# p039xsymbol.rb  
class Test  
  puts :Test.object_id.to_s  
  def test  
    puts :test.object_id.to_s  
    @test = 10  
    puts :test.object_id.to_s  
  end  
end  
t = Test.new  
t.test  

puts

know_ruby = :yes  
if know_ruby == :yes  
  puts 'You are a Rubyist'  
else  
  puts 'Start learning Ruby'  
end  

puts

puts "string".to_sym.class # Symbol  
puts :symbol.to_s.class    # String  