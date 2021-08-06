from org.transcrypt.stubs.browser import *
import time

class AnswerTime:
	def __init__(self, question_id):
		self.id = question_id
		self.start = time.time()
		self.end = -1

	@property
	def elapsedtime(self):
		if self.end == -1:
			self.stop()
		return int(self.end - self.start)

	def restart(self, question_id):
		self.id = question_id
		self.start = time.time()

	def stop(self):
		self.end = time.time()
	

class Records:
	def __init__(self):
		self.items = {}

	def start_timer(self, question_id):
		self.items[question_id] = AnswerTime(question_id)

	def stop_timer(self, form_id, question_id):
		self.items[question_id].stop()
		curform = document.getElementById("form-{}".format(form_id))
		answer = curform.elements["answer"].value
		curform.elements["challenge_id"].value = str(question_id)
		curform.elements["elapsed_time"].value = self.items[question_id].elapsedtime
		curform.submit()


	def get_elapsedtime(self, question_id):
		return self.items[question_id].elapsedtime

records = Records()
