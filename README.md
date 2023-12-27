# KubeArmor CLI

## Python3

Steps to run Server/Client demo with python3. We used python3.12 and have already compiled
the proto files. 


1. [Download + Install python3](https://www.python.org/downloads/)

2. Install Requirements (using venv)
```shell
python3 -m venv venv 
source venv/bin/activate 

python3 -m pip install --upgrade pip  
python3 -m pip install --upgrade -r requirements.txt
```

3. Compile proto files 
```shell
for file in `ls proto/` ; do python3 compile.py proto/${file} ; done
```

4. Start Server 
```shell
python3 kube_server.py 
```

