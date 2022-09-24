import os

with open('.\\dist\\index.html', 'r', encoding='utf-8') as fp:
    content = fp.read()
    content = content.replace('/favicon', 'favicon').replace('/_assets/', '')
    with open('.\\dist\\index.html', 'w', encoding='utf-8') as f:
        f.write(content)

cmd = '''cd dist
move .\_assets\* .
rmdir /Q _assets

git init
git add -A
git commit -m deploy
git push -f git@github.com:drelf2018/nana7mi.link.git master:gh-pages
cd ..'''

for c in cmd.split('\n'):
    os.system(c)
