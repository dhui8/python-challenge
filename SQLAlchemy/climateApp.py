#################################################
# Flask Stuff
#
#
# David Hui
# 02/02/2018
#################################################

import sqlalchemy
import numpy as np
import datetime

from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.ext.automap import  automap_base
from sqlalchemy.sql import func
from sqlalchemy import Date, cast
from flask import Flask, jsonify
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import Session
from sqlalchemy.sql import extract
from sqlalchemy import and_

Base = declarative_base()
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)
Base.classes.keys()
Base.metadata.create_all(engine)
session = Session(bind=engine)
Stations = Base.classes.station
Measures = Base.classes.measure

app = Flask(__name__)



@app.route("/api/v1.0/test")
def precipitation():
	
    #Return a list of daily precipitation information
	
    #Query all precipitation for last year - 2017
	
	results = session.query(func.date(Measures.date), Measures.tobs).\
              filter(extract('year',Measures.date) == 2017).\
              order_by(Measures.date.desc()).all()
	rec_list=list(np.ravel(results))
	
	d=[]
	for key, value in results:
		d.append({'date':key, 'tobs':value})

	return(jsonify(d))
	
	
	
@app.route("/api/v1.0/precipitation_V2")
def precipitation_V2():
	
    #Return a list of daily precipitation information
	
    #Query all precipitation for last year - 2017
	
	results = session.query(func.date(Measures.date), Measures.tobs).\
              filter(extract('year',Measures.date) == 2017).\
              order_by(Measures.date.desc()).all()
	rec_list=list(np.ravel(results))

	print(rec_list)

	return jsonify(rec_list)	


	
@app.route("/api/v1.0/stations")
def stations():
	"""Return a list of all stations"""
	# Query all Stations
        
	results = session.query(Stations.station + '-'+ Stations.name).\
	order_by(Stations.station.asc()).all()
            
    # Convert list of tuples into normal list using np.ravel
	rec_list = list(np.ravel(results))
	
	print(rec_list)
	
	return jsonify(rec_list)
	
	
	
	
@app.route("/api/v1.0/tobs")
def tobs():
	"""Return a json list of tobs from the dataset."""
	# Query all tobs
	# TOBS needs to be casted  for JSON serialization
	results = session.query(cast(Measures.tobs, String)).filter(extract('year',Measures.date) == 2017).order_by(Measures.date.desc()).all()
            
    # Convert list of tuples into normal list using np.ravel
	rec_list = list(np.ravel(results))
	print(results)
	
	return jsonify(rec_list)
	
	
	
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start(start, end=None):

# http://127.0.0.1:5000/api/v1.0/2016-09-01
# http://127.0.0.1:5000/api/v1.0/2016-09-01/2016-10-31
	
	if end == None:
		print("No End Date")
		results = session.query(func.max(Measures.tobs),func.min(Measures.tobs),func.avg(Measures.tobs) ).\
				filter(Measures.date >=s start).all()
	else:
		print("Both Start and End")
		results = session.query(func.max(Measures.tobs),func.min(Measures.tobs),func.avg(Measures.tobs) ).\
				filter(Measures.date.between(start, end)).all()			  
    # Convert list of tuples into normal list using np.ravel
	all_tobs = list(np.ravel(results))

	return jsonify(all_tobs)


	
	
if __name__ == "__main__":
    app.run(debug=True)
	

	

	
