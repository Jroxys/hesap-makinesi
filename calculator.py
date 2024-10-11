def topla(say1,say2):
    print('Sayıların toplamı:', say1+say2)
def cikar(say1,say2):
    print('Sayıları çıkartımı:', say1-say2)
def bol(say1,say2):
    print('Sayıların bölümü:', say1//say2)
def carp(say1,say2):
    print('Sayıların çarpımı:', say1*say2)




menu ="""
    Hesap Makinesine hoş geldiniz:
    
    1-Topla
    2-Çıkart
    3-Böl
    4-Çarp
    5-Çıkış
    """




while True:
    print(menu)
    say1 = eval(input('Birinci sayıyı giriniz : '))
    say2 = eval(input('İkinci sayıyı giriniz : '))
    print('-'*50)
    secim = input('Yapmak istediğiniz işlemi seçiniz.(1,2,3,4,5): ')
    if secim == '1':

            print('-'*50)
            topla(say1,say2)
            print('-'*50)
    elif secim == '2':
            print('-'*50)   
            cikar(say1,say2)
            print('-'*50)
    elif secim == '3':
            print('-'*50)
            bol(say1,say2)
            print('-'*50)
    elif secim == '4':
            print('-'*50)
            carp(say1,say2)
            print('-'*50)
    elif secim == '5':
            quit()
    else:
            input('Yanlış seçim yaptınız lütfen verilen değerlerden birini giriniz.')
            

    
 