from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(Article_name,Article_topic,Article_rating):
	knowledge_object= Knowledge(
		Article_name=Article_name,
		Article_topic=Article_topic,
		Article_rating=Article_rating)
	session.add(knowledge_object)
	session.commit()

add_article("rainbow","weather", 9)
	

def query_all_articles():
	articles= session.query(
		Knowledge).all()
	return articles
# print(query_all_articles())

def query_article_by_topic(a1):
	topic=session.query(
		Knowledge).filter_by(
		Article_name=a1).first()
	return topic
# print(query_article_by_topic("s"))
	

def delete_article_by_topic(Article_name):
	session.query(Knowledge).filter_by(
		Article_name=Article_name).delete()
	session.commit()
# delete_article_by_topic("rainbow")

	

def delete_all_articles(Article_name):
	session.query(Knowledge).delete()
	session.commit()
delete_all_articles("Knowledge")
	

def edit_article_rating(update_rating,article_title):
	food_object=session.query(
		Knowledge).filter_by(
		Article_topic=article_title).first()
	food_object.Article_rating=update_rating
	session.commit()

edit_article_rating(5,"weather")

	

