# CERP

> The webview for the CERP project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

Additional notes:

The only file that needs to be changed is: 

`src/config.js`

There are three options:

1. API_LOCATION: 'http://localhost:5000'
2. API_LOCATION: ''
3. API_LOCATION: 'https://cerp-code-foco.herokuapp.com'

Use 1 if you are planning on making changes to both the front end and back end (you'll need to start the pythons server)
Use 2 if you are building for production DONT FORGET TO CHANGE CONFIG TO THIS IF BUILDING FOR PRODUCTION
Use 3 if you are planning on making changes to the front end, and don't want to start up the local dev server