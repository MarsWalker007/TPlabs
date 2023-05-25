import turtle


def apply_rules(s, rules):
    new_s = ""
    for char in s:
        if char in rules:
            new_s += rules[char]
        else:
            new_s += char
    return new_s


def draw_l_system(t, axiom, rules, iterations, angle, length):
    sentence = axiom
    for i in range(iterations):
        sentence = apply_rules(sentence, rules)

    for char in sentence:
        if char == 'F':
            t.forward(length)
        elif char == '+':
            t.right(angle)
        elif char == '-':
            t.left(angle)


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color('blue')
t.penup()
t.goto(-200, 0)
t.pendown()

axiom = "F++F++F"
rules = {"F": "F-F++F-F"}
iterations = 4
angle = 60
length = 400 / (3 ** iterations)

for i in range(3):
    draw_l_system(t, axiom, rules, iterations, angle, length)
    t.right(120)

turtle.done()
