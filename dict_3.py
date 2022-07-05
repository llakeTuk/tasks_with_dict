def count_it(str_numbers):
  num_count = {int(elem): str_numbers.count(elem) for elem in str_numbers}
  sorted_num_count = sorted(num_count.items(), key = lambda element: element[1])
  return dict(sorted_num_count[-3:])
y = 'y'
while y == 'y':
  input_str = input('enter string of numbers: ')
  print(count_it(input_str))
  y = input('restart?(y/n): ')
print('goodbye')