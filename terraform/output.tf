output "instance_id" {
  description = "CloudOps EC2 instance ID"
  value       = aws_instance.cloudops.id
}

output "public_ip" {
  description = "CloudOps EC2 public IP"
  value       = aws_instance.cloudops.public_ip
}

output "vpc_id" {
  description = "CloudOps VPC ID"
  value       = aws_vpc.cloudops.id
}

output "ssh_command" {
  description = "SSH command to connect to the instance"
  value       = "ssh -i <path-to-private-key.pem> ubuntu@${aws_instance.cloudops.public_ip}"
}