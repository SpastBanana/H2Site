git add .
git status
echo Commit Text:
read pushname
git commit -m $pushname
git push