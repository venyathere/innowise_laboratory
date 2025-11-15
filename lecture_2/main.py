def get_hobbies():
    hobbies = []
    hobby = None
    while hobby != "stop":
        hobby = input("Enter favorite hobby or type 'stop' to finish: ").lower()
        hobbies.append(hobby)
        if hobby == "stop":
            hobbies.remove("stop")
            break
    
    return hobbies

def generate_profile(current_age):
    if current_age <= 13:
        life_stage = "Child"
    elif current_age <= 19:
        life_stage = "Teenager"
    else:
        life_stage = "Adult"

    return life_stage

def output(user_profile, hobbies):
    print("---")
    print("Here is your profile summary")
    print(f"Your full name is: {user_profile["full_name"]}")
    print(f"Your age is: {user_profile["age"]}")
    print(f"Your life stage is: {user_profile["life_stage"]}")
    if len(hobbies) > 0:
        print(f"You have {len(hobbies)} hobbies. Here they are:")
        for i in range(0,len(hobbies)):
            print(f"{i+1}. {hobbies[i]}")
    else:
        print("You didn't mention any hobbies.")
    print("---")

def main():
    user_name = input("Enter your Full Name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = 2025 - int(birth_year) 
    hobbies = get_hobbies()
    user_profile = {
        "full_name": user_name,
        "age": current_age,
        "life_stage": generate_profile(current_age),
        "hobbies": hobbies,
    }
    output(user_profile, hobbies)
    
main()
