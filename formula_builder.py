#!/usr/bin/env python
import os
import sys
import datetime

readme = """
%s
=========================
Install and configure %s

Available states
----------------
``%s``
  Install the ``%s`` software and enable the service.

``%s.bar``
  Install the ``bar`` package
"""

changelog = """
%s formula
=====================
0.0.1 (%date)

- Initial creation
"""

license = """
---Insert your license of choice here---
"""

pillar = """
somekey: somevalue
"""

version = """
The VERSION file should contain the currently released version of the particular formula.
Current release version of this formula = 
"""

map_jinja = """
{% set mysql = salt['grains.filter_by']({
    'Ubuntu': {
        'server': 'mysql-server',
        'client': 'mysql-client',
        'service': 'mysql',
        'config': '/etc/mysql/my.cnf',
    },
    'CentOS': {
        'server': 'mysql-server',
        'client': 'mysql',
        'service': 'mysqld',
        'config': '/etc/my.cnf',
    },
}, merge=salt['pillar.get']('mysql:lookup')) %}
"""

init_sls = """
# Use main init for basic state with sane defaults
# Put advanced state info into child states built using basic states
mysql:
  pkg:
    - installed
  service:
    - running
"""

bar_sls = """
include:
  - mysql

pkg:
  - installed
  - name: python-mysqldb
  - require_in:
    - pkg: mysql
"""


def get_date():
  '''Get the current date and time - returning it as a nice string -- yyyy-mm-dd-hh-mm-ss'''
  runtime = datetime.datetime.now()
  year = str(runtime.year)
  month = str(runtime.month)
  day = str(runtime.day)
  dt = year + "-" + month + "-" + day
  return dt

def write_file(filename, content):
  try:
    f = open(filename, 'w')
    f.write(content)
    f.close()
  except Exception, e:
    print "Could not write file %s" % filename
  return

if len(sys.argv) < 2:
  sys.exit("Usage: build_formula.py formula-name")

formula_name = sys.argv[1]
top_path = "formula-" + formula_name
try:
  os.makedirs(top_path)
except Exception, e:
  print "Unable to create directory %s" % top_path
  print e
  sys.exit(1)

try:
  os.chdir(top_path)
except Exception, e:
  print "Unable to chdir into directory %s" % top_path
  print e
  sys.exit(1)

readme = readme.replace('%s', formula_name)
write_file("README.rst", readme)

changelog = changelog.replace('%s', formula_name)
changelog = changelog.replace('%date', get_date())
write_file("CHANGELOG.rst", changelog)
write_file("License", license)
write_file("pillar.example",pillar)
write_file("VERSION", version)

try:
  os.makedirs(formula_name)
except Exception, e:
  print "Unable to create directory %s" % formula_name
  print e
  sys.exit(1)

try:
  os.chdir(formula_name)
except Exception, e:
  print "Unable to chdir into directory %s" % formula_name
  sys.exit(1)

write_file("map.jinja", map_jinja)
write_file("init.sls", init_sls)
write_file("bar.sls", bar_sls)

print "Finished creating new Salt State Forumula: %s" % top_path
