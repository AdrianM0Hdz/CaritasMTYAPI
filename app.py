import os
import gunicorn
from dotenv import load_dotenv
load_dotenv(override=True)

from src.infrastructure.create_app import create_app

import pyodbc 
print(pyodbc.drivers())

# # Remove 'Server' from header
# from gunicorn.http import wsgi
# class Response(wsgi.Response):
#     def default_headers(self, *args, **kwargs):
#         headers = super(Response, self).default_headers(*args, **kwargs)
#         return [h for h in headers if not h.startswith('Server:')]
# wsgi.Response = Response

app = create_app()

@app.after_request
def add_header(r):
    import secure
    secure_headers = secure.Secure()
    secure_headers.framework.flask(r)
    #r.headers['X-Frame-Options'] = 'SAMEORIGIN' # ya lo llena 'secure'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Content-Security-Policy"] = "default-src 'none'"
    r.headers["Content-Type"] = "application/json"
    r.headers["Content-Security-Policy"] = "default-src 'self'"
    return r

API_CERT = 'C:/Users/jaime/OneDrive/Documentos/GitHub/ReposTec/CaritasMTYAPI/equipo04.tc2007b.tec.mx.cer'
API_KEY = 'C:/Users/jaime/OneDrive/Documentos/GitHub/ReposTec/CaritasMTYAPI/equipo04.tc2007b.tec.mx.key'

if __name__ == '__main__':
    import ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(API_CERT, API_KEY)
    app.run(host='0.0.0.0', port=5000, ssl_context=context, debug=True)
