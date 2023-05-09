class maths:
        def sum(a,b):
            sum= float(a+b)
            return sum
        
        def minus(a,b):
            minus= float(a-b)
            return minus
        
        def mult(a,b):
            mult=float(a*b)
            return mult
        
        def div(a,b):
            div= float(a/b)
            return div 
        def  sqrr(a,b):
            b=input("how much do you want to raise to:")
            sqrr = a**b
            return sqrr 


class physics: 
    def velocity(self, distance, time):
        return (distance / time)
     
    def acceleration(self, initial_velocity, final_velocity, time):
        return (final_velocity - initial_velocity) / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def momentum(self, mass, velocity):
        return mass * velocity

    def work(self, force, distance):
        return force * distance
     
    
    


Maths = maths()

Physics = physics()

category = input("Which subject would you like to calculate - Mathematics or Physics? ")
operation = input("Which operation would you like to perform? ")

if category.lower() == "mathematics":
    if operation.lower() == "sum":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.sum(a, b)
        print("Result:", result)

    elif operation.lower() == "minus":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.minus(a, b)
        print("Result:", result)

    elif operation.lower() == "mult":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.mult(a, b)
        print("Result:", result)

    elif operation.lower() == "div":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = mathematics.div(a, b)
        print("Result:", result)

    elif operation.lower() == "sqrr":
        a = float(input("Enter base number: "))
        b = float(input("Enter exponent: "))
        result = mathematics.sqrr(a, b)
        print("Result:", result)

    else:
        print("Invalid operation selected.")

elif category.lower() == "physics":
    if operation.lower() == "velocity":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        result = physics.velocity(distance, time)
        print("Result:", result)

    elif operation.lower() == "acceleration":
        initial_velocity = float(input("Enter initial velocity: "))
        final_velocity = float(input("Enter final velocity: "))
        time = float(input("Enter time: "))
        result = physics.acceleration(initial_velocity, final_velocity, time)
        print("Result:", result)
    elif operation.lower() == "force":
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        result = physics.force(mass, acceleration)
        print("Result:", result)

    elif operation.lower() == "momentum" :
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        result = physics.momentum(mass, velocity)
        print("Result:", result)

    elif operation.lower() == "work":
        force = float(input("Enter force: "))
        distance = float(input("Enter distance: "))
        result = physics.work(force, distance)
        print("Result:", result)

    else:
        print("Invalid operation selected.")

else:
    print("Invalid category selected.")