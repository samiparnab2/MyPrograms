import os

def copy_file(fin_path,fout_path):
    fin=open(fin_path,'rb')
    fout=open(fout_path,'wb')
    print('coppying '+fin_path+' to '+fout_path+' -')
    total_size=os.path.getsize(fin_path)
    completed=0
    while True:
        data=fin.read(10000)
        completed+=10000
        print(round(100*(completed/total_size),2) ,' %',end='\r')
        if data==b'':
            break
        fout.write(data)
    fin.close()
    fout.close()

def copy_folder(fin_path,fout_path):
    folder_name=fin_path.split('/')[-1]
    fout_path=fout_path+'/'+folder_name
    os.mkdir(fout_path)
    files=os.popen('ls '+fin_path).read().split()
    for pth in files:
        if os.path.isdir(fin_path+'/'+pth):
            copy_folder(fin_path+'/'+pth,fout_path)
        else:
            copy_file(fin_path+'/'+pth,fout_path+'/'+pth)



f_in_path=input('enter input file path: ')
f_out_path=input('enter output file path: ')
if os.path.isdir(f_in_path):
    copy_folder(f_in_path,f_out_path)
else:
    copy_file(f_in_path,f_out_path)
