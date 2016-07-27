#!flask/bin/python
from flask import Flask, jsonify, json
from enum import Enum
import requests, time

app = Flask(__name__)

class State(Enum):
	home = 1
	away = 2

appState = State.home

def getToken():
	tokenUrl = 'http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001/login'

	headers = {'Accept': 'application/json'}

	payload  = {'username':'roboreg',
                'password':'splab',
                'eauth':'pam'
                }
	r = requests.post(tokenUrl, headers=headers, data=payload)

	return r.headers['X-Auth-Token']

@app.route('/orchestrate/api/v1.0/getState', methods=['GET'])
def getState():
    return appState.name

@app.route('/orchestrate/api/v1.0/push', methods=['POST'])
def run():
    global appState
    if appState == State.home:
        goAway()
        appState = State.away
        print appState.name
        return 'went away'
    elif appState == State.away:
        goHome()
        docking()
        appState = State.home
        return 'got home and docked'

def goAway():
    startNodeOnRobot('/home/turtlebot/launch_minimal_amcl.sh')
    time.sleep(5)
    startNodeOnRobot('/home/turtlebot/launch_amcl.sh')
    time.sleep(5)
    startNodeOnRobot('/home/turtlebot/launch_moveto_away.sh')
    # publish to a move_base topic

def goHome():
    startNodeOnRobot('/home/turtlebot/launch_moveto_home.sh')

def docking():
    # kill running nodes
    # start docking nodes 
    print 'docking now'

def startNodeOnRobot(command):
    url = 'http://ab44513583e1711e6b0ef02e4cf15b02-1319127330.eu-central-1.elb.amazonaws.com:8001'

    headers = {'Accept': 'application/json',
               'X-Auth-Token': '' + getToken() + ''
               }

    payload = {'client':'local',
               'tgt':'*',
               'fun':'cmd.run_bg',
               'arg':[command]
               }

    r = requests.post(url, headers=headers, data=payload)

    print 'started node'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
