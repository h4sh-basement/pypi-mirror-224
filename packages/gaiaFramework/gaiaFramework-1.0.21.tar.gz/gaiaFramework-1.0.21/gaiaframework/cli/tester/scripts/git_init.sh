git init
git remote add origin https://git.gaia.com/{name-your-service}
git add .
git commit -m "init creating new project"
git pull --set-upstream origin master --allow-unrelated-histories --no-edit
git push --set-upstream origin master

