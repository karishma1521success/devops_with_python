terraform {
  required_version = ">= 1.13.0"   # Replace with your installed Terraform version if different

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0, < 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}