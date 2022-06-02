import mlflow

with open("artifats.txt","r") as f:
    text=f.read()


with open("artifats02.txt","w") as f:
    text=f.write(text+"added line")
mlflow.log_metric("last_text", text)
print("end of stage 3")