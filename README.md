# project_crawl

Step 1 

1. Install Charles Proxy 
2. Install the chosen app on my ios device *Ricardo.ch*
3. Configure proxy manual => local server and port from Charles 
4. Install Charles SSL certificate 
SSL - Secure Sockets Layer, a global standard security technology that enables encrypted communication between a web browser and a web server. 
In order to create this secure connection, a SSL certificate is installed on a web server and serves 2 functions: 

It authenticates the identity of the website (this guarantees visitors that they’re not on a bogus site)
It encrypts the data that’s being transmitted

5. Listen to the network traffic and enter the app on the ios device. 
  In my case, I've chosen the API with a list of the newest articles. 
6. Copy the cURL request and convert it into a Python request 

Step 2 

7. In PyCharm -> receive a json file by sending a get request 
8. Generate a json file with all of the articles received 
9. zip the result and generate a zipfile 

Docker 

Docker is a tool that enables developers to ship their applications (along with libraries and other dependencies), ensuring that they can run with the exact same configuration, regardless of the environment in which they're deployed.

This is done by isolating the applications in individual containers, which, although separated by containers, share the operating system and adequate libraries.

Docker can be broken down into:

Docker Engine – A software packaging tool used to containerize applications.
Docker Hub – A tool for managing your container applications in the cloud.

FROM python:3.7 
ADD main.py /
CMD [ "python", "./main.py" ] 

FROM - used to specify the base image from which the image is built
ADD - adding local files (main.py) to the docker image 
CMD - runs the main.py app 


- I wasn't sure how to create the distributed crawler and due to technical issues with my laptop, I didn't have enough time to evaluate all of the tasks. But I am surely going to continue researching how to complete all of the them. 


