import sublime
import sublime_plugin
import os
import subprocess

hide_default_status = True
erases = {}
class EraseByTimeout():
  def __init__(self, view, key, timeout):
    self.disabled = False

    self.view = view
    self.key = key
    sublime.set_timeout(self._erase, timeout)

    global erases
    if key in erases:
      erases[key].disabled = True

    erases[key] = self

  def _erase(self):
    if self.disabled:
      return

    erase(self.view, self.key)

    global erases
    erases.pop(self.key, None)

statuses = {}

def get_all(view):
  if view == None:
    id = 0
  else:
    id = view.id()

  global statuses
  if not id in statuses:
    statuses[id] = {}

  return statuses[id]

def refresh(view):
  result = []
  statuses = get_all(view)
  for key in sorted(statuses):
    if statuses[key].strip() == '':
      continue

    result.append(statuses[key])

  # 'z' * 100 - is very last position
  status = "\t\t".join(result)
  global hide_default_status
  if hide_default_status:
    status += "\0"

  view.set_status('z' * 100, status)

def set(view, key, message, timeout = None):
  if message == '':
    return erase(view, key)

  get_all(view)[key] = message
  refresh(view)

  if timeout != None:
    EraseByTimeout(view, key, timeout)

def get(view, key):
  return get_all(view).get(key, None)

def erase(view, key):
  get_all(view).pop(key, None)
  refresh(view)