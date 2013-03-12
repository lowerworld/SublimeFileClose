import sublime_plugin

class FileClose(sublime_plugin.WindowCommand):
    def _close(self, command):
        active_view = self.window.active_view()
        if active_view:
            self.window.run_command(command, dict(zip(('group', 'index'), self.window.get_view_index(active_view))))

class FileCloseOthers(FileClose):
    def run(self):
        self._close('close_others_by_index')

class FileCloseToRight(FileClose):
    def run(self):
        self._close('close_to_right_by_index')
