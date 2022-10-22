FROM python:3.8
LABEL CREATOR="AMIRAJOODANI | https://nextsysadmin.ir"



# Set working directory
RUN mkdir /logapp
WORKDIR /logapp
COPY . /logapp

# Installing requirements
ADD requirements/req.txt /logapp
RUN pip3 install --upgrade pip
RUN pip3 install -r req.txt

# Collect static files
RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "logapp", "--bind", ":8000", "sadadlog.wsgi:application"]

