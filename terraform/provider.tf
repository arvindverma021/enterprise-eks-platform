provider "aws" {
  region = "ap-south-1"

  default_tags {
    tags = {
      Project     = "Enterprise-EKS-Platform"
      Environment = "Dev"
      ManagedBy   = "Terraform"
    }
  }
}
