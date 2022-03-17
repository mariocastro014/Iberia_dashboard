from flask import render_template, request, session, redirect, url_for
from app import app
from werkzeug.security import generate_password_hash, check_password_hash