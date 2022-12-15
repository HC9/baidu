from settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*ual((asdf%wt%5_ara^*f5@%3234&8&gr=fg)^b&c@ioqdkekdtmb5v2i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

# The URL of the LDAP server(s).  List multiple servers for high availability ServerPool connection.
LDAP_AUTH_URL = ["ldap://42.193.153.112:389"]

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "dc=ihopeit,dc=com"

# The LDAP username and password of a user for querying the LDAP database for user
# details. If None, then the authenticated user will be used for querying, and
# the `ldap_sync_users`, `ldap_clean_users` commands will perform an anonymous query.
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "rgJGQCJFa9aeSGTfOQu7"
