# Sublime StatusMessage plugin

Glorious plugin that replaces default (ugly) sublime status bar and makes it a
bit nicer (with icons). Works great together with
[sublime-shell-status](http://github.com/shagabutdinov/sublime-shell-status)
plugin.


### Demo

![Notebook screenshot](https://raw.github.com/shagabutdinov/sublime-status-message/master/screenshot.png)

This is sublime running on my laptop. It's always employs as much space as
possible that is why there is time (ω) and battery charge (do not displayed on
screenshot) are showed in status bar panel.


### WARNING

It disable some default status messages (window-status messages) and sublimes
default status messages. In order to see all status messages you should use
keyboard hotkey.

Some icons used in status bar (e.g. battery "🔋", search "🔎" or star "✱") will
result text padding so lowest pixel row of text (including underscores "_") will
not be visible. It is really annoying bug and if you have an workaround please
tell me it.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

Replaces default status bar with a bit nicer one. Provides API for other plugins
to make nice status bar output.


### Commands

| Description           | Keyboard shortcut | Command palette                       |
|-----------------------|-------------------|---------------------------------------|
| Show scope name       | ctrl+u, ctrl+\    | StatusMessage: Show scope name        |
| Toggle default status | ctrl+u, ctrl+y    | StatusMessage: Toggle default status  |


### API

Methods are located under "StatusMessage.status_message" ("from StatusMessage
import status_message"):


##### set(view, key, message, timeout = None)

Set status message to view.

Arguments:

  - view - view to set message

  - key - unique id of message; message could be erased or resetted by this key

  - message - message to be setted

  - timeout - number of milliseconds after which message will be erased;
    None - never erase


##### get(view, key)

Get status message from view.

Arguments:

  - view - view to set message

  - key - unique id of message


##### erase(view, key)

Erase status message from view.

Arguments:

  - view - view to set message

  - key - unique id of message


##### get_all(view)

Get all statuses from view that were setted through this plugin. Returns dict
(key: message). Modifying this dict and issuing "refresh" command will result
modifying status bar messages.


##### refresh(view)

Refresh view status bar.