import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/components/HomeView'
import AboutView from '@/components/AboutView'
import ContactView from '@/components/ContactView'
import PrecintView from '@/components/PrecintView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/about',
      name: 'AboutView',
      component: AboutView
    },
    {
      path: '/contact',
      name: 'ContactView',
      component: ContactView
    },
    {
      path: '/precint/:id',
      name: 'PrecintView',
      component: PrecintView
    }
  ]
})
