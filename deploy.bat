cd dist
move .\\_assets\\* .
rmdir /Q _assets

git init
git add -A
git commit -m deploy
git push -f git@github.com:drelf2018/nana7mi.link.git master:gh-pages
cd ..