from sqlalchemy.orm import Session
from models.user_model import User

class UserService:

    def get_all_users(self, db_session: Session):
        users = db_session.query(User).all()
        return users

    def get_user_by_id(self, db_session: Session, user_id: int,):
        user = db_session.query(User).filter(User.ID == user_id).first()
        return user


    def create_user(self, db_session: Session, name: str, weight: float, description: str = ""):
        new_user = User(NAME=name,
                            WEIGHT=weight,
                            DESCRIPTION=description
                            )

        db_session.add(new_user)
        db_session.commit()
        db_session.refresh(new_user)

        return new_user
    

    def edit_user(self, db_session: Session, user_id: int, name: str = None, weight: float = None, description: str = None):
        user = db_session.query(User).filter(User.ID == user_id).first()

        if user:
            user.NAME = name if not(name) else user.NAME
            user.WEIGHT = weight if not(weight) else user.WEIGHT
            user.DESCRIPTION = description if not(description) else user.DESCRIPTION

            db_session.commit()
            db_session.refresh(user)
        
        return user


    def delete_user(self, db_session: Session, user_id: int):
        user = db_session.query(User).filter(User.ID == user_id).first()

        if user:
            db_session.delete(user)
            db_session.commit()
            db_session.flush()
            return True
        else:
            return False
    
    def delete__all_users(self, db_session: Session):
        users = db_session.query(User).all()

        if len(users):
            db_session.delete(users)
            db_session.commit()
            db_session.flush()
            return True
        else:
            return False

