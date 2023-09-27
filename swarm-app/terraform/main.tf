terraform {
  required_version = ">= 1.0.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  backend "s3" {

    # This backend configuration is filled in automatically at test time by Terratest. If you wish to run this example
    # manually, uncomment and fill in the config below.

    bucket         = "terraform-state-ikigai"
    key            = "docker-swarm/terraform.tfstate"
    region         = "eu-west-2"
    dynamodb_table = "terraform-locks-ikigai"
    encrypt        = true

  }
}

provider "aws" {
  region = "eu-west-2"
}


resource "aws_instance" "swarm" {
  ami           = "ami-0eb260c4d5475b901"
  for_each      = toset(var.instance_names)
  instance_type = "t2.large"
  key_name =    "adriantest"

  tags = {
    Name = each.value
    Managedby = "Terraform"
  }
}

variable "instance_names" {
  description = "Instance name"
  type        = list(string)
  default     = ["mgr1", "mgr2", "mgr3", "wrk1", "wrk2", "wrk3"]
}

output "instance_public_ips" {
  value = values(aws_instance.swarm)[*].public_ip
}
