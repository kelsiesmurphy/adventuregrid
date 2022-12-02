from flask import Flask, Blueprint, redirect, render_template, request
from models.experience import Experience
import repositories.experience_repository as experience_repository

experiences_blueprint = Blueprint("experiences", __name__)


# INDEX
# GET '/experiences'


# NEW EXPERIENCE
# GET '/experiences/new'


# CREATE EXPERIENCE
# POST '/experiences'


# SHOW EXPERIENCE
# GET '/experiences/<id>'


# EDIT EXPERIENCE
# GET '/experiences/<id>/edit'


# UPDATE EXPERIENCE
# POST '/experiences/<id>' (would normally be PUT)


# DELETE EXPERIENCE
# DELETE '/experiences/<id>/delete'