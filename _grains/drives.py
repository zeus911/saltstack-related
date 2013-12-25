#!/usr/bin/env python
import os
import os.path


def gather_cloudera_mount_points():
  # Get a list of directories at /
  thedir = "/"
  candidates = os.listdir(thedir)
  #print "candidates are: %s" % candidates
  actual_dirs = []
  for c in candidates:
    filepath = os.path.join(thedir, c)
    if os.path.isdir(filepath):
      actual_dirs.append(filepath)
  #print "actual_dirs are %s" % actual_dirs
 
  # Prune to only be mount points
  mountpoints = []
  for d in actual_dirs:
    if os.path.ismount(d):
      mountpoints.append(d)
  #print "mountpoints are %s" % mountpoints
  
  cloudera_mounts = []
  for m in mountpoints:
    fname = os.path.basename(m)
    if fname.startswith("cloudera"):
      cloudera_mounts.append(m)
  #print "cloudera_mounts are %s" % cloudera_mounts
  
  return {'cloudera_drives':cloudera_mounts}

if __name__ == "__main__":
  print "cloudera drives are: "
  print gather_cloudera_mount_points()
