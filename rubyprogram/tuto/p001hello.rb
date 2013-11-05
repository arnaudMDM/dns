# p001hello.rb
puts 'hello'
=begin frefrfrf
fr
fr
fr =end
=end
=begin
puts 1 + 2
puts 1 * 2
puts 3 / 2
puts 10 - 11
puts 1.5 / 2.6
=end
@gt = @gt || 45
#print @gt

#if a = 2 && b = 3 then puts a, b end


def g *args # The splat here says accept 1 or more arguments, in the form of an Array  
  args      # This returns an array  
end  
  
def f arg  
  arg  
end  
  
x,y,z = [true, 'two', false] # parrallel assignment lets us do this  
  
if c = f(z) or a = f(x) and b = f(y) then  
  puts g(a,b,c) # An array is returned, and stored in variable d 
end  
  
#p d # using p to puts and inspect d  
