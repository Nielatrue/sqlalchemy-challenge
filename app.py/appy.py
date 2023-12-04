# %%
# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# %%
# Database Setup

#create engine 
engine = create_engine("sqlite:///Resources/hawaii.sqlite") 

# %%
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# %%
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# %%
# Create our session (link) from Python to the DB
session = Session(engine)

conn = engine.connect()

# %%
#Start Homepage

# %%
# Flask Setup
app= Flask(__name__)

# %%
# Flask Routes
@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Welcome to the Climate App API!<br>"
        f"Use this API if you dare...<br/>"
        f"Here are the available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

# %%
#-----2 /api/v1.0/precipitation 
#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.



# %%
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

conn = engine.connect()
 

# %%
results = session.query(measurement.prcp).all()

    

# %%
session.close()

# %%
# Convert list of tuples into normal list
precipitation_data = list(np.ravel(results))

# %%
#     Return the JSON representation of your dictionary.

return jsonify(precipitation_data)

# %%
#3./api/v1.0/stations
#Return a JSON list of stations from the dataset.


# %%
@app.route("/api/v1.0/stations")
def station():
# Create our session (link) from Python to the DB
    session = Session(engine)

conn = engine.connect()



# %%
results = session.query(measurement.station).distinct().all()
session.close()

# %%
station_list = list(np.ravel(results))

# %%
return jsonify(station_list)

# %%
#4 ----- /api/v1.0/tobs

#Query the dates and temperature observations of the most-active station for the previous year of data.

#Return a JSON list of temperature observations for the previous yea

# %%
@app.route("/api/v1.0/tobs")
# Create our session (link) from Python to the D
session = Session(engine)

conn = engine.connect()

# %%
most_active_station = session.query(measurement.station).\
        group_by(measurement.station).\
        order_by(func.count().desc()).\
        first()

# %%
session.close()


