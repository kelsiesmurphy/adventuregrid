from flask import Flask, Blueprint, redirect, render_template, request
from models.users_experiences import Users_Experiences
import repositories.users_experience_repository as users_experiences_repository

users_experiences_blueprint = Blueprint("users_experiences", __name__)