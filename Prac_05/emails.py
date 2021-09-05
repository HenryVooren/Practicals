"""
CP1404/CP5632 Practical
Email dictionary
"""

email_dict = {}
user_email = input(">>> ")
while user_email != "":
    user_name = user_email.split("@")[0].replace(".", " ").title()
    if input(f"Is your name {user_name}? (Y/n) ").lower() == "n":
        user_name = input("Name? ").title()

    email_dict[user_name] = user_email
    user_email = input(">>> ")

for key in email_dict:
    print(f"{key} {email_dict[key]}")
