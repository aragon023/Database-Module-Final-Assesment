from getpass import getpass
from app import app, db
from models import User

def main():
    with app.app_context():
        email = input("Enter admin email: ").strip()
        password = getpass("Enter admin password: ")

        user = User(email=email, is_admin=True)
        user.set_password(password)  # assuming your User model has this method
        db.session.add(user)
        db.session.commit()
        print(f"Admin user {email} created successfully.")

if __name__ == "__main__":
    main()