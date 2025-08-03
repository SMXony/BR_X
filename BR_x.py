import sys


pas = input("send the password (4 to 20 characters): ")


keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#৳$%&*+-[]:ঃ


min_len = 4
max_len = 20
found = False


if not (min_len <= len(pas) <= max_len):
    print(f"Error: Password length must be between {min_len} and {max_len} characters.")
    sys.exit()

def brute_force(current_guess, target_length):
    
    global found
    
    
    if found:
        return

    
    if len(current_guess) == target_length:
        
       
        prin(f"Trying: {current_guess}\r", end='', flush=True) 
        
        
        if current_guess == pas:
            print(f"The password is: {current_guess}")
            found = True
            return
        
        return

    
    for char in keys:
        if found:
            return
        brute_force(current_guess + char, target_length)

print("Attacking password... please wait....")


for length in range(min_len, max_len + 1):
    print(f"\nChecking passwords of length {length}...")
    brute_force("", length)
    
    
    if found:
        break

if not found:
    print("Password not found within the specified length and character set.")
