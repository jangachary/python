
import img2pdf
import glob
#this code converts tiff images into pdf using img2pdf(https://pypi.org/project/img2pdf/) library 
files=glob.glob("E:/sriram/*.tif")
with open("E:/sriram/output.pdf", "wb") as f:
	f.write(img2pdf.convert(files))
