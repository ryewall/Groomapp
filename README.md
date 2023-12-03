# Groomapp
Portfolio Project: Groomapp

Groomapp is a database used for scheduling appointments for dog grooming services. The database will help a groomer keep track of their clientlist, information about each of the dogs that they groom and allow them to schedule appointments for the dogs using REST API. The database is written using ORM in Python with the help of flask, alembic and sqlalchemy.

I chose to use object-relational mapping in order to furthur my understanding of python and because I could more easily understand creating the REST API using objects. In the future I will also write the model using raw sequel becuase I understand that it is more universal and easier to understand.

I plan to work on this database some more and implement more API endpoints. I would like to be able to add services to the appointments and also make the date/time of the schedule unique when considered simultaneously (in postgres one cannot use DateTime datatypes so it was necessary to split this into 2 columns). I also need to seed the database with more information to run more tests and ultimitely finish developing this idea all the way to help my friend with her business.
 