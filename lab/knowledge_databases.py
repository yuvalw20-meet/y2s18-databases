from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Article():

	"""
	Design and comment functions to
	-create an article object
	-add an article to the DB
	-Remove an article from the DB
	-Edit an article, to update its
	rating

	Article objects should have the structure
	defined in knowledge_model.py
	"""