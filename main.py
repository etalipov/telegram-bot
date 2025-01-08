from os import environ

print("Start")

a = environ.get("KANDINSKIY_API_KEY")
print(a)
  
print(environ.get("KANDINSKIY_SECRET_KEY"))
print(environ.get("TEST"))

print("End")
