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
    
    
p = Particle(2, 0, 0, 3, 4)   # mass, x, y, vx, vy

print(p.speed())            # 5.0
print(p.kinetic_energy())   # 25.0
p.move(2)
print(p)                    # Particle(x=6, y=8)
p.move(1)
print(p)                    # Particle(x=9, y=12)