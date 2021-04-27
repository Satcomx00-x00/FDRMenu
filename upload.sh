sudo rm -rf *.dist-info *.egg-info
sudo rm -fR *.pyc
git init -b main
git add .
git commit -m "File Preview Feature"
git push -f origin main
