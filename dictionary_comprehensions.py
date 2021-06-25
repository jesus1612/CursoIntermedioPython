def main():
  # Reto
  naturals_nums = {i: i ** 3 for i in range(1, 101) if(i % 3 != 0)}

  reto_nums = {i: round(i ** 0.5, 2) for i in range(1, 1001)}
  print(reto_nums)
if __name__ == '__main__':
  main()