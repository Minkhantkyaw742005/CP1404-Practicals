email_to_name = {}
email = input("Email: ")

while email != "":
    prefix = email.split("@")[0]
    name_parts = prefix.split(".")
    name = " ".join(name_parts).title()
    name_confirm = input(f"Is this your name {name}? (Y/n)")
    if name_confirm != "Y" and