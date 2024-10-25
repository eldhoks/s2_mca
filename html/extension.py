filename=raw_input("enter the filename;")
if'.' in filename:
   extension=filename.split('.')[-1]
   print'the extension of the file is:', extension
else:
   print'the file has no extension'
  
