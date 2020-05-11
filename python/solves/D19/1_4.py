subject = ["I","you"]
verbs = ["Play","love"]
objects = ["Hockey","Football"]


for sub in subject:
    for v in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,v,obj))