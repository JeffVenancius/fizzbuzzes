def divisable_form(): # for comparison
    print('fizzbuzz with division')
    print(0)
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
    print(0)
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

def lookup_form():
    print('lookup fizzbuzz')
    print(0)
    for i in range(1,101):
        output = ""
        last_digit = str(i)[-1]
        if not i % 3:
            output += "fizz"
        if last_digit == '5' or last_digit == '0':
            output += "buzz"
        if not output:
            output = str(i)

        print(output)


# divisable_form()
# no_division_form()
lookup_form()
