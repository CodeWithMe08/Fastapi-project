from passlib.context import CryptContext

pwd_coontext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_coontext.hash(password)