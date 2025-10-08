# print(f"i like piza")
# txt_data = "I love coding"
# employees =[ "Pius ","mike","jeff"] 

# file_path ="output.txt"

# with open(file=file_path, mode="w") as file:
#     for employee in employees:
#         file.write(employee +"\n")
#     print(f"txt file '{file_path} was created")


txt = "I will be going to  hospital"

file_path = "gb.txt"

with open(file_path,"w") as file:
    file.write(txt)
    print(f"the txt file '{file_path}' has been created")
