resource "aws_subnet" "mysubnet" {
  vpc_id     = "vpc-0e2fcd9260bbf03af"
  cidr_block = "10.0.0.0/24"
}
resource "aws_route_table_association" "a" {
  subnet_id      = "subnet-02ff9a2007efd4199"
  route_table_id = "rtb-05dcb9724bc03c2f0"
}