from flask import Flask, Blueprint, redirect, render_template, request
from models.experience import Experience
import repositories.experience_repository as experience_repository

experiences_blueprint = Blueprint("experiences", __name__)