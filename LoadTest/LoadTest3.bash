#!/bin/bash 
javac LoadTest.java 
echo $SECONDS 
java LoadTest 127.0.0.1 8080 11 GET 10000 & 
java LoadTest 127.0.0.1 8080 11 GET 10000 & 
java LoadTest 127.0.0.1 8080 11 GET 10000 & 
java LoadTest 127.0.0.1 8080 11 GET 10000 &
wait $(jobs -p) 
echo $SECONDS
