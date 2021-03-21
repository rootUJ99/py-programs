def largest_prime_factor(number)
  i = 2
  while number > 1
    if number % i == 0
      number /= i;
    else
      i += 1
    end
  end
  return i
end
print largest_prime_factor(6008514999999)
