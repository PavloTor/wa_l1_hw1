###### Read device from file and append to list ######
devices = []
file = open("devices.txt", "r")

for item in file:
    item = item.strip()
    devices.append(item)

file.close
print(devices)
