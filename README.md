*** First stage ***
## System description ##

Background:
Agent and mission management system for the service of a military unit
The system will include a function to manage the system at the agent/mission level
and the groups will be stored in the unit's database.

Goal:
To enable the unit to optimally manage the management of missions and agents
including ensuring that the processes take into account the various constraints.
In addition, the information will be stored at the database level and will allow for orderly and organized access to this data.

*** Step Two ***
## Description of Folder Structures ##
intelligence-task-manager/ 
├── database/ 
|   │   
|   ├── db_connection.py 
|   │   
|   ├── agent_db.py 
|   │   
|   └── mission_db.py
├── services/
|   └── agent_service
|   └── mission_service
├── logs/
|   └──  set_logger.py
|   └──  logs.log
├── README.md
├── main.py 
├── requirements.txt 
└── .gitignore

*** Step Three ***
## Table Structure ##

*** agent table ***

filed               |   type        | extra info 
-------------------------------------------------------
id                      INT         AUTO_INCREMENT, UNIQUE
name                   VARCHAR(50)
specialty              VARCHAR(50)
is_active              BOOLEAN      DEFAULT = TRUE
completed_missions      INT         DEFAULT = 0 
failed_missions         INT         DEFAULT = 0 
agent_rank              ENUM        Junior/Senior/Commander
________________________________________________________


*** missions table ***

filed               |   type        | extra info 
-------------------------------------------------------
id                      INT          AUTO_INCREMENT, UNIQUE
title                  VARCHAR(100)
description            TEXT
location               VARCHAR(100)
difficulty              INT          NUMBER BETWEEN 1-10
importance              INT          NUMBER BETWEEN 1-10
status                 VARCHAR(20)   DEFAULT = NEW
risk_level             VARCHAR(20)   AUTO_CALCULATED
assigned_agent_id       INT          DEFAULT = NULL
________________________________________________________

*** forth step ***
## Explanation of the existing classes and what each function does ##

*** db_connection.py : ***
A basic configuration file that contains the DB connection method and default methods for creating our desired tables

get_connection()
Returns an active connection to the database

create_database()
Creates the Intelligence_db if it has not yet been created

create_tables()
Creates the two desired tables [tasks, agents]
According to the rules we defined if it has not yet been created
_____________________________________________________________

*** agentDB.py ***

the file that includes all crud functions to do within the agent table in the DB.

create_agent(data)
create a new agent with the data that are given and return the agent object

get_all_agents()
return all agents in the agent table in a list
if is null return []

get_agent_by_id(id)
return an agent based on id from the agent table
if not ecsist return NONE

update_agent(id, data)
updating an agent with new info excluding id that cent be changed

deactivate_agent(id)
set status of a specific agent base on id to not active

increment_completed(id) 
updating the number of completed missions. by +1

increment_failed(id) 
updating the number of the failed missions. by +1

get_agent_performance(id)
return an {dict} with a full agent performance

count_active_agents() 
return the number of total active agents

__________________________________________________________

*** missionDB ***

the file that includes all crud functions to do within the missions table in the DB.

create_mission(data)
create a new mission with the data that are given and return the mission object

get_all_missions()
return all missions in the missions table in a list
if is null return []

get_mission_by_id(id)
return an mission based on id from the mission table
if not ecsist return NONE

assign_mission(m_id, a_id)
assign_ a specific mission to un specific agent

update_mission_status(id, status)
update a specific mission with a new status

get_open_missions_by_agent(id)
Returns a list of ASSIGNED/IN_PROGRESS tasks
if none return []

count_all_missions()
return the number of the missions in the table
if none return 0

count_by_status(status)
return the number of the missions in the table
base on a specific given status
if none return 0

count_open_missions()
return the number of the missions in the table
with open status .
if none return 0

count_critical_missions()
return the number of the missions in the table
with critical level
if none return 0

get_top_agent()
return the agent with the higest number of completed missions .

_____________________________________________________________

*** system roles used in services files ***

## roles :##

1. rank :

must be Junior / Senior / Commander — throws every another value  .
2. dificulty ,importance:
must be number between 1-10 otherwise return error
3.risk_level:
The user does not send a value, it is calculated automatically.
4.
An agent whose status is listed as inactive cannot accept tasks.
5.
An agent cannot have more than 3 open tasks.
6.
Missions that are at a critical risk level can only be accepted by an agent who is at the rank of Commender.
7.
A task can only be assigned to an agent if it is in the NEW status. After assignment, the status will change to Assigned.
8.
A task can only be started if it is in the Assigned status
After starting the status will change to in progress
9.
A mission can only be completed if STATUS is in progress
Status will be updated to mission completed or filed
10.
A task can be canceled from an agent
provided its execution status is NEW or assigned
otherwise an error
_______________________________________________________________________________________

*** fifth step ***
## How to run Docker  — Run instructions ##

run docker by this commend :

# docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 \   -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0

install venv and activate it by :
# py -m venv venv
# venv\Scripts\activate

install the reqirments by this commend :
# pip install -r requirements.txt

and then run main app by:
# py main.py

_______________________________________________________________________________________

day2:


