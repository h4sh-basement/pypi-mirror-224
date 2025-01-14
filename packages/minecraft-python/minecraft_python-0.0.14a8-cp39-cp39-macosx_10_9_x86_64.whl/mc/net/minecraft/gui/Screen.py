from mc.net.minecraft.renderer.Tesselator import tesselator
from mc.CompatibilityShims import rshift
from pyglet import window, gl

class Screen:

    def render(self, xMouse, yMouse):
        for button in self._buttons:
            if button.visible:
                if button.enabled:
                    self._fill(button.x - 1, button.y - 1, button.x + button.w + 1, button.y + button.h + 1, 0xFF000000)
                    if xMouse >= button.x and yMouse >= button.y and xMouse < button.x + button.w and yMouse < button.y + button.h:
                        self._fill(button.x - 1, button.y - 1, button.x + button.w + 1, button.y + button.h + 1, -6250336)
                        self._fill(button.x, button.y, button.x + button.w, button.y + button.h, -8355680)
                        self.drawCenteredString(button.msg, button.x + button.w // 2, button.y + (button.h - 8) // 2, 16777120)
                    else:
                        self._fill(button.x, button.y, button.x + button.w, button.y + button.h, -9408400)
                        self.drawCenteredString(button.msg, button.x + button.w // 2, button.y + (button.h - 8) // 2, 14737632)
                else:
                    self._fill(button.x - 1, button.y - 1, button.x + button.w + 1, button.y + button.h + 1, -8355680)
                    self._fill(button.x, button.y, button.x + button.w, button.y + button.h, -7303024)
                    self.drawCenteredString(button.msg, button.x + button.w // 2, button.y + (button.h - 8) // 2, -6250336)

    def _keyPressed(self, key, modifiers, state):
        if key == window.key.ESCAPE:
            self._minecraft.setScreen(None)
            self._minecraft.grabMouse()

    def _mouseClicked(self, button):
        pass

    def init(self, minecraft, width, height):
        self._minecraft = minecraft
        self._width = width
        self._height = height
        self._buttons = []

    def _fill(self, x0, y0, x1, y1, col):
        a = rshift(col, 24) / 255.0
        r = (col >> 16 & 255) / 255.0
        g = (col >> 8 & 255) / 255.0
        b = (col & 255) / 255.0
        t = tesselator
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glColor4f(r, g, b, a)
        t.begin()
        t.vertex(x0, y1, 0.0)
        t.vertex(x1, y1, 0.0)
        t.vertex(x1, y0, 0.0)
        t.vertex(x0, y0, 0.0)
        t.end()
        gl.glDisable(gl.GL_BLEND)

    def _fillGradient(self, x0, y0, x1, y1, col1, col2):
        f9 = 96 / 255.0
        f10 = 5 / 255.0
        f11 = 5 / 255.0
        f12 = 160 / 255.0
        f6 = 48 / 255.0
        f7 = 48 / 255.0
        f8 = 96 / 255.0
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glBegin(gl.GL_QUADS)
        gl.glColor4f(f10, f11, 0.0, f9)
        gl.glVertex2f(x1, 0.0)
        gl.glVertex2f(0.0, 0.0)
        gl.glColor4f(f6, f7, f8, f12)
        gl.glVertex2f(0.0, y1)
        gl.glVertex2f(x1, y1)
        gl.glEnd()
        gl.glDisable(gl.GL_BLEND)

    def drawCenteredString(self, string, x, y, color):
        self._minecraft.font.drawShadow(string, x - self._minecraft.font.width(string) // 2, y, color)

    def drawString(self, string, x, y, color):
        self._minecraft.font.drawShadow(string, x, y, color)

    def updateEvents(self, button=None, key=None, modifiers=None, state=True):
        if button:
            xm = self._minecraft.mouseX * self._width // self._minecraft.width
            ym = self._height - self._minecraft.mouseY * self._height // self._minecraft.height - 1
            if button != window.mouse.LEFT:
                return

            for button in self._buttons:
                if xm >= button.x and ym >= button.y and xm < button.x + button.w and ym < button.y + button.h:
                    self._buttonClicked(button)
        elif key and state:
            self._keyPressed(key, modifiers, state)

    def tick(self):
        pass

    def closeScreen(self):
        pass
