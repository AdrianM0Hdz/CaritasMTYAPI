import ssl
import os
import gunicorn
from dotenv import load_dotenv
load_dotenv(override=True)

from src.infrastructure.create_app import create_app

import pyodbc 
print(pyodbc.drivers())

app = create_app()

@app.after_request
def add_header(r):
    import secure
    secure_headers = secure.Secure()
    secure_headers.framework.flask(r)
    r.headers['X-Frame-Options'] = 'SAMEORIGIN' # ya lo llena 'secure'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Content-Security-Policy"] = "default-src 'none'"
    r.headers["Content-Type"] = "application/json"
    r.headers["Content-Security-Policy"] = "default-src 'self'"
    return r

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(os.environ["API_CERT"], os.environ["API_KEY"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=context, debug=True)
