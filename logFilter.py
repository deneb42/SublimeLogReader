import sublime, sublime_plugin


class LogFilterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view ## toto
		s = v.sel()## toto
		r = []	## toto

		for reg in s:
			r.extend(v.find_all(v.substr(reg), sublime.LITERAL))

		for reg in r:
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
		r = []

		for reg in s:
			r.extend(v.find_all(v.substr(reg), sublime.LITERAL))
		for i in range(len(r)):
			r[i] = v.full_line(r[i])

		i = 0
		while i < len(r) - 1:
			if r[i].end() == r[i+1].begin():
				r[i] = sublime.Region(r[i].begin(), r[i+1].end())
				del r[i+1]
			else:
				i = i + 1


		s.add(sublime.Region(0, v.size()-1))
		for reg in r:
			s.subtract(reg)

		i = len(s) - 1
		while i >= 0:
			v.erase(edit, s[i])
			i = i - 1
		s.clear()
