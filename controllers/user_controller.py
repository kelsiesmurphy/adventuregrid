from flask import Flask, Blueprint, redirect, render_template, request
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)


# INDEX
# GET '/users'
@users_blueprint.route('/users')
def users_home():
    users = user_repository.select_all()
    return render_template('users/index.html', users=users)


# NEW USER
# GET '/users/new'
@users_blueprint.route('/users/new')
def users_new():
    return render_template('users/create.html')


# CREATE USER
# POST '/users'


# SHOW USER
# GET '/users/<id>'
@users_blueprint.route('/users/<int:id>')
def user_show(id):
    user = user_repository.select_by_id(id)
    return render_template('users/show.html', user=user)


# EDIT USER
# GET '/users/<id>/edit'


# UPDATE USER
# POST '/users/<id>' (would normally be PUT)


# DELETE USER
# DELETE '/users/<id>/delete'