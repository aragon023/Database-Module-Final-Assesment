from app import app, db
from models import User

def main():
    with app.app_context():
        email = "admin@example.com"       
        password = "NewStrongPass123!"     
        name = "Admin User"

        # check if user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email, name=name, is_admin=True)
            user.set_password(password)  
            db.session.add(user)
            print("Created new admin user")
        else:
            user.is_admin = True
            user.set_password(password)
            print("Updated existing user to admin")

        db.session.commit()
        print(f"Admin user ready: {email} / {password}")

if __name__ == "__main__":
    main()