# Завдання 1
# def get_day_name(day_number):
#     days = {
#         1: "понеділок",
#         2: "вівторок",
#         3: "середа",
#         4: "четвер",
#         5: "п'ятниця",
#         6: "субота",
#         7: "неділя"
#     }
#
#     try:
#         day_number = int(day_number)
#         return days[day_number]
#     except (ValueError, KeyError):
#         raise ValueError("Некоректний номер дня тижня")
#
# # Зчитування введеного номера дня тижня від користувача
# user_input = input("Введіть номер дня тижня (1-7): ")
#
# # Виведення результату
# try:
#     result = get_day_name(user_input)
#     print(result)
# except ValueError as e:
#     print(f"Помилка: {e}")


#завдвння 2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if num1 == num2:
#         print("OK!Числа рівні")
#     else:
#         print(f"Числа не рівні. У порядку зростання: {min(num1, num2)}, {max(num1, num2)}")
# except ValueError as e:
#     print(f"Error: {e}")

#завдання 3
# def perform_operation(number1, number2, operator):
#     try:
#         number1 = float(number1)
#         number2 = float(number2)
#
#         if operator == '+':
#             result = number1 + number2
#         elif operator == '-':
#             result = number1 - number2
#         elif operator == '*':
#             result = number1 * number2
#         elif operator == '/':
#             # Обробка ділення на нуль
#             if number2 == 0:
#                 raise ValueError("Ділення на нуль неможливе.")
#             result = number1 / number2
#         else:
#             raise ValueError("Введено невірну математичну дію.")
#
#         return f"Результат: {result}"
#     except ValueError as e:
#         return f"Помилка: {e}"
#
# # Зчитування введених користувачем чисел та математичної дії
# user_input1 = input("Введіть перше число: ")
# user_input2 = input("Введіть друге число: ")
# user_operator = input("Введіть математичну дію (+, -, *, /): ")
#
# # Виведення результату
# result = perform_operation(user_input1, user_input2, user_operator)
# print(result)



