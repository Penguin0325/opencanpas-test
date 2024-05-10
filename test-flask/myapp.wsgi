activate_this = '/home/hoge/.local/share/virtualenvs/wsgi-scripts-XXXXXX/bin/activate_this.py'
with open(activate_this) as file_:
  exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, 'var/www/html/wsgi-scripts')

from hello import app as application
