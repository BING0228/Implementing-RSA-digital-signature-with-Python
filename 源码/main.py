import shuziqianming as qm
import argparse
def xiaoxi(xiao):
    print("对文字进行数字签名以及验证")
    print("======================================")
    print("签名：")
    #首先生成公钥与私钥
    key=qm.generatePublicAndSecretKeys()
    #公钥
    publikkey=[key["e"],key["n"]]
    print("生成的公钥为：{}".format(publikkey))
    #私钥
    privatekey=[key["d"],key["n"]]
    print("生成的私钥为：{}".format(privatekey))
    #文字的摘要
    aa=xiao
    print("签名的消息为：{}".format(aa))
    cc=aa.encode("utf-8")
    zhaiyao=qm.hashing(cc)
    print("文字的摘要为：{}".format(zhaiyao))
    print("使用私钥以及文字摘要生成签名：私钥：{}，文字摘要：{}".format(privatekey,zhaiyao))
    #文字生成的签名,使用私钥进行签名
    s=qm.signMessage(zhaiyao,privatekey[0],privatekey[1])
    print("文字生成的签名为：{}".format(s))
    print("验证：")
    print("使用公钥以及签名看生成的摘要内容是否一致：公钥：{}，签名：{}，原本的摘要：{}".format(publikkey,s,zhaiyao))
    shencheng=qm.verifySign(s,publikkey[0],publikkey[1])
    print("检验生成的消息摘要：{}".format(shencheng))
    if shencheng==zhaiyao:
        print("验证成功")
    else:
        print("验证失败")
    print("======================================")

def file(ff):
    print("对文件进行数字签名")
    print("======================================")
    print("签名：")
    #首先生成公钥与私钥
    key=qm.generatePublicAndSecretKeys()
    #公钥
    publikkey=[key["e"],key["n"]]
    print("生成的公钥为：{}".format(publikkey))
    #私钥
    privatekey=[key["d"],key["n"]]
    print("生成的私钥为：{}".format(privatekey))
    #文件的摘要
    file=open(ff,"rb")#读取文件
    cc=file.read()
    zhaiyao=qm.hashing(cc)
    print("文件的摘要为：{}".format(zhaiyao))
    print("使用私钥以及文字摘要生成签名：私钥：{}，文字摘要：{}".format(privatekey,zhaiyao))
    #文字生成的签名,使用私钥进行签名
    s=qm.signMessage(zhaiyao,privatekey[0],privatekey[1])
    print("文字生成的签名为：{}".format(s))
    print("验证：")
    print("使用公钥以及签名看生成的摘要内容是否一致：公钥：{}，签名：{}，原本的摘要：{}".format(publikkey,s,zhaiyao))
    shencheng=qm.verifySign(s,publikkey[0],publikkey[1])
    print("检验生成的消息摘要：{}".format(shencheng))
    if shencheng==zhaiyao:
        print("验证成功")
    else:
        print("验证失败")
    print("======================================")
if __name__ == '__main__':
    choices = {'xiaoxi': xiaoxi, 'file': file}
    parser = argparse.ArgumentParser(description='选择你要签名的是消息，还是文件')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-f',type=str)
    parser.add_argument('-x',type=str)
    args = parser.parse_args()
    function = choices[args.role]
    if args.role=='xiaoxi':
        function(args.x)
    else:
        function(args.f)