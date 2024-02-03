from asyncio import constants
from flask import Flask, render_template, jsonify
from CareersWebsite import app

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",
                           company_name = 'Mele',
                           jobs = JOBS)

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)

"""
Don't know how to add a temp array

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Milan, Italy',
        'salary': '2,000€'
    },
    {
        'id': 2,
        'title': 'Frontend Engineer',
        'location': 'Venice, Italy',
        'salary': '3,000€'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Rome, Italy',
        'salary': '4,000€'
    }
]
"""