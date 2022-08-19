def to_dict(input_list):
  return {item: item for item in input_list}

y = 'y'
while y == 'y':
  input_list = input('enter list of elements, using comma: ').split(',')
  print(to_dict(input_list))
  y = input('restart?(y/n): ')
print('goodbye')
