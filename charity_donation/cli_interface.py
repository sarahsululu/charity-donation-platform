

from .donation_logic import create_campaign, list_campaigns, make_donation

logged_in_user = None 


def prompt_yes_no(message):
    answer = input(message + " (y/n): ").strip().lower()
    return answer in ['y', 'yes']


users = {} 


def register():
    print("\n=== REGISTER ===")
    username = input("Enter username: ").strip()
    if username in users:
        print("❌ Username already exists.")
        return

    password = input("Enter password: ").strip()
    users[username] = password
    print("✅ Registration successful!")


def login():
    global logged_in_user
    print("\n=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if users.get(username) == password:
        logged_in_user = username
        print(f"✅ Welcome, {username}!")
    else:
        print("❌ Invalid username or password.")


def logout():
    global logged_in_user
    logged_in_user = None
    print("✅ You have been logged out.")


def browse_campaigns():
    print("\n=== BROWSE CAMPAIGNS ===")
    campaigns = list_campaigns()
    if not campaigns:
        print("No campaigns available.")
        return

    for c in campaigns:
        print(f"ID: {c.id}, Title: {c.title}, Goal: {c.goal_amount}, Raised: {c.current_amount}")

    if logged_in_user:
        try:
            campaign_id = int(input("Enter Campaign ID to donate (or press Enter to skip): ") or 0)
            if campaign_id != 0:
                donate_to_campaign(campaign_id)
        except ValueError:
            print("❌ Invalid input.")


def create_new_campaign():
    if not logged_in_user:
        print("❌ You must be logged in to create a campaign.")
        return

    print("\n=== CREATE CAMPAIGN ===")
    title = input("Campaign Title: ").strip()
    description = input("Campaign Description: ").strip()
    try:
        goal = float(input("Goal Amount: $").strip())
    except ValueError:
        print("❌ Invalid amount.")
        return

    create_campaign(title, description, goal)


def donate_to_campaign(campaign_id=None):
    if not logged_in_user:
        print("❌ You must be logged in to donate.")
        return

    if campaign_id is None:
        try:
            campaign_id = int(input("Enter Campaign ID to donate: ").strip())
        except ValueError:
            print("❌ Invalid campaign ID.")
            return

    try:
        amount = float(input("Donation Amount: $").strip())
    except ValueError:
        print("❌ Invalid amount.")
        return

    message = input("Optional message (press Enter to skip): ").strip() or None
    make_donation(logged_in_user, campaign_id, amount, message)


def guest_menu():
    while True:
        print("\n=== GUEST MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Browse Campaigns")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            browse_campaigns()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


def user_menu():
    while logged_in_user:
        print(f"\n=== MENU (Logged in as {logged_in_user}) ===")
        print("1. Browse Campaigns")
        print("2. Create Campaign")
        print("3. Donate")
        print("4. Logout")
        print("5. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            browse_campaigns()
        elif choice == "2":
            create_new_campaign()
        elif choice == "3":
            donate_to_campaign()
        elif choice == "4":
            logout()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


def main():
    while True:
        if logged_in_user:
            user_menu()
        else:
            guest_menu()


if __name__ == "__main__":
    main()


