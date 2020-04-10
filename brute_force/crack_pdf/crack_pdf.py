import subprocess

FILENAME = 'cadeado.pdf'

output = 'decrypted_' + FILENAME
for i in range(999):
    password = "%03d" % i
    print("Trying password '%s'... " % password, end='')
    try:
        py2output = subprocess.check_output(['qpdf', '--password='+password, '--decrypt', FILENAME, output])
        print("Success!")
        break
    except:
        print("Failed!")

