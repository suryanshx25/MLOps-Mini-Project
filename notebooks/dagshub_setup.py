import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/suryanshx25/MLOps-Mini-Project.mlflow')

dagshub.init(repo_owner='suryanshx25', repo_name='MLOps-Mini-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)