from flask import Flask, Blueprint, redirect, render_template, request
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)