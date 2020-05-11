import zlib
string = 'hello world!hello world!hello world!hello world!hello world!'

comp = zlib.compress(string)
print(zlib.decompress(comp))