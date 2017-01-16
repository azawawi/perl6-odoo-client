import jsonrpclib

HOST = "localhost"
PORT = 8069
DB   = "sample"
USER = "user@example.com"
PASS = "123"

# server proxy object
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
server = jsonrpclib.Server(url)

version = server.call(service="common", method="version", args=[])
print(version)

# log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])

# helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    print("args = %s" % args)
    return server.call(service="object", method="execute", args=args)

user_ids = invoke('res.users', 'search', [])
print(user_ids)

user = invoke('res.users', 'read', [1]);
print(user)
