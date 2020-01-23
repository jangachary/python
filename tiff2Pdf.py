import natsort
import img2pdf
import glob
fils=glob.glob("E:/sriram/*.tif")
fils=natsort.natsorted(fils,reverse=False)
with open("E:/sriram/output.pdf", "wb") as f:
	f.write(img2pdf.convert(fils))
