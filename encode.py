import glob
file_name = glob.glob('out/piano/*_1.mid')[0]
import base64
with open(file_name, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
header = 'data:audio/mid;base64,'
file_rep = header+encoded_string.decode('utf-8')
with open("/var/www/html/midi/file_rep.txt", "w") as f:
    f.write(file_rep)