import pyqrcode

url_path = 'https://oguzbatuhan.github.io'
url_output = 'output.svg'

url = pyqrcode.create(url_path)
url.svg(url_output, scale=8)
print(url.terminal(quiet_zone=1))