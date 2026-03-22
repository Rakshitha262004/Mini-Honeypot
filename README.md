# Low-Interaction Honeypot

## Project Overview
This project is a Python-based Low-Interaction Honeypot that simulates an SSH login service and captures attacker activities such as login attempts and connection requests. The captured data including IP address, username, password, and timestamp are stored in a JSON log file and displayed on a Flask-based monitoring dashboard.

## Features
- Simulates SSH login service
- Captures attacker username and password
- Logs attacker IP address and timestamp
- Stores logs in JSON format
- Flask web dashboard for monitoring attacks
- Attack simulation using Python script

## Technologies Used
- Python
- Flask
- Socket Programming
- JSON
- HTML
- Networking

## Project Structure
app.py            - Flask dashboard
listener.py       - Honeypot server
attacker.py       - Attack simulation script
dashboard.html    - Dashboard user interface
dashboard.json    - Log file storing attack data
requirements.txt  - Required Python libraries

## How to Run the Project
1. Start the honeypot listener:
   python listener.py

2. Run the attacker simulation:
   python attacker.py

3. Start the Flask dashboard:
   python app.py

4. Open the browser and go to:
   http://127.0.0.1:5000

## Project Output
The dashboard displays:
- Attacker IP Address
- Username
- Password
- Time of attack

