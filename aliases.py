# main.py
import text_utils as tu

def aliases():
    input_string = input("Enter a string: ")
    
    reversed_str = tu.reverse_string(input_string)
    capitalized_str = tu.capitalize_string(input_string)

    print(f"Reversed String: {reversed_str}")
    print(f"Capitalized String: {capitalized_str}")

if __name__ == "__main__":
    aliases()