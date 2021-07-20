"""
-upload / download / show files
simple script to control your account through the terminall
Author : safou abderrahim
sdk : dropbox sdk
"""
from os import system
from sys import exit

#inspired from razewerz assist
try:
	import dropbox
except:
	system('pip install dropbox')
#end inspiration

TOKEN = 'your token'
dbx = dropbox.Dropbox(TOKEN)


def show_files():
	count = 1
	print("\nshowing files...")
	for entry in dbx.files_list_folder('').entries:
		print(f"""File [{count}] | File name : '{entry.name}'
         | Last modified date : {entry.server_modified}
         | File size : {entry.size} bytes\n""")
		count += 1


def upload():
	filename = input("\nEnter File name:")
	with open(filename ,"rb") as f :
		filename = '/' + filename
		dbx.files_upload(f.read(),filename)
	print("Done!")

def download():
	count = 1
	files = []
	for entry in dbx.files_list_folder('').entries:
		files.append(entry.name)
		print(f" [ {count} ] : {entry.name}")
		count += 1

	file_number = int(input("Enter file number to download :")) - 1
	dbx.files_download_to_file(files[file_number] ,'/'+files[file_number])
	print("[✓] Downloaded")


def exit_or_continue():
	user_choice = input("back to main [y/n]? :")
	if user_choice == 'y' :
		return True
	else :
		exit("closing...")

while True :
	inp = int(input("1)show files \n2)upload file \n3)download file\n what is your next step? :"))
	if inp == 1 :
		show_files()
		exit_or_continue()
	elif inp == 2 :
		upload()
		exit_or_continue()
	elif inp == 3 :
		download()
		exit_or_continue()
	else :
		print("[!] invalid input")
		exit_or_continue()
