terraform {
  required_version = ">= 1.0.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  backend "s3" {

    bucket         = "terraform-state-ikigai"
    key            = "prod/data-stores/mysql/terraform.tfstate"
    region         = "eu-west-2"
    dynamodb_table = "terraform-locks-ikigai"
    encrypt        = true

  }
}

provider "aws" {
  region = "eu-west-2"
}

module "mysql" {
  source = "../../../../modules/data-stores/mysql"

  db_name     = var.db_name
  db_username = var.db_username
  db_password = var.db_password
}
