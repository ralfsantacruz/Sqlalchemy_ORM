import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Defined function to get date two years ago.
from twoyear import two_yr


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# # Convert list of tuples into normal list
# #https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ravel.html
# all_names = list(np.ravel(results))

@app.route("/api/v1.0/precipitation")
def precipitation():
    """This function makes a dictionary from your query and serves it up in JSON."""
    # Querying for dates and measurements from last 2 years.
    precip_data = dict(session.query(Measurement.date,Measurement.prcp)\
    .filter(Measurement.date > two_yr()).all())
    return jsonify(precip_data)

@app.route("/api/v1.0/station")
def station():
    # Simple list comprehension to get station names.
    stations = [x.station for x in session.query(Station)]
    return jsonify(stations)
    

@app.route("/api/v1.0/tobs")
def tobs():
    # Another list comprehension to get the observed temps as a list.
    tobs = [x.tobs for x in session.query(Measurement).filter(Measurement.date > two_yr())]
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    # Gets max, min and avg temps for a start date. Makes a dictionary from returned tuples and uses keys in 'y'.
    x = engine.execute("select max(tobs), min(tobs), avg(tobs) from measurement where date > '{0}'".format(start))
    y = ('TMAX','TMIN','TAVG')
    dic = {}
    for i in x:
        tup = i
        break
    for a,b in zip(y,tup):
        dic[a]=b
    
    return jsonify(dic)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    x = engine.execute("select max(tobs), min(tobs), avg(tobs) from measurement where date >= '{0}' and date <= '{1}'".format(start,end))
    y = ('TMAX','TMIN','TAVG')
    dic = {}
    for i in x:
        tup = i
        break
    for a,b in zip(y,tup):
        dic[a]=b
    
    return jsonify(dic)


if __name__ == '__main__':
    app.run(debug=True)