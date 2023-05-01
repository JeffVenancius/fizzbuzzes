def divisable_form(): # for comparison
    print('fizzbuzz with division')
    for i in range(1,101):
        output = ""
        if not i % 3: # since false is 0
            output += "fizz"
        if not i % 5:
            output += "buzz"
        if not output:
            output = i
        print(output)

def no_division_form():
    print('fizzbuzz "without" division')
    fizz_counter = 0
    buzz_counter = 0
    for i in range(1,101):
        output = ""
        fizz_counter += 1
        buzz_counter += 1
        if fizz_counter == 3:
            output += "fizz"
            fizz_counter = 0
        if buzz_counter == 5:
            output += "buzz"
            buzz_counter = 0
        if not output: 
            output = i
        print(output)

divisable_form()
no_division_form()
