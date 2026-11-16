class Particle:
    def __init__(self, mass, positionx, positiony, velocityx, velocityy):
        self.mass = mass
        self.positionx = positionx
        self.positiony = positiony
        self.velocityx = velocityx
        self.velocityy = velocityy
    def speed(self):
        return (self.velocityx ** 2 + self.velocityy ** 2) ** .5
    def kinetic_energy(self):
        return self.mass * .5 * (self.velocityx ** 2 + self.velocityy ** 2)
    def move(self, t):
        self.positionx = self.positionx + t * self.velocityx
        self.positiony = self.positiony + t * self.velocityy
    def __repr__(self):
        return (f"Particle(x = {self.positionx}, y = {self.positiony})")

def collision(p1, p2):
    momentumx = p1.mass * p1.velocityx + p2.mass * p2.velocityx
    momentumy = p1.mass * p1.velocityy + p2.mass * p2.velocityy
    totalmass = p1.mass + p2.mass
    newvelocityx = momentumx / totalmass
    newvelocityy = momentumy / totalmass
    return (newvelocityx, newvelocityy)



    
p1 = Particle(2, 0, 0, 3, 4)   # mass, x, y, vx, vy
p2 = Particle(2, 0, 0, -6, -8)

print(p1.speed())            # 5.0
print(p1.kinetic_energy())   # 25.0
p1.move(2)
print(p1)                    # Particle(x=6, y=8)
p1.move(1)
print(p1)                    # Particle(x=9, y=12)
print(collision(p1, p2))