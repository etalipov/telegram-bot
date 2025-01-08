from os import environ

print("Start")

a = environ.get("KANDINSKIY_API_KEY")
print(type(a))
  
print(environ.get("KANDINSKIY_SECRET_KEY"))

print("End")
