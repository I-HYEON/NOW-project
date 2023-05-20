import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DepositProducts from '../views/DepositProducts.vue'
import Community from '../views/Community.vue'
import SignUpView from '../views/SignUpView.vue'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import ArticleDetailView from '../views/ArticleDetailView'
import DepositDetail from '../views/DepositDetail.vue'
import Recommend from '../views/Recommend.vue'
import MapView from '../views/MapView.vue'

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
    path: '/depositproducts/:bank_info',
    name: 'deposit_detail',
    component: DepositDetail
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
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

  {
    path: '/article',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/article/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/mapview',
    name: 'mapview',
    component: MapView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
