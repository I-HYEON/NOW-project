import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DepositProducts from '../views/DepositProducts.vue'
import Community from '../views/Community.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/depositproducts',
    name: 'depositproducts',
    component: DepositProducts
  },
  {
    path: '/community',
    name: 'community',
    component: Community
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
