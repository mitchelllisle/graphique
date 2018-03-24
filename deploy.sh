echo "---------------------------------"
echo "Package & Build"
echo "---------------------------------"

echo " - Remove Old Packages..."
rm -r dist

echo " - Package Latest Graphique package..."
python setup.py sdist

echo " - Uploading to PyPi..."
twine upload dist/*

echo " - Pushing to github ...."
git add .
git commit -m 'pushing new version'
git push
git pull

echo " - Installing new version ...."
pip install -U  graphique --no-cache-dir

echo "Done!"
