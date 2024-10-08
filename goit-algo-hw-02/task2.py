from collections import deque

def is_palindrome(string_check) -> bool:
    string_check = string_check.lower()
    deq = deque(string_check)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True

def main():
    while True:
        user_input = input("Enter a string to check if it's a palindrome: ")
        if is_palindrome(user_input):  #юзер може ввести слово для перевірки"
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()