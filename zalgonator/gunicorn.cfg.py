import os
from distutils.util import strtobool

bind = os.environ.get('GUNICORN_BIND', 'unix:/tmp/gunicorn.sock')
backlog = 128
workers = os.environ.get('GUNICORN_WORKERS', 1)
timeout = 30
keepalive = 2

# spew - Install a trace function that spews every line of Python
#        that is executed when running the server.

spew = os.environ.get('GUNICORN_SPEW', False)
# Restart server on source change, useful for development (requires source folder to be mounted in the container)
reload = bool(strtobool(os.environ.get('GUNICORN_AUTORELOAD', '0')))
daemon = False
pidfile = os.environ.get('GUNICORN_PID', '/var/run/gunicorn.pid')

errorlog = os.environ.get('GUNICORN_ERR_LOG', '-')
loglevel = os.environ.get('GUNICORN_LOG_LEVEL', 'info')
accesslog = os.environ.get('GUNICORN_ACCESS_LOG', '-')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Server hooks

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    pass


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    # # get traceback info
    # import threading
    # import sys
    # import traceback
    # id2name = {th.ident: th.name for th in threading.enumerate()}
    # code = []
    # for threadId, stack in sys._current_frames().items():
    #     code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""), threadId))
    #     for filename, lineno, name, line in traceback.extract_stack(stack):
    #         code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
    #         if line:
    #             code.append("  %s" % (line.strip()))
    # worker.log.debug("\n".join(code))


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")