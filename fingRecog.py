#pip install PyFingerprint
from pyfingerprint.pyfingerprint import PyFingerprint

# Initialize the fingerprint sensor
f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

if not f.verifyPassword():
    raise ValueError('The given fingerprint sensor password is wrong!')

# Search for a finger
try:
    position = f.searchTemplate()
    if position >= 0:
        print("Authentication successful: Fingerprint matched at position {}".format(position))
    else:
        print("Authentication failed: Fingerprint not found!")

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
