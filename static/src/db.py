from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///preds.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Pred(Base):
    __tablename__ = 'preds'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    text = Column(String)

    def __init__(self, filename, text):
        self.filename = filename
        self.text = text

Base.metadata.create_all(engine)

def add_pred(filename, text):
    session = Session()
    try:
        pred = Pred(filename, text)
        session.add(pred)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()

def get_preds():
    session = Session()
    try:
        preds = session.query(Pred).all()
        return [{'id': pred.id, 'filename': pred.filename, 'text': pred.text} for pred in preds]
    except Exception as e:
        print(e)
        return {"404": "No data found"}
    finally:
        session.close()

def get_pred_by_filename(filename):
    session = Session()
    try:
        pred = session.query(Pred).filter_by(filename=filename).first()
        return {'id': pred.id, 'filename': pred.filename, 'text': pred.text}
    except Exception as e:
        print(e)
        return {"404": "No data found"}
    finally:
        session.close()


