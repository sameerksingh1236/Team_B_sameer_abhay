# Python Image 3.8 version 
FROM python:3.8
# Setting working directory for Docker
WORKDIR /app
# Copying the content to Docker
COPY . .
# Installing Dependencies
RUN pip install -r requirements.txt
# Defining the Entry point for the application
EXPOSE 5001
ENTRYPOINT [ "python" ]
# Starting point of the Application
CMD [ "app.py" ]