import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueRouter from 'vue-router'
import 'normalize.css'
//css초기화

//Bootstrap-start
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueRouter)
//Bootstrap-end

Vue.config.productionTip = false

new Vue({
  router,
  store,
  data() {
    return {
      apiKey: process.env.VUE_APP_API_KEY
    }
  },
  render: h => h(App)
}).$mount('#app')
