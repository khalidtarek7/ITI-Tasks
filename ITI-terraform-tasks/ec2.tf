resource "aws_instance" "ec2" {
  ami           = "ami-0b5eea76982371e91"
  instance_type = "t2.micro"
  associate_public_ip_address = true
  subnet_id = "subnet-02ff9a2007efd4199"
  vpc_security_group_ids = [aws_security_group.secgroup.id]
  user_data = <<EOF

#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html

EOF
}
