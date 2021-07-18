#!/usr/bin/env python

# Modules
from pygnmi.client import gNMIclient
from dotenv import load_dotenv
import os

# User-defined functions (Tests)
def test_capabilities():
    load_dotenv()
    username_str = os.getenv("USER")
    password_str = os.getenv("PASS")
    hostname_str = os.getenv("HOST")
    port_str = os.getenv("PORT")
    path_cert_str = os.getenv("CERT")

    with gNMIclient(target=(hostname_str, port_str), username=username_str, 
                    password=password_str, path_cert=path_cert_str) as gc:
        result = gc.capabilities()

    assert "supported_models" in result
    assert "supported_encodings" in result
    assert "gnmi_version" in result

def test_get():
    load_dotenv()
    username_str = os.getenv("USER")
    password_str = os.getenv("PASS")
    hostname_str = os.getenv("HOST")
    port_str = os.getenv("PORT")
    path_cert_str = os.getenv("CERT")

    with gNMIclient(target=(hostname_str, port_str), username=username_str, 
                    password=password_str, path_cert=path_cert_str) as gc:
        gc.capabilities()
        result = gc.get(path=["/"])

    assert "notification" in result
    assert isinstance(result["notification"], list)
