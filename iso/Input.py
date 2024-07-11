from .Vector2D import Vector2D


class Input:
	def __init__(self):
		self.key_listeners   = []
		self.mouse_listeners = []
		self.mouse_position = None

		
	def addMouseListener(self, listener):
		self.mouse_listeners.append(listener)


	def addKeyboardListener(self, listener):
		self.key_listeners.append(listener)


	def removeMouseListener(self, listener):
		self.mouse_listeners.remove(listener)


	def removKeyboardListener(self, listener):
		self.key_listeners.remove(listener)


	def mouseButtonDown(self, event):
		for listener in self.mouse_listeners:
			consumed = listener.mouseButtonDown(event)
			if consumed:
				break


	def mouseWheel(self, event):
		for listener in self.mouse_listeners:
			consumed = listener.mouseWheel(event)
			if consumed:
				break


	def mouseButtonUp(self, event):
		for listener in self.mouse_listeners:
			consumed = listener.mouseButtonUp(event)
			if consumed:
				break


	def mouseMotion(self, event):
		new_mouse_pos = Vector2D(event.x, event.y)
		if self.mouse_position != None:
			delta = new_mouse_pos - self.mouse_position
		else:
			delta = Vector2D()
		self.mouse_position = new_mouse_pos

		for listener in self.mouse_listeners:
			consumed = listener.mouseMotion(event, delta.x, delta.y)
			if consumed:
				break


	def keyDown(self, event):
		for listener in self.key_listeners:
			consumed = listener.keyDown(event)
			if consumed:
				break


	def keyUp(self, event):
		for listener in self.key_listeners:
			consumed = listener.keyUp(event)
			if consumed:
				break


class MouseListener:
	def mouseButtonDown(self, event):
		pass


	def mouseButtonUp(self, event):
		pass


	def mouseMotion(self, event, delta_x, delta_y):
		pass


	def mouseClick(self, event):
		pass


	def mouseWheel(self, event):
		pass


class KeyboardListener:
	def keyDown(self, event):
		pass

	def keyUp(self, event):
		pass

