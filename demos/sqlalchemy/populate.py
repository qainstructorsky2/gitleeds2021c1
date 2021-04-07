from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Let's import our Book and Base classes from our database_setup.py file
from db_setup import Book, Base

# bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine( "mysql://root:#Pa$$w0rd#@54.74.234.11/peter_demo?charset=utf8mb4" )
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

# Create

bookOne = Book( title="The No. 1 Ladies' Detective Agency", author="Alexander McCall Smith", genre='fiction' )
session.add(bookOne)
session.commit()

# Read

session.query(Book).all()
session.query(Book).first()

# Update
#editedBook = session.query(Book).filter_by(id=1).one()
#editedBook.author = "Alexander McCall Smith"
#session.add(editedBook)
#session.commit()

# Delete

#bookToDelete = session.query(Book).filter_by(title="The No. 1 Ladies' Detective Agency").one()
#ession.delete(bookToDelete)
#ßsession.commit()
