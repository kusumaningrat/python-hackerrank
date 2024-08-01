import time

the_answer = 8
guessed_number = []

max_attempts = 3

numbers = [i for i in range(1,11)]

mid_number = len(numbers) // 2

while True:
    input_guessing = int(input("Enter your guess: "))
    guessed_number.append(input_guessing)

    if input_guessing < the_answer:
        print("Too low")
    elif input_guessing > the_answer:
        print("Too high")
    else:
        input_guessing = mid_number
        print("You guess it!!")
        break

    max_attempts -= 1
    print(f"You have {max_attempts} attempts left") 
    
    if max_attempts < 1:
        print("Timeout!!")
        break
    

# Another one

thousands_numbers = [x for x in range(100)]

the_answer = 86
low = 0
high = len(thousands_numbers) - 1
guess_count = 0

start_time = time.time()

while low <= high:
    guess_count += 1
    mid = (low + high) // 2
    print(f"Guess #{guess_count}: mid={mid} low={low} high={high}")

    if mid < the_answer:
        low = mid + 1
    elif mid > the_answer:
        high = mid - 1
    else:
        print(f"Found it! The answer is {the_answer} and the {mid}. It takes guess for {guess_count} times")
        break

end_time = time.time()

exec_time = end_time - start_time
print(f"Execution time: {exec_time:.4f} seconds")