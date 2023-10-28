#The code I provided is part of importing and declaring classes to use the SQLAlchemy library in Python.
#The `from sqlalchemy import ForeignKey, Column, Integer, String, Numeric` statement imports the classes and data types needed to define columns and foreign keys in a database.
#The `from typing import List` statement imports the List data type to specify the type of list attributes. 
#The `from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship` statement imports classes and functions useful for declaring database model classes. 

from sqlalchemy import ForeignKey, Column, Integer, String , Numeric
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
 
 #The `Base(DeclarativeBase)` class is used as a base class to declare database model classes. This class is provided by SQLAlchemy and provides useful functionality for managing tables and database objects when extended by other classes.

class Base(DeclarativeBase):
    pass

#The “Artists” class corresponds to the “artists” table in the database and contains information about musical artists.
#It has an “artistId” column as the primary key and a “name” column to store the artist name. 
#This class also has a relationship with the "Albums" class to indicate the albums associated with each artist.

class Artists(Base):
    __tablename__="artists"

    artistId = mapped_column(Integer , primary_key= True)
    name = mapped_column(String())
    albums:Mapped[List["Albums"]]= relationship(back_populates="artists")

#The "Albums" class corresponds to the "albums" table in the database and contains information about music albums. 
#It has an "albumId" column as the primary key and columns to store the album title, track duration (in milliseconds), album unit price. 
#This class also has an "artistId" column which is a foreign key referring to "artists". 
#"table to indicate the artist associated with the album. 
#Additionally, this class has relationships with the "Artists" and "Tracks" classes. 
#The "artists" relationship is a "one-to-many" relationship which indicates that each album is associated with a single artist, while the "tracks" relationship is a "one-to-many" relationship which indicates that each album can contain multiple songs.

class Albums(Base):
    __tablename__ = "albums"
    albumId = mapped_column(Integer , primary_key= True)
    title = mapped_column(String())
    artistId = mapped_column(Integer , ForeignKey("artists.artistId"), nullable=False)
    artists:Mapped[List["Artists"]]= relationship(back_populates="albums")
    tracks : Mapped[List["Tracks"]] = relationship(back_populates="albums")

#The “Tracks” class corresponds to the “tracks” table in the database and contains information about music tracks. 
# It has a “trackId” column as the primary key and a “name” column to store the track name.

class Tracks(Base):
    __tablename__="tracks"
    trackId = mapped_column(Integer , primary_key=True)
    name = mapped_column(String())
    milliseconds = mapped_column(String())
    unitPrice = mapped_column(Numeric(precision= 10 , scale = 2), nullable = False)
    albumId = mapped_column(Integer , ForeignKey("albums.albumId"),nullable= False )
    albums : Mapped[List["Albums"]]= relationship(back_populates="tracks")