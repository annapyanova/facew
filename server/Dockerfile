FROM python:latest
WORKDIR /server
COPY requirements.txt /server
RUN pip3 install --upgrade pip -r requirements.txt
RUN pip3 install opencv-python-headless
COPY . /server
EXPOSE 1234