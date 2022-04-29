from models.users import User
from base import session_factory

session = session_factory()
adarsh = User(**dict(user_name="adarsh",first_name="Adarsh", last_name="Ramalingaiah", email="adakr@deloitte.com"))
anusha = User(**dict(user_name="anusha",first_name="Anusha",last_name="Shetty", email="anusha@gmail.com"))


session.add(adarsh)
session.add(anusha)

session.commit()
session.close