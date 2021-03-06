from flask import Flask
import logging
import sys

# imported ddtrace modules
from ddtrace import tracer
from ddtrace.contrib.flask import TraceMiddleware

tracer.configure(hostname='127.0.0.1') # configured for localhost as lazy

# Have flask use stdout as the logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)
c = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c.setFormatter(formatter)
main_logger.addHandler(c)

app = Flask(__name__)
traced_app = TraceMiddleware(app, tracer, service='AndyTestApp') ## added this with an app name

@app.route('/')
def api_entry():
    return 'Entrypoint to the Application'

@app.route('/api/apm')
def apm_endpoint():
    return 'Getting APM Started'

@app.route('/api/trace')
def trace_endpoint():
    return 'Posting Traces'

if __name__ == '__main__':
    app.run(port=9999) ## changed this port number as conflict with another port
