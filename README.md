# Python Flask App Template

## Summary

Flask application boilerplate/template with the following features:
- Organized as a flask package
- Configuration classes
  - configuration injection in run.py
- Blueprint pattern
- pytest
- psql configurations for prod
- sqlite for dev and testing
- pydecouple and .env file for production environment variables
- static folder set up with basic css, js, img, and a generic favicon

## What you're going to need to do...

### Setup local virtual environment
`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

### Add .env File
- place at the root of your directory
- load up with your production variables

### Name Your Application
- use and IDE to refector/change the name of the app directory
- update the app variable to match your project directory name
  - highlight app declaration line
  - right click -> rename symbol

### Update Configuration Classes
Out of the box this template contains:
- Base
- Dev
- Testing
- Prod