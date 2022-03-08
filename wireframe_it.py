import glob
import shutil
import os

src_file = "placeholder.jpg"
#dst = "RNIB - See differently -_files"
name = "Welcome to the British Heart Foundation"
#name = "The Chesterfield Canal Trust - Help to restore the last nine miles"

dst =  name+"_files"
htmlfile= name+".html"

def placehold (dst_dir, ext):
    dst_paths = os.path.join(dst_dir,"*."+ext)
    print("dst_paths", dst_paths)
    for imgfile in glob.iglob(dst_paths):
        print ("imgfile", imgfile)
        shutil.copyfile("placeholder."+ext , imgfile)


placehold(dst, "svg")
placehold(dst, "jpg")
placehold(dst, "png")

from bs4 import BeautifulSoup
import re
from bs4.diagnose import diagnose

with open(htmlfile, 'r', encoding='utf-8') as fp:
    data = fp.read()
#diagnose(data)
soup = BeautifulSoup(data)
headings = soup.find_all(re.compile("^h[1-6]"))

for heading in headings :
    print(heading.stripped_strings)
#print(headings)