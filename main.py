from os import environ

print("Start")

a = environ.get("KANDINSKIY_API_KEY")
print(a)
if a is not None:
  print("OK")
  
print(environ.get("KANDINSKIY_SECRET_KEY"))

print("End")
