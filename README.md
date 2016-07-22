# e2eTurtlebotDemo

The goal is to get a a simple End to End Cloud Robotics application using ROS.
The application we’re implementing uses a Big Red button (bt.tn) to control a turtlebot and switch between two high level goals:
  - Go to docking station and dock
  - Reach a predefined point in the map (goal)


## on the Turtlebot
The minimal lauch and the amcl nodes have to be running. This can be done either manually or via salt. 
Some experimental salt curl commands are in /salt_api_requests/salt_api_requests.md

## kubernetes
For creating the pods and services in kubernetes, you can find the yaml files in the subfolder of /kubernetes
The pods and services can be created using the kubectl or via an existing pod. 

### kubectl:
```
kubectl create -f <pod or service yaml>
```
### create a pod from a pod:
```
url -sSk -H "Authorization: Bearer $KUBE_TOKEN" -H "Content-Type: application/json" --stderr /dev/null --request POST https://$KUBERNETES_SERVICE_HOST:$KUBERNETES_PORT_443_TCP_PORT/api/v1/namespaces/default/pods --data @map_server_pod.json
```

## ros2djs example
this is a static html/js example of showing a map in the browser and display the robot position on it. 
With a double click on the map you can even send the robot around. Further informations on how to get everything running can be found in the nav_notes.md inside the ros2djs_example folder.

## moveto
This is a ROS node which has two predefined position of our lab map. With this node the robot can be send away and back to it's starting point. 
