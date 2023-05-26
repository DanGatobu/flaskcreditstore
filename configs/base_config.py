from lib2to3.pytree import Base
import secrets


FLASK_APP='main.py'
SECRET_KEY=secrets.token_hex(16)

class development(Base):
    FLASK_ENV='development'
    DATABASE="creditstore"

