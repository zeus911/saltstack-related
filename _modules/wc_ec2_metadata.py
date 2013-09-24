#!/usr/bin/env python
import urllib2
# Reference: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html

# MetaData we want to make available using salt: public-hostname, public-ipv4, instance-id, placement, security-groups

def get_public_dns():
  '''A function to retrieve the public dns address of a server

  CLI Example::
    salt stage3 hp_dns.get_public_dns
  '''
  url = "http://169.254.169.254/latest/meta-data/public-hostname"
  f = urllib2.urlopen(url)
  output = f.read()
  return output

def get_public_ipv4():
  '''A function to retrieve the public ip v4 address of a server

  CLI Example::
    salt stage3 hp_dns.get_public_ipv4
  '''
  url = "http://169.254.169.254/latest/meta-data/public-ipv4"
  f = urllib2.urlopen(url)
  output = f.read()
  return output

def get_instance_id():
  '''A function to retrieve the aws instance id of a server

  CLI Example::
    salt stage3 hp_dns.get_instance_id
  '''
  url = "http://169.254.169.254/latest/meta-data/instance-id"
  f = urllib2.urlopen(url)
  output = f.read()
  return output

def get_placement():
  '''A function to retrieve the aws placement of a server

  CLI Example::
    salt stage3 hp_dns.get_placement
  '''
  url = "http://169.254.169.254/latest/meta-data/placement"
  f = urllib2.urlopen(url)
  output = f.read()
  return output

def get_security_groups():
  '''A function to retrieve the security groups an aws instance has been placed

  CLI Example::
    salt stage3 hp_dns.get_security_groups
  '''
  url = "http://169.254.169.254/latest/meta-data/security-groups"
  f = urllib2.urlopen(url)
  output = f.read()
  return output

if __name__ == "__main__":
  print get_public_dns()
