sendRequest:
  salt.runner:   
    - name: http.query
    - url: 'http://acf7984ae549511e69b640206bb85836-1252824845.eu-central-1.elb.amazonaws.com:5000/orchestrate/api/v1.0/dock' 
    - method: POST 
