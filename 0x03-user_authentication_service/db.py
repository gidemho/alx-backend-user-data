from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User  # Import the User class from your user module


class DB:
    """DB class for managing database operations."""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)  # Drop all existing tables
        Base.metadata.create_all(self._engine)  # Create new tables
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database and return the User object"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)  # Add the new user to the session
        self._session.commit()  # Commit the transaction to save to the database
        return new_user  # Return the newly created User object


    def find_user_by(self, **kwargs) -> User:
    """Find user by arbitrary keyword arguments."""
     try:
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user
    except InvalidRequestError:
        raise InvalidRequestError


    def update_user(self, user_id: int, **kwargs) -> None:
    """Update user attributes based on given keyword arguments."""

try:
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Attribute '{key}' does not exist on User model")
            setattr(user, key, value)
        self._session.commit()
    except NoResultFound:
        raise NoResultFound(f"User with id {user_id} not found")
    except InvalidRequestError:
        raise InvalidRequestError
