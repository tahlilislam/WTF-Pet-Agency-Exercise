"""Seed file to make sample data for adobt_db."""

from models import Pet, db
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    Pet.query.delete()

    p1 = Pet(name='Woofly', species='dog',
                 photo_url='https://images.unsplash.com/photo-1598133894008-61f7fdb8cc3a?w=1600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZG9nc3xlbnwwfHwwfHx8MA%3D%3D',
                 age=2)
    p2 = Pet(name='Porchetta', species='porcupine',
                 photo_url='https://images.unsplash.com/photo-1598255352496-e67192a8a5ac?w=1600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cG9yY3VwaW5lfGVufDB8fDB8fHww',
                 age=1)
    p3 = Pet(name='Snargle', species='cat',
                 photo_url='https://images.unsplash.com/photo-1621592286525-28400f548051?w=1600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2F0JTIwbWFpbmNvb258ZW58MHx8MHx8fDA%3D',
                 notes = "a large maincoon weighing 20 pounds",
                 age=3)

    db.session.add_all([p1, p2, p3])
    db.session.commit()