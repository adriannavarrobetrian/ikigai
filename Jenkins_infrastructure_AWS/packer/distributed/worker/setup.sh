#!/bin/bash

echo "Install Java JDK 8"
yum update -y
yum install java-17-amazon-corretto-devel -y

echo "Install Docker engine"
yum update -y
yum install docker -y
usermod -aG docker ec2-user
systemctl enable docker

echo "Install git"
yum install -y git