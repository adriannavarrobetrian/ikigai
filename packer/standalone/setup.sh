#!/bin/bash

echo "Install Jenkins stable release"
yum remove -y java
sudo dnf update -y
dnf install java-17-amazon-corretto-devel
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
rpm --import http://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum install -y jenkins
chkconfig jenkins on
service jenkins start
