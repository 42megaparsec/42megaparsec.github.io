@echo off
echo ===============================
echo  Hugo build starting...
echo ===============================

hugo --minify -d docs

echo ===============================
echo  Deploying to GitHub...
echo ===============================

git add .
git commit -m "update"
git push

echo ===============================
echo  Deployment finished!
echo ===============================

pause