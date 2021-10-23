# Standard Library Rest API

This is as implementation of a simple REST API using only the Python standard library. 

# Motivation

There are many tutorials of varying quality on the web that walk the reader through the process of creating a simple REST API using a framework such as Flask or Django. After  anumber of years in the software industry, I have experience with the benefits of using a framework for large software projects. But these frameworks can take time to confgiure and time to learn. For simple code sketches, I wanted a simple REST server that was extremly fast to set up and did not require any additional overhead or configuration.

Another reason that this repo exists is because I wanted to prove to myself that I could write a REST server from scratch using only the [standard python library documentation](https://docs.python.org/3/library/). After years of contributing features to projects that were already set up by some other developer, it is a nice feeling to know that I can set up a REST server from scratch in just a few short minutes.

# How to Use

1. Pull the repo
2. Change directories into the pulled repo
3. Run the program with `python3 manage.py`
4. Visit the available paths for a `200` response:
  * `localhost:8000`
  * `localhost:8000/ping`
5. Visit any other path for a `404` response

