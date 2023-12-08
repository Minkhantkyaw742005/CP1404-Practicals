def main():
    """Create a dictionary of emails-to-names."""
    email_to_name = {}
    user_email = input("Email: ")

    while user_email != "":
        user_name = get_name_from_email(user_email)
        confirmation = input(f"Is your name {user_name}? (Y/n) ")

        if confirmation.upper() != "Y" and confirmation != "":
            user_name = input("Name: ")

        email_to_name[user_email] = user_name
        user_email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract an expected name from the email address."""
    email_prefix = email.split('@')[0]
    name_parts = email_prefix.split('.')
    user_name = " ".join(name_parts).title()
    return user_name


main()
