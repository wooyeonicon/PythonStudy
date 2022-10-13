# 作者 : 杨航
# 开发时间 : 2022/4/11 20:34
# 字符串的编码和解码
print('===编码====')
s='天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK的编码中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8编码中，一个中文占3个字节

print('===解码===')
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
