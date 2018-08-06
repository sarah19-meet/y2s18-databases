from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__="knowledge"
	knowledge_id= Column(Integer, primary_key=True)
	Article_name=Column(String)
	Article_topic=Column(String)
	Article_rating=Column(Integer)

	def __repr__(self):
		return("Knowledge Article_name:{}\n"
			"Knowledge Article_topic:{}\n"
			"Knowledge Article_rating:{}").format(
			self.Article_name,
			self.Article_topic,
			self.Article_rating)

		print(repr(Knowledge.__table__))


s=Knowledge(Article_name="rainbow",Article_topic="weather",Article_rating=9)
print(s)






	