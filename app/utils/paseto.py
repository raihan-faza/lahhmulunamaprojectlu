from pyseto import Key

with open("private_key.pem") as pr:
    private_key = Key.new(version=4, purpose="public", key=pr.read())

with open("public_key.pem") as pu:
    public_key = Key.new(version=4, purpose="public", key=pr.read())
