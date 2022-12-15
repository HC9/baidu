from settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*ual((sk%wt%5_ara^*f5@%45&8&gr=fg)^b&c@ioqbtmb5v2i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# The URL of the LDAP server(s).  List multiple servers for high availability ServerPool connection.
LDAP_AUTH_URL = ["ldap://42.193.153.112:389"]

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "dc=ihopeit,dc=com"

# The LDAP username and password of a user for querying the LDAP database for user
# details. If None, then the authenticated user will be used for querying, and
# the `ldap_sync_users`, `ldap_clean_users` commands will perform an anonymous query.
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "rgJGQCJFa9aeSGTfOQu7"

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]

DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=bc7c80fd5f46bc44131734ce2f9cf6af3b3da922adc2c49d95af426dc83b6782"
DINGTALK_SECRET = "SEC845b355b963e2b157a6978e1b7c5927535da49b05f070c9a21057a1f95c45a79"
