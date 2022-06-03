options = """1. Right triangle, 2. Equilateral triangle, 3.Rhombus, 4. Square, 5. Rectangle"""
choice = int(input(f"What geographical shape do you want? \n{options} "))
x = input()
x = x + "  "

def draw_rightTriangle():
    print(f"""
{x}
{x}{x}
{x}   {x}
{x}      {x}
{x}{x}{x}{x}{x}""")
def draw_equilateralTriangle():
    print(f"""      
      {x}
    {x} {x}
  {x}     {x}
{x}{x}{x}{x}{x}""")
def draw_rhombus():
    print(f"""      
      {x}
    {x} {x}
  {x}     {x}
{x}{x}{x}{x}{x}
  {x}     {x}    
    {x} {x}
      {x}      """)
def draw_square():
    print(f"""{x}{x}{x}{x}
{x}{x}{x}{x}
{x}{x}{x}{x}
{x}{x}{x}{x}""")
def draw_rectangle():
    print(f"""
{x}{x}{x}{x}{x}
{x}{x}{x}{x}{x}
{x}{x}{x}{x}{x}
{x}{x}{x}{x}{x}""")
if choice == 1:
    draw_rightTriangle()
elif choice == 2:
    draw_equilateralTriangle()
elif choice == 3:
    draw_rhombus()
elif choice == 4:
    draw_square()
elif choice == 5:
    draw_rectangle()