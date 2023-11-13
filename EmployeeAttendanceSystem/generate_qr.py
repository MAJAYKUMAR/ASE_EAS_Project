from MyQR import myqr
import os

employee_file = open('EmloyeeID.txt','r')
employee_data_from_file = employee_file.read().split("\n")

for _ in range (0,len(employee_data_from_file)):
    data = employee_data_from_file[_]
    version,level,qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture="qr_background_image.png",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(employee_data_from_file[_]+'.png'),
        save_dir=os.getcwd()
    )
