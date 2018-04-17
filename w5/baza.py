from auto_postgre import City, Country
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://marcin:marcin@localhost:5432/python_w5')
Session = sessionmaker(bind=engine)
session = Session()

all_countries = session.query(Country)
print(all_countries)

#all_penelopes = all_actors.filter(Actor.first_name == 'PENELOPE')

for country in all_countries:
      print(f'{country.country}')
#     print('{} {}'.format(penelope.first_name, penelope.last_name))

#print(all_penelopes.all())

# marcin = Actor(
#     first_name = 'Marcin',
#     last_name = 'Jamroz'
# )
#
# marcin_q = session.query(Actor).filter(Actor.last_name == 'Jamroz').first()
# print(marcin_q)
# print(marcin_q.actor_id, marcin_q.first_name, marcin_q.last_name, marcin_q.last_update)
#
#
# session.add(marcin)
# session.commit()
# print(marcin.actor_id, marcin.first_name, marcin.last_name, marcin.last_update)
#
# marcin_q.first_name = 'MARCIN'
# session.commit()




