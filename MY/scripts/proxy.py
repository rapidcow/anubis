# https://docs.mitmproxy.org/stable/addons/options/
def request(flow):
    # flow:    mitmproxy.flow.Flow
    # client:  mitmproxy.connection.Client
    # peername: (host: str, port: int)
    flow.request.headers["X-Real-IP"] = flow.client_conn.peername[0]
    flow.request.headers["X-Forwarded-For"] = flow.client_conn.peername[0]
    with open('dada.txt', 'a') as out:
        print(repr(flow), file=out)
