import mlflow
with open("artifats.txt","r") as f:
    text=f.read()

new_text="end of stage 02"
mlflow.log_param("text", new_text)
print("end of stage 02")