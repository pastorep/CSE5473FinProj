
class puppyMod:
  
  def __init__(self):
    puppy_pic = open("puppy.png", "rb").read()

  def response(flow):
    if flow.response.headers.get("content-type", "").startswith("image"):
      flow.response.content = puppy_pic
      flow.response.headers["content-type"] = "image/png"

addons = [
    puppyMod()
]