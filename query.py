from duombaze import db, Query

db.create_all()

jonas = Query('Jonas', 'jon@gmail.com', 'Sveiki visi')
petras = Query('Petras', 'petr@gmail.com', 'Viso gero')

db.session.add_all([jonas, petras])

db.session.commit()