import sublime
import sublime_plugin
from StatusMessage import status_message

class DefaultStatus(sublime_plugin.EventListener):
  def on_selection_modified_async(self, view):
    self._set_status(view)

  def on_activated_async(self, view):
    self._set_status(view)

  def _set_status(self, view):
    selections = view.sel()

    if len(selections) != 1:
      message = '☰' + str(len(selections))
    else:
      selection = selections[0]
      if selection.empty():
        row, col = view.rowcol(selections[0].b)
        message = 'λ' + str(row + 1) + ':' + str(col + 1)
      else:
        message = '#' + str(selection.size())

    # prevent message jumping when navigating over text
    message = message.ljust(10)

    # _ - is very first position
    status_message.set(view, '_', message)