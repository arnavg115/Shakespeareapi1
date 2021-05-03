# Shakespeareapi1
This is a simple flask where one can query it and it will generate a text with the number of characters specified. The model is from <a href = "https://www.tensorflow.org/tutorials/text/text_generation">this tensorflow tutorial.</a>
## Setup
This project can be run with or without docker. 
### Docker
Get the docker image from <a href ="https://hub.docker.com/r/arnavg1q5/shakespeareapi">Docker hub</a>. You can do this by doing
```
docker pull arnavg1q5/shakespeareapi:latest
```
Then you can run it
```
docker run -t -d -p 5000:5000 --name shakespeareapi arnavg1q5/shakespeareapi:latest
```
The api is up and running and you can find it at 0.0.0.0:5000.
### Other way
Clone this repository
```
git clone https://github.com/arnavg115/Shakespeareapi1.git
```
and then cd into it
```
cd Shakespeareapi1
```
Then install the dependencies
```
pip install -r requirements.txt
```
or 
```
pip3 install -r requirements.txt
```
Then you can run the python file by doing 
```
python3 app.py
```
This should launch a flask server and then you can access it at 0.0.0.0:5000
## Make a request
Open up 0.0.0.0:5000 and then go to 0.0.0.0:5000/api/v1/request/<insert char num>
for <insert char num> input the number of characters to generate. It should return a dictionary type thing with the key being "Shakespeare" and the value being the generated text.
Simple program to query the api
```python
import requests
repsonse = requests.get(0.0.0.0:5000/api/v1/request/50)
# This is querying the api for a 50 chracter string of writing in a shakespearean style.
print(response.status_code)
if repsonse.status_code == 200:
# Checks if the request is valid
  gentext = response.json()
# gentext is a dictionary in the formate {"Shakespeare":""}
  print(gentext["Shakespeare"])
```
## Access the api without downloading anything
I have put this api up on azure so you can query it <a href = "https://apiapiapi123.azurewebsites.net/">here.</a> This will not always be up so I recommend using a local version. 
