from flask import Flask, Blueprint, redirect, render_template, request
from models.experience import Experience
import repositories.experience_repository as experience_repository

experiences_blueprint = Blueprint("experiences", __name__)


# INDEX
# GET '/experiences'
@experiences_blueprint.route('/experiences')
def experiences_home():
    experiences = experience_repository.select_all()
    return render_template('experiences/index.html', experiences=experiences)


# NEW EXPERIENCE
# GET '/experiences/new'
@experiences_blueprint.route('/experiences/new')
def experience_new():
    return render_template('experiences/create.html')


# CREATE EXPERIENCE
# POST '/experiences'


# SHOW EXPERIENCE
# GET '/experiences/<id>'
@experiences_blueprint.route('/experiences/<id>')
def experience_show(id):
    experience = experience_repository.select_by_id(id)
    return render_template('experiences/show.html', experience = experience)


# EDIT EXPERIENCE
# GET '/experiences/<id>/edit'


# UPDATE EXPERIENCE
# POST '/experiences/<id>' (would normally be PUT)


# DELETE EXPERIENCE
# DELETE '/experiences/<id>/delete'