from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, article, topic, article_rating):
	knowledge_object = Knowledge(
	    name = name,
	    article = article,
	    topic = topic,
	    article_rating = article_rating)

	session.add(knowledge_object)
	session.commit()

add_article(name = "Kareem",article = "https://en.wikipedia.org/wiki/Biology",topic = "Biology",article_rating = 2)
add_article(name = "Wissam",article = "https://en.wikipedia.org/wiki/Cat#Disease",topic = "Killing Cats",article_rating = 10)
add_article(name = "Caleb",article = "https://en.wikipedia.org/wiki/Bhangra_(dance)",topic = "Banghra Dancing",article_rating = 8)



def query_all_articles():
	all_articles = session.query(Knowledge).all()
	print(all_articles)
	return

print(query_all_articles())

def query_article_by_topic(topic):
	artcile_by_topic = session.query(Knowledge).filter_by(topic=topic).first()
	print(artcile_by_topic)
	return

query_article_by_topic("Biology")


def delete_article_by_topic():
	delete_by_topic = session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

delete_article_by_topic("Banghra Dancing")

def delete_all_articles():
	pass

def edit_article_rating():
	pass
