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
import WordSearch from '../views/WordSearch.vue'
import ProfileView from '../views/ProfileView.vue'
import ProfileUpdateView from '../views/ProfileUpdateView.vue'
import UpdateView from '../views/UpdateView.vue'
import Withdrawl from '../views/Withdrawl'
import loginView from '../views/loginView.vue'
import ChangePassword from '../views/ChangePassword.vue'
import MoneyChange from '../views/MoneyChange.vue'

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
    path: '/login',
    name: 'login',
    component: loginView
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
  },
  {
    path: '/wordsearch',
    name: 'WordSearch',
    component: WordSearch
  },
  {
    path: '/moneychange',
    name: 'MoneyChange',
    component: MoneyChange
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/profileupdate',
    name: 'ProfileUpdateView',
    component: ProfileUpdateView
  },
  {
    path: '/update/:id',
    name: 'UpdateView',
    component: UpdateView
  },
  {
    path: '/withdrawl',
    name: 'Withdrawl',
    component: Withdrawl
  },
  {
    path: '/changepassword',
    name: 'ChangePassword',
    component: ChangePassword
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
