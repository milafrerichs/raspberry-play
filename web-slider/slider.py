#!/usr/bin/env python

from webserver import TornadoWebServer
from sharedvalue import SharedValueHandler

def main():
  webserver = TornadoWebServer(port=8888, debug=True)
  webserver.static_files('/static/', 'static')
  webserver.websocket('/slider-value', SharedValueHandler(0, on_change=slider_updated))
  print 'Listening on %s' % webserver.url
  webserver.run()

def slider_updated(value, connection):
  print 'Slider value: ', value

if __name__ == '__main__':
  main()

