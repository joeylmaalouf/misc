if [[ $# -gt 0 ]]
  then
    appname=$1
  else
    appname="nodeapp"
fi
echo "Creating node app boilerplate for $appname..."
mkdir $appname
cd $appname
directories="public/javascripts public/stylesheets routes views/layouts"
for directory in $directories;
do
  echo "Making directory $directory"
  mkdir -p $directory
done
files="app.js public/javascripts/main.js public/stylesheets/styles.css routes/index.js views/layouts/main.handlebars views/home.handlebars"
for file in $files;
do
  echo "Making file $file"
  touch $file
done
cd ..
echo "All done!"
