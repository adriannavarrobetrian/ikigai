# Jenkins infrastructure on AWS

## Introduction

- It uses Packer for building images for Jenkins master and for Jenkins agents.
- Deploys a VPC with public and private networks using Terraform.
- Jenkins agents attach themselves to the Jenkins master at boot up.
- Jenkins agents scale up and down based on load using autoscaling groups.
- Jenkins is available through a cloud load balancer.
- Deploys a microservice architecture with several languages: Go, Python, NodeJS