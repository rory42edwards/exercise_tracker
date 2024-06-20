import multiprocessing

bind = '127.0.0.1:8000'

workers = multiprocessing.cpu_count() * 2 + 1

threads = 2

backlog = 2048

timeout = 30

accesslog = '-'

errorlog = '-'

loglevel = 'info'

daemon = False
