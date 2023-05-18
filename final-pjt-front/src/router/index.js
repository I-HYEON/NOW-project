import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DepositProducts from '../views/DepositProducts.vue'
import Community from '../views/Community.vue'
import SignUpView from '../views/SignUpView.vue'

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
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
