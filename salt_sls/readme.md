### sls are salt state files, which can define event or orchestration tasks

In our small sample application, the turtlebot sends an event to the salt master when it has returned to his home position. 
this event sls triggers then an salt orchestration task on the salt master. The orchestration task is also defined in an other sls file. 

so to get it working the sls files must be in the correct directory:

event sls: /srv/reactor/someEvent.sls
orchestration sls: /srv/salt/orch/someOrchestration.sls

to trigger the event sls an entry has to be added to the salt-master configuration
