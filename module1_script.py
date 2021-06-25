#Module 1
#check which python version the system is using
#for mac python3 -V
#for pc python -V and the result is #Python 3.9.5

#go to packages-platformio-ide-terminal
#new terminal

#create a virtual environment
#for mac python3 -m venv webdash2
#for pc python -m venv webdash2

#activate a virtual environment
#for mac source ./webdash/Scripts/activate
#for pc first make changes to the setting of powershell
#right click open powershell
#run: set-executionpolicy remotesigned
#then for pc
#webdash\Scripts\activate
#it works

#install fastapi and unicorn in the virtual environment
#pip install fastapi
#pip install uvicorn

#app.py file
#from fastapi import FastAPI
#app = FastAPI ()
#@app .get ("/")
#def welcome ():
#x = {" message ": " HELLO WORLD !!! Welcome to fastAPI !!"}
#return x

#main.py file
#import uvicorn
#if __name__ == "__main__":
#    uvicorn.run ("app.app:app",host="0.0.0.0",port=8080,reload=True)
#go into the virtual environment run
#python main.py
#then the first web application can be viewed at
#http://0.0.0.0:8080
#http://localhost:8080/


#module 2
#download okteto cli
#Download https://downloads.okteto.com/cli/okteto.exe
#then i move the okteto cli into an existing path
#advanced system settings- environment variables- path- edit- C:\Users\angelineamber\AppData\Local\atom\bin
#then in the webdash virtual environment, type okteto
#and it will show available commends
#analytics, build, config, create, delete, doctor, down, exec, help, init...

#kubernetes config file
#this is what i copied over from okteto
###$Env:KUBECONFIG=("$HOME\Downloads\okteto-kube.config;$Env:KUBECONFIG;$HOME\.kube\config")
#this is from professor's slides
#Windows:
###$Env:KUBECONFIG=("$HOME\Downloads\okteto-kube.config;$Env:KUBECONFIG;$HOME\.kube\config")
#(Env should be env)

#test if everything is correct: kubectl get all

#in webdash virtual env run:
#pip freeze > requirements.txt


# wei
#$env:KUBECONFIG="$HOME\Downloads\okteto-kube.config"

#download kubectl
#C:\Users\angelineamber\Desktop\web_dashboard_waj_course\cli\kubectl.exe "get pod"
"No resources found in andiangeline namespace"

#dir env: show all environmen variables "KUBECONFIG"
#KUBECONFIG                     C:\Users\angelineamber\Downloads\okteto-kube.config

#get requirements.txt file by running "pip freeze > requirements.txt"
#then a requirements file will be generated in "C:\Users\angelineamber\Desktop\web_dashboard_waj_course\atom_scripts"

#okteto up
#okteto login (may not need to run if already logged in)

#pip install -r requirements.txt
