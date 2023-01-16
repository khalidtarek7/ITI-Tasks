resource "aws_route" "igw-route" {
  route_table_id            = "rtb-05dcb9724bc03c2f0"
  destination_cidr_block    = "0.0.0.0/0"
  gateway_id = "igw-0cf997b08a5d85b9d"
}

