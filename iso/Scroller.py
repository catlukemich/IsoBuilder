from .Input import *
from .Vector2D import *


class ScrollerConstraint:
    def constrainCenter(self, new_center_location):
        return new_center_location


class Scroller(MouseListener):
    def __init__(self, viewport, input):
        self.rmb_down = False
        self.viewport = viewport
        self.input = input
        self.scroller_constraint = ScrollerConstraint()
        pass

    def enable(self):
        self.input.addMouseListener(self)

    def disable(self):
        self.input.removeMouseListener(self)

    def setScrollerConstraint(self, constraint):
        self.scroller_constraint = constraint

    def mouseButtonDown(self, event):
        if event.num == 3:
            self.rmb_down = True
            return True

    def mouseMotion(self, event, delta_x, delta_y):
        if self.rmb_down:
            c = self.viewport.getCenter()
            c.x += 0.1 * delta_x
            c.y -= 0.1 * delta_x
            c.x += 0.1 * delta_y
            c.y += 0.1 * delta_y

            # if not self.scroller_constraint.canScrollTo(c):
            c = self.scroller_constraint.constrainCenter(c)
            self.viewport.setCenter(c)

    def mouseButtonUp(self, event):
        if event.num == 3:
            self.rmb_down = False
