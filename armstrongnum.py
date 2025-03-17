x=int(input())
y=int(input())
z=int(input())
u=int(str(x)+str(y)+str(z))
v=x**3+y**3+z**3
if u==v:
  print("armstrong number")
else:
  print("not armstrong number")