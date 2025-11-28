x = input("File name: ")
x = x.strip().lower()
def check(a):
   return x.endswith(a)

if check(".gif"):
    print("image/gif")
elif check(".jpg") or check(".jpeg"):
    print("image/jpeg")
elif check(".png"):
    print("image/png")
elif check(".pdf"):
    print("application/pdf")
elif check(".txt"):
    print("text/plain")
elif check(".zip"):
    print("application/zip")
elif check(".bin"):
    print("application/octet-stream")
else:
    print("application/octet-stream")

