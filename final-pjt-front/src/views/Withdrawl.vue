<template>
  <div>

    <div class="withdrawl-container">
      <h1>회원탈퇴</h1>
      <div class="withdrawl-form">
        <div>
        <label for="password1">현재 비밀번호  </label>
        <input type="password" id="password1" v-model="password1" >
        </div>
        <br>
        <div>
        <label for="password2">현재 비밀번호 확인 </label>
        <input type="password" id="password2" v-model="password2" >
        </div>
        <br>
        <button type="button" style="width: 200px;" @click='deleteAccount' class="btn btn-warning">확인</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'Withdrawl',
    computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userInfo() {
      return this.$store.state.userInfo
    },
    },
    data(){
        return{
            password1:null,
            password2:null,
        }
    },
    methods:{
    deleteAccount() {
      const password1 = this.password1
      const password2 = this.password2
      if (password1===password2){
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/delete/`,
        data: {password1},
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
      })
        .then(() => {
          // Account deletion successful
          // Perform any additional actions, such as logging out the user or redirecting
          // to a different page
          console.log('Account deleted successfully')
          this.$store.dispatch('logOut')
          this.$router.push({ name: 'home' })
        })
        .catch((error) => {
          // Account deletion failed
          // Handle the error accordingly
          console.error('Account deletion failed:', error)
        })}
      else{
        alert('비밀번호가 일치하지 않습니다')
      }

    },
    check(){
        console.log(this.password1,this.password2)
    }
    }
}
</script>

<style>
label{
  margin-right: 10px;
}

.withdrawl-container{
  text-align: center;
}
.withdrawl-form {
  display: inline-block;
  padding: 20px;
  width: 300px;
  height: 230px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>