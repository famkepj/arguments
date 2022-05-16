# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet (name, greeting = 'Hello, <name>!'):
    return greeting.replace('<name>', name)

print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))

def force(mass, body='earth'):
    surface_gravity = dict(
        sun= 274,
        jupiter= 24.9,
        neptune= 11.2,
        saturn=	10.4,
        earth= 9.8,
        uranus=	8.9,
        venus= 8.9,
        mars= 3.71,
        mercury= 3.7,
        moon= 1.6,
        pluto= 0.6
    )

    gravity = surface_gravity[body]
    return mass * gravity

print(force(10, 'moon'))

def pull(m1, m2, d):
    return (6.674* 10**-11) * ((m1 * m2)/d**2)

print(pull(0.1, 5.972*10**24, 6.371*10**6))
