#!/bin/bash

echo "Install Jenkins stable release"
yum remove -y java
sudo dnf update -y
dnf install java-17-amazon-corretto-devel -y
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
yum install -y jenkins
chkconfig jenkins on
service jenkins start
