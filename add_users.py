from db import  db_session, User

users = [
    {
        'first_name': 'Anakin',
        'last_name': 'Skywalker',
        'email': 'darkside@sith.com',
    },
    {
        'first_name': 'Luke',
        'last_name': 'Skywalker',
        'email': 'lightside@jedi.com',
    },
    {
        'first_name': 'Yoda',
        'last_name': 'Master',
        'email': 'green@badass.com',

    }
]

for u in users:
    user = User(u['first_name'], u['last_name'], u['email'])
    db_session.add(user)

db_session.commit()