import os
os.system('cnpm run build')
with open('.\\dist\\index.html', 'r', encoding='utf-8') as fp:
    content = fp.read()
    content = content.replace('/favicon', 'favicon').replace('/_assets/', '')
    with open('.\\dist\\index.html', 'w', encoding='utf-8') as f:
        f.write(content)

os.system('deploy.bat')
