x = (0..99).to_a.sort_by{rand}.join
i = 0
no = false
hash = {}
stack = []
(0..99).each {|i| hash[i] = false}
while i < x.length
  if i < (x.length - 1) and x[i] != 0 and hash[(x[i] + x[i + 1]).to_i] == false and hash[(x[i] + x[i + 1]).to_i] = true and stack << (x[i] + x[i + 1])
    i += 2
  else
    res = false
  end	
  while res == false
    if no == false && hash[x[i].to_i] == false and hash[x[i].to_i] = true and stack << x[i] and res = true
      i += 1 
    else
      val = stack.pop()
	  hash[val.to_i] = false
	  i -= val.length
	  val.length == 1 ? no = true : no = false
    end
  end
end
puts stack.sort_by(&:to_i)