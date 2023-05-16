import random


def main():
    print("Khansole Academy")
    # generate 2 numbers
    value_one = random.randint(10, 99)
    value_two = random.randint(10, 99)

    # take input from user for answer
    user_answer = input(f"What is {value_one} + {value_two}? ")

    # print total 2 random numbers added together
    total = value_one + value_two

    # print user answer
    print(f"Your answer: {user_answer}")

    # determine if answer is right or wrong
    if int(user_answer) == total:
        print("Correct!")
    else:
        print("Incorrect.")


if __name__ == "__main__":
    main()
