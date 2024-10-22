user = input("what array do you want to display single dimension array? or two dimension array: ").lower()

list = ["Carlos", "Mosqueda", "Garay"]
lists = [
    ["Legaspi", "Jang", "Sagaad"],
    [1,2,3,4,5,6,7,8,9,10]
]

def listname():
    for room in list:
        print(list)
       

def listsname():
    for rock in lists:
        for rocks in rock:
            print(lists)

def choice():
    if user == "single dimension array":
        return list
    elif user == "two dimension array":
        return lists
    else:
        return "error"

result = choice()
print(result)