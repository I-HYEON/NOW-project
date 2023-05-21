import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

//Bootstrap-start
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
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
