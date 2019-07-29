from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'peopleWannaLearn'
	student_id = Column(Integer, primary_key=True)
	name = Column(String)
	article = Column(String)
	topic = Column(String)
	article_rating = Column(Integer)
	def __repr__(self):
		consReturn =("ID: {}\n"
				"Student Name: {}\n"
				"Chosen Topic: {}\n"
				"Chosen Article: {}\n"
				"Chosen article_rating: {}").format(
					self.student_id,
					self.name,
					self.topic,
					self.article,
					self.article_rating,)

		if self.article_rating < 7:
			return(str(consReturn) + ", not very useful is it...")
		else:
			return(str(consReturn)) 



# kareem = Knowledge(student_id = 0,name = "Kareem",article = "https://en.wikipedia.org/wiki/Biology",topic = "Biology",article_rating = 2)
# wissam = Knowledge(student_id = 1,name = "Wissam",article = "https://en.wikipedia.org/wiki/Cat#Disease",topic = "Killing Cats",article_rating = 10)
# caleb = Knowledge(student_id = 2,name = "Caleb",article = "https://en.wikipedia.org/wiki/Bhangra_(dance)",topic = "Banghra Dancing",article_rating = 8)




# print(str(kareem) + "\n\n" + str(wissam) + "\n\n" + str(caleb))