acl= int (input("what is the IPv4 ACL number"))

if acl<=1 and acl <=99:

    print("this is the standard IPv4 acl.")

elif acl >=100 and acl <= 199:

    print("this a extended IPv4 ACL.")
else:

    print("this is not a standard or extended IPv4 ACL")