import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

from twoyear import two_yr


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

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
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

# # Convert list of tuples into normal list
# #https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ravel.html
# all_names = list(np.ravel(results))

@app.route("/api/v1.0/precipitaion")
def precipitation():
    


@app.route("/api/v1.0/station")
def station():

@app.route("/api/v1.0/tobs")
def tobs():

@app.route("/api/v1.0/<start>")
def start():


if __name__ == '__main__':
    app.run(debug=True)