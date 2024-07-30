# Declare a dictionary
# my_map = {}

# sizee = int(input("len of the array > "))
# for i in range(sizee):
#     my_map[i] = input("give me the attribute : ").split()

# for j in range(sizee):
#     for k in range (2):
#         if k == 0:
#             print("attribute:\t" + my_map[j][k] + " | ",end="")
#         else:
#             print("type:\t" + my_map[j][k] + " ",end="")
#     print("")
# print(my_map[0][0])

# input_string = "Hello, World!"

# # Check if the string has at least two characters
# if len(input_string) >= 2:
#     string_without_last_two = input_string[:-2]
#     print("String without last two characters:", string_without_last_two)
# else:
#     print("String is too short to remove the last two characters.")


# def checked(stt):
#     wiwi = stt.find()
#     print("132")
#     i = 0
#     if stt[wiwi] == "[" and stt[:-1] == "]":
#         print("howaaaaaa")
#     else:
#         print("nooooooooo")




# input_string = "age[111111111111515511515321322323123....]"
# checked(input_string)

# def checked(stt):
#     opening_bracket_index = stt.find("[")
#     closing_bracket_index = stt.find("]")
#     res = ""
#     if opening_bracket_index != -1 and closing_bracket_index != -1 and opening_bracket_index < closing_bracket_index:
#         if len(stt[:opening_bracket_index]) != 0:
#             print("Pattern is matched")
#             res = stt[opening_bracket_index + 1:closing_bracket_index]
#             sssy = stt[:opening_bracket_index]
#             print (res)
#             print (sssy)
#         else:
#             print("Pattern is not matched")
#     else:
#         print("Pattern is not matched")

# input_string = "age[111111111111515511515321322323123....]"
# checked(input_string)


# Find the position of the opening square bracket '['
# opening_bracket_index = input_string.find('[')
# print(input_string.find('['))

# # Extract the part of the string before the opening square bracket
# if opening_bracket_index != -1:
#     extracted_part = input_string[:opening_bracket_index]
#     extracted_partw = input_string[opening_bracket_index:]
#     print(extracted_part)
#     print(extracted_partw)
# else:
#     print("Opening square bracket not found in the input string.")
    
    
    
    
# param = input("nbr of attribute : ")
# param = param.strip()
# param = ' '.join(param.split())
# if (param.isalpha() == False):
#     print("noooo")
# else:
#     print("good")
    
# if len(param.split()) == 1:
#     print(Green + "ok" + Color_Off)
#     break
# else :
#     print(BRed + "Retry " + Color_Off)
#     continue


try:
    user_input = input("Enter an integer: ")
    user_input = int(user_input)
    user_input = user_input.strip()
    user_input = ' '.join(user_input.split())
    print(f"You entered a valid integer: {user_input}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
