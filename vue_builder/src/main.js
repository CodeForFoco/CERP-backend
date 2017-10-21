// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import VueMaterial from 'vue-material'
import VueHighcharts from 'vue-highcharts'
import 'vue-material/dist/vue-material.css'

import VueResource from 'vue-resource'

Vue.use(VueMaterial) // this allows material design
Vue.use(VueResource) // this allows get / post requests
Vue.use(VueHighcharts) // Use highcharts

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
