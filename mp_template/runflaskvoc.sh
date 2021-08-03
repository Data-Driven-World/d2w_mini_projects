#!/bin/bash

port=`voc_get_proxied_server_port` 
flask run -h localhost -p $port