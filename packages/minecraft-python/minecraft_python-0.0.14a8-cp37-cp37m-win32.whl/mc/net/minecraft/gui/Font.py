from mc.net.minecraft.renderer.Tesselator import tesselator
from mc import Resources
from pyglet import gl

class Font:

    def __init__(self, name, textures):
        self.__charWidths = [0] * 256
        self.__fontTexture = textures.loadTexture(name, gl.GL_NEAREST)
        texture = Resources.textures[name]
        w = texture[0]
        h = texture[1]
        rawPixels = texture[2]

        for i in range(128):
            xt = i % 16
            yt = i // 16

            emptyColumn = False
            for x in range(8):
                if emptyColumn:
                    break
                xPixel = (xt << 3) + x
                emptyColumn = True
                for y in range(8):
                    if not emptyColumn:
                        break
                    yPixel = ((yt << 3) + y) * w
                    pixel = rawPixels[xPixel + yPixel] & 255
                    if pixel > 128:
                        emptyColumn = False
            if i == 32:
                x = 4
            self.__charWidths[i] = x

    def drawShadow(self, string, x, y, color):
        self.draw(string, x + 1, y + 1, color, True)
        self.draw(string, x, y, color)

    def draw(self, string, x, y, color, darken=False):
        if darken:
            color = (color & 0xFCFCFC) >> 2
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.__fontTexture)
        t = tesselator
        t.begin()
        t.color(color)
        xo = 0
        for i in range(len(string)):
            char = string[i]
            if char == '&':
                cc = '0123456789abcdef'.index(string[i + 1])
                br = ((cc & 8) * 8) << 3
                b = (cc & 1) * 191 + br
                g = ((cc & 2) >> 1) * 191 + br
                r = ((cc & 4) >> 2) * 191 + br
                color = r << 16 | g << 8 | b
                i += 2
                if darken:
                    color = (color & 0xFCFCFC) >> 2
                t.color(color)

            ix = ord(char) % ord('\020') << 3
            iy = ord(char) // ord('\020') << 3
            t.vertexUV(x + xo, y + 8, 0.0, ix / 128.0, (iy + 8) / 128.0)
            t.vertexUV(x + xo + 8, y + 8, 0.0, (ix + 8) / 128.0, (iy + 8) / 128.0)
            t.vertexUV(x + xo + 8, y, 0.0, (ix + 8) / 128.0, iy / 128.0)
            t.vertexUV(x + xo, y, 0.0, ix / 128.0, iy / 128.0)

            xo += self.__charWidths[ord(char)]

        t.end()
        gl.glDisable(gl.GL_TEXTURE_2D)

    def width(self, string):
        if string is None:
            return 0
        else:
            length = 0
            for i, char in enumerate(string):
                if char != '&':
                    length += self.__charWidths[ord(char)]

            return length
