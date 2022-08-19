my_dict = {}
def biggest_dict(**kwargs):
  my_dict.update(**kwargs)
  print(my_dict)

biggest_dict(first = 'first', length = 100)
biggest_dict(k1 = 44, k2 = 0, k3 = 10)
