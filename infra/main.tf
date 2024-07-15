terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.region
}


resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.s3_name

  tags = {
    Name        = var.s3_name
    Environment = "Dev"
  }
}