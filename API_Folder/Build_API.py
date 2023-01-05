from flask import Flask
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app=Flask(__name__)
db.create_all()


class Drink(db.model):
    id=db.column(db.Integer, primary_key=True)
    name=db.column(db.String(80),unique=True,nullable=False)
    description=db.column(db.String(120))
def __repr__(self):
    return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return "<h1>Samundeeswari velusamy</h1>"


@app.route('/drinks')
def get_drinks():
    drinks=drink.query.all()
    output=[]
    for drink in drinks:
        drink_data={'name':drink.name,'description':drink.Description}
        output.append(drink_data)
    return {'drinks':output}


# drink = Drink(name="Grape Soda", Description='Taste like grapes')
# print(drink)
db.session.add(Drink(name="Grape Soda", Description='Taste like grapes'))
db.session.commit()
# drink.query.all()

if __name__ == '__main__':
    app.run(debug=True)