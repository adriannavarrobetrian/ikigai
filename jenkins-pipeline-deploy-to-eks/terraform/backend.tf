terraform {
  backend "s3" {
    bucket = "terraform-state-ikigai"
    region = "eu-west-2"
    key = "eks/terraform.tfstate"
  }
}

provider "aws" {
  region = "eu-west-2"
}