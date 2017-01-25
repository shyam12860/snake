class Snake(object):

    def __init__(self):
        self.x = 2 
        self.y = 0
        self.dx = 1
        self.dy = 0
        self.body = [(0,0), (1,0), (2, 0)] 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        del self.body[0]

        if (self.x, self.y) in self.body:
            return False
        self.body.append((self.x, self.y))
        return True

    def grow(self):
        if len(self.body) == 1:
            self.body.insert(0, (self.x - self.dx, self.y - self.dy))
        else:
            dir_x = self.body[0][0] - self.body[1][0]
            dir_y = self.body[0][1] - self.body[1][1]
            self.body.insert(0, (self.body[0][0] + dir_x, self.body[0][1] + dir_y))
