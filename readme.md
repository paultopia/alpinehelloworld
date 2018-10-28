Fork of heroku docker example app.

Example app is provided by heroku to illustrate [how to build a local docker image and deploy](https://devcenter.heroku.com/articles/container-registry-and-runtime).

However, why build a docker container locally and spend time pushing it, when if you use the fancy new [heroku.yml functionality](https://devcenter.heroku.com/articles/docker-builds-heroku-yml) heroku will happily build it for you?  

So this is a series of experiments.  Part 1: get the existing application to build and run using heroku.yml, and build on heroku's servers, instead of building locally. 

Steps: 

1.  clone this repo.
2.  run the following: 

```
heroku update beta
heroku plugins:install @heroku-cli/plugin-manifest
heroku create your-app-name --manifest
# make some trivial change to convince git to let you commit like echo "foo" > foo.txt or something ???
git add .
git commit -m "first commit"
heroku stack:set container
git push heroku master
heroku open
```

and a hello world should appear.

**this is verified to work**

Part 2: then switch to ubuntu, get texlive and pandoc in, and make sure that works.

Steps: 
```
git checkout ubuntu
# I'm assuming you've already the heroku steps in part 1 (updating the CLI, creating the app, etc.)
git push heroku ubuntu:master
heroku open
```

(See [this page](https://devcenter.heroku.com/articles/git#deploying-code) on deploying non-master branches to heroku.)

**this is also verified to work, yay!**
