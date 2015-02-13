import sublime, sublime_plugin

class LogFilterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		s = v.sel()
		r = v.find_all(v.substr(s[0]), sublime.LITERAL)
		s.add_all(r)

		for reg in s:
			if not reg.empty():
				s.add(v.full_line(reg))

		i = len(s) - 1
		while i >= 0:
			v.erase(edit, s[i])
			i = i - 1
		s.clear()

class LogMultiFilterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		s = v.sel()
		r = sublime.Selection(66)

		for reg in s:
			r.add_all(v.find_all(v.substr(reg), sublime.LITERAL))

		s.add_all(r)

		for reg in s:
			if not reg.empty():
				s.add(v.full_line(reg))

		i = len(s) - 1
		while i >= 0:
			v.erase(edit, s[i])
			i = i - 1
		s.clear()

class LogKeepCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		s = v.sel()
		r = sublime.Selection(33)

		for reg in s:
			r.add_all(v.find_all(v.substr(reg), sublime.LITERAL))

		s.add_all(r)
		toRemove = sublime.Selection(806)
		toRemove.add(sublime.Region(0, v.size()-1))

		for reg in s:
			if not reg.empty():
				toRemove.subtract(v.full_line(reg))

		i = len(toRemove) - 1
		while i >= 0:
			v.erase(edit, toRemove[i])
			i = i - 1
		s.clear()
