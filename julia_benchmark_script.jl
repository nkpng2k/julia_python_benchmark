f(x) = x^2 - 2

f_prime(x) = 2x

function recursive_roots()
  initial_conditions = -100:0.01:100
  roots = similar(initial_conditions)

  for (j, x_0) in enumerate(initial_conditions)
    x = x_0

    for i in 1:1000
      x = x - f(x) / f_prime(x)
    end

    roots[j] = x
  end

  initial_conditions, roots
end



function iterative_fibonacci(x)
  var1 = 0
  var2 = 1
  if x < 2
    return x
  end

  fib_num = BigInt(0)
  for i in 1:x-1
    fib_num =  var1 + var2
    var1 = var2
    var2 = fib_num
  end

return fib_num
end


funtion rec_fib(x)
  if x == 1
    return 1
  elseif x == 0
    return 0
  else
    return rec_fib(x-1) + rec_fib(x-2)
  end
end
