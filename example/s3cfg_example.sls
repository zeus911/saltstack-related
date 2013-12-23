#!py

# working example of using pure python to create a state file

def run():
  config = {}
  user = 'root'
  group = 'root'
  home = '/root/'

  config['s3cmd'] = {
    'pkg': [
      'installed',
      {'name': 's3cmd'},
     ],
   }

  config[home + '/.s3cfg-test'] = {
    'file.managed': [
      {'source': 'salt://s3cfg/templates/s3cfg'},
      {'template': 'jinja'},
      {'user': user},
      {'group': group},
      {'mode': 600},
      {'context': {
        'aws_key': 'AWS_ACCESS_KEY_ID',
        'aws_secret_key': 'AWS_SECRET_ACCESS_KEY',
          },
        },
      ],
  }

  return config
