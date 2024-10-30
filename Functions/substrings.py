def parse_and_display(full_name):

    space_index = full_name.find(" ")
    first_name = full_name[:space_index]
    last_name = full_name[space_index + 1:]
    
    print(f"Full Name: {full_name}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}\n")

parse_and_display('Abbey Road')
parse_and_display('Hey Jude')
parse_and_display('Sargent Pepper')