import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    token: null,
    articles: [
    ],
    comments: [
    ],
    depositData: null,
    currentDetail: null,
  },
  getters: {
    // isLogin(state){
    //   return state.token ? true : false
    // },
  },
  mutations: {
    LOGIN(state, payload){
      this.state.token = payload
      console.log('잘들어갔나확인',this.state.token)
    },
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
    GET_CURRENT_DETAIL(state, currentDetail) {
      state.currentDetail = currentDetail
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
      const age = payload.age
      const gender = payload.gender
      const salary = payload.salary
      const wealth = payload.wealth
      const tendency = payload.tendency
      const email = payload.email
      console.log(username, password1, password2, age, gender, salary, wealth, tendency, email)

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/registration/',
        data: {
          username, password1, password2, age, gender, salary, wealth, tendency, email
        }
      })
      .then((res)=>{
        console.log('결과가',res)
        console.log('토큰이!!',res.data.key)
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    login(context, payload){
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: {
          username, password
        }
      })
      .then((res)=>{
        // console.log(res.data.key)
        const token = res.data.key
        context.commit('LOGIN', token)
        context.dispatch('saveTokenState')
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    saveTokenState(context) {
      const jsonToken = JSON.stringify(context.state.token)
      localStorage.setItem('token', jsonToken)
    }
  },
  modules: {
  }
})
