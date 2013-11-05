o = Object.new
def o.foo
  puts 42
end

#o.dup.foo   # raises NoMethodError
o.clone.foo # returns 42

class Foo
  attr_accessor :bar
end
o = Foo.new
o.freeze

o.dup.bar = 10   # succeeds
#o.clone.bar = 10 # raises RuntimeError