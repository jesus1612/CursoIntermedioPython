def main():
  my_list = [1, "Hello", True, 4.5]
  my_dict = {"firstName": "facundo", "lastName": "García"}

  super_list = [
    {"first_name": "facundo", "last_name": "García"},
    {"first_name": "Miguel", "last_name": "Torres"},
    {"first_name": "Pepe", "last_name": "Roledo"},
    {"first_name": "Susana", "last_name": "Martínez"},
    {"first_name": "José", "last_name": "García"}
  ]

  super_dict = {
    "natural_nums": [1, 2, 3, 4, 5],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 4.5, 6.43]
  }

  for key, value in super_dict.items():
    print(key, "-", value)

if __name__ == '__main__':
  main()