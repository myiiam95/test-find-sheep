def find_sheep_and_wolves(numbers):
  # ผลรวมของหมายเลขบนเสื้อของหมาป่าทั้ง 2 ตัว
  wolf_sum = 20
  
  # หาเลขของหมาป่า
  wolf_numbers = []
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == wolf_sum:
        wolf_numbers.append(numbers[i])
        wolf_numbers.append(numbers[j])
        break
    if wolf_numbers:
      break
  
  # หาเลขของแกะ
  sheep_numbers = []
  for number in numbers:
    if number not in wolf_numbers:
      sheep_numbers.append(number)
      
  return sheep_numbers

# case 1
case1_input = [10, 13, 25, 30, 12, 18, 5, 7]
case1_output = find_sheep_and_wolves(case1_input)
print(f"Input dataset = {case1_input}")
print(f"Output result : {case1_output}")

print("-" * 20)

# case 2
case2_input = [9, 26, 1, 14, 11, 41, 6, 12]
case2_output = find_sheep_and_wolves(case2_input)
print(f"Input dataset = {case2_input}")
print(f"Output result : {case2_output}")