'''Ini merupakan satu program ringkas untuk mendapatkan isipadu kuboid'''
pi=3.142
def kira_kuboid(tinggi,panjang,lebar):
    isipadu_kuboid=tinggi*panjang*lebar
    return isipadu_kuboid
    
def kuboid(): #Isipadu kuboid
    tinggi=float(input("Masukkan tinggi: "))
    panjang=float(input("Masukkan panjang: "))
    lebar=float(input("Masukkan lebar: "))
    print("Isipadu kuboid=",kira__kuboid(tinggi,panjang,lebar))
    
def kira_silinder(pi,jejari,tinggi):
    isipadu_silinder=pi*(jejari**2)*(tinggi)
    return isipadu_silinder
    
def silinder(): #Isipadu silinder 
    jejari=int(input("Masukkan jejari: "))
    tinggi=int(input("Masukkan tinggi: "))
    print("Isipadu silinder=",kira_silinder(pi,jejari,tinggi))
    
def kira_kon(pi,jejari,tinggi):
    isipadu_kon=(1/3)*pi*(jejari**2)*(tinggi)
    return isipadu_kon
    
def kon(): #Isipadu kon
    jejari=float(input("Masukkan jejari: "))
    tinngi=float(input("Masukkan tinggi: "))
    print("Isipadu kon=",kira_kon(pi,jejari,tinngi))
    
def kira_sfera(pi,jejari):
    isipadu_sfera=4/3*pi*(jejari**3)
    return isipadu_sfera
    
def sfera(): #Isipadu sfera
    jejari=float(input("Masukkan jejari: "))
    print("Isipadu sfera=",kira_sfera(pi,jejari))
    
###################
#Subatur cara utama
###################

ulang=True

while(ulang):
    print(
    '''
    MENGIRA ISI PADU
    1.Kuboid
    2.Silinder
    3.Kon
    4.Sfera
    5.keluar dari program''')
    print("")
    
    pilih=int(input("Sila masukkan pilihan anda : "))
    
    if(pilih==1):
       kuboid()    #memanggil fungsi kuboid
    elif(pilih==2):
       silinder()  #memanggil fungsi silinder
    elif(pilih==3):
       kon()       #memanggil fubgsi kon
    elif(pilih==4):
       sfera()     #memanggil fungsi sfera
    elif(pilih==5):
         ulang=False
         print("Good Bye")
    else:
         print("Pilihan tiada dalam senarai")
         print("")