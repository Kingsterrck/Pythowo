a = input().split(" ")
res = []
b = int(float(a[0]) / 0.5)
c = int(float(a[1]) / 0.8)
d = int(float(a[2]) / 0.4)
temp1 = b*c*d
res.append(temp1)
b = int(float(a[0]) / 0.5)
c = int(float(a[2]) / 0.8)
d = int(float(a[1]) / 0.4)
temp2 = b*c*d
res.append(temp2)
b = int(float(a[1]) / 0.5)
c = int(float(a[0]) / 0.8)
d = int(float(a[2]) / 0.4)
temp3 = b*c*d
res.append(temp3)
b = int(float(a[1]) / 0.5)
c = int(float(a[2]) / 0.8)
d = int(float(a[0]) / 0.4)
temp4 = b*c*d
res.append(temp4)
b = int(float(a[2]) / 0.5)
c = int(float(a[1]) / 0.8)
d = int(float(a[0]) / 0.4)
temp5 = b*c*d
res.append(temp5)
b = int(float(a[2]) / 0.5)
c = int(float(a[0]) / 0.8)
d = int(float(a[1]) / 0.4)
temp6 = b*c*d
res.append(temp6)
print(max(res))