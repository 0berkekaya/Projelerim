import os
import os.path
import json
import rsa

publicKey, privateKey = rsa.newkeys(1024)


def FileFeature():
    fileName = 'password'
    fileType = 'berke'
    return str(fileName + "." + fileType)


def FileControl(fileFeature):
    return os.path.exists(fileFeature)


def AccountWrite():
    company = input("Firma Adı Giriniz : ")
    username = input("Kullanıcı Adı Giriniz : ")
    password = input("Şifre Giriniz : ")

    x = {''+company+'': {''+username+'': ''+password+''}}

    print(x)

    file = open(FileFeature(), mode='a', encoding='utf-8')

    file.write(FileEncryption(x)+"\n")

    file.close()


def AccountsRead():
    # whoAccount = str(input("Kullanıcı Adı Giriniz : "))

    file = open(FileFeature(), mode='r', encoding='utf-8')

    for x in file.readlines():
        FileDecryption(x)

    """ for x in file.readlines():
        for key, value in ast.literal_eval(x).items():
            print(value.keys()) """


def FileEncryption(message):

    return rsa.encrypt(message.encode(), publicKey)


def FileDecryption(message):

    decMessage = rsa.decrypt(bytes(message, 'utf-8'), privateKey).decode()

    print("decrypted string: ", decMessage)


if FileControl(FileFeature()):
    print("Dosya Mavcut.")

    AccountWrite()

else:
    print("Dosya Yok")

    berke = open(FileFeature(), mode='x')

    if os.path.isfile(FileFeature()) & os.access(FileFeature(), os.R_OK):
        print("Dosya Oluşturma Başarılı :)")

    else:
        print("Dosya Oluşturulamadı. Lütfen programı kapatıp açınız !")
