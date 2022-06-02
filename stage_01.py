import mlflow
text="input 01"
with open("artifats.txt", "w") as f:
    f.write(text)
mlflow.log_artifact("artifats.txt", artifact_path="features")