import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    articles: [
    ],
    comments: [
    ],
    depositData: null,
  },
  getters: {
    // isLogin(state){
    //   return state.token ? true : false
    // },
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    },
    GET_COMMENTS(state, comments){
      state.comments = comments
      console.log(state.comments)
    },
    GET_DEPOSIT_DATA(state, depositData) {
      state.depositData = depositData
    },
  },
  actions: {
    getArticles(context){
      axios({
        method: 'get',
        url : `${API_URL}/articles/`
      })
      .then((res)=> {
        context.commit('GET_ARTICLES',res.data)
      })
      .catch(err => console.log(err))
    },
    getComments(context){
      axios({
        method: 'get',
        url:  `${API_URL}/articles/comments/`
      })
      .then((res)=>{
        console.log(res)
        context.commit('GET_COMMENTS',res.data)
      })
      .catch(err => console.log(err))
    },
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
