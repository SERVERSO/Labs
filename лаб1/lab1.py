a = int(input("Введите число: "))
print(*range(1, a + 1), sep = "\n")


arr = set((int(input(f"Введите число {_}: "))) for _ in range(1,3))
print("Большее число: ", max(arr))
