aclNum = int(input("What is the IPv4 ACL number?"))

if aclNum >=1 and aclNum<=99:
    print("This is a stamdard IPv4 ACL.")
elif aclNum >=100 and aclNm <= 199:
    print("This is a extended IPv4 ACL.")
else:
    print("Thi is not a standard or extended IPc4 ACL.SS");