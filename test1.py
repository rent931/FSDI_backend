

def print_name():
    print("Miguel Renteria")




def list1():
    print("Working with list (arrays)")

    names = ['John', 'Juan']

    names.append("Carlos")
    names.append("Charles")


    # get the values
    print(names[0])
    print(names[3])

    print(names)


    print_name()

    #for loop
    for name in names:
        print(name)



def list2():
    print("-" * 30)

    nums = [123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]

    # 1 - print the sum of all numbers
    total = 0
    for n in nums:
        total += n

    print (total)


    #2a- print numbers lower than 50 
    #2b- count how many numbers are lower than 50 

    count = 0
    for num in nums:
        if(num < 50):
            print(num)
            count += 1


    print(f"there are: {count} nums lower than 50")

    # 3 - find the smallest number in the list 
    # variable that start with any number in the list (first)
    #compare if the num is ower than the smallest number 
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num 





    print(f"The smallest in the list is: {smallest}")







def dict1():
    print("Dictionary Test 1 ---------------------------")


    me = {
        "name": "Miguel",
        "last": "Renteria",
        "age": 28,
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 118,
            "city": "Springfield"
        }
    }

    print(me["name"])
    print(me["name"] + " " + me["last"])


    me["age"] = 99

    me["email"] = "miguel2@sdgku.edu"

    print( me )



    #print the full address in a single line 
    address = me["address"]
    print(f"{address['number']} {address['street']} {address['city']}")



print_name()
list1()
list2()

dict1()
