variable "aws_region" {
  description = "AWS region for CloudOps infrastructure"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project resource name prefix"
  type        = string
  default     = "cloudops"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.small"
}

variable "key_name" {
  description = "Existing AWS EC2 key pair name"
  type        = string
}

variable "allowed_ssh_cidr" {
  description = "Your public IPv4 address with /32 mask"
  type        = string

  validation {
    condition     = can(cidrnetmask(var.allowed_ssh_cidr)) && endswith(var.allowed_ssh_cidr, "/32")
    error_message = "Use your public IPv4 address followed by /32, for example 203.0.113.10/32."
  }
}