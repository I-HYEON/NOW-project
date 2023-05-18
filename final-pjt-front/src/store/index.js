import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    depositData: null,
  },
  getters: {
  },
  mutations: {
    GET_DEPOSIT_DATA(state, depositData) {
      state.depositData = depositData
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: {
          username, password1, password2
        }
      })
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=> {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
