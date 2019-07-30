# IPython log file

import logging
logging.warning("Hello world")
get_ipython().magic('logoff')
import logging

log = logging.getLogger("my-logger")
log.warning("Hello, world")
get_ipython().magic('logstate')
get_ipython().magic('logon')
get_ipython().magic('logstate')
get_ipython().magic('logstart')
get_ipython().magic('logstate')
import logging

log = logging.getLogger("my-logger")
log.warning("Hello, world")
get_ipython().magic('logstop')
