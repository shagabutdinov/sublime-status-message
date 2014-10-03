import sublime
import sublime_plugin
from StatusMessage import status_message

class ShowScopeNameEnhanced(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.sel()) == 0:
      return

    message = self.view.scope_name(self.view.sel()[0].b)
    status_message.set(self.view, 'scope_name', '◍' + message, 5000)

class ToggleDefaultStatus(sublime_plugin.TextCommand):
  def run(self, edit):
    status_message.hide_default_status = not status_message.hide_default_status
    status_message.refresh(self.view)