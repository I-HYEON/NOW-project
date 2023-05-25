<template>
  <div>
    <div class="change-pw-container">
      <h1>비밀번호 변경</h1>
      <div class="change-pw-form">
        <div>
        <label for="old_password">전 비밀번호  </label>
        <input type="password" id="old_password" v-model="old_password" >
        </div><br>
        <div>
        <label for="new_password1">새 비밀번호  </label>
        <input type="password" id="new_password1" v-model="new_password1" >
        </div><br>
        <div>
        <label for="new_password2">새 비밀번호 확인  </label>
        <input type="password" id="new_password2" v-model="new_password2" >
        </div><br>
        <button type="button"  @click="changePassword" style="margin-bottom:5px; width: 200px;" class="btn btn-success">확인</button>
        <p style="margin-bottom:50px; color:red ;text-align:center"><span v-if='check'>비밀번호가 유효하지 않습니다.</span></p>
        </div>
    
  </div>
      </div>
      
    
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ChangePassword',
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
            old_password:null,
            new_password1:null,
            new_password2:null,
            check:false,
        }
    },
    methods:{
    changePassword() {
      const old_password = this.old_password  
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
    //   console.log((new_password1 && new_password2 && old_password))
      
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/changepassword/`,
        data: {old_password: old_password,new_password:new_password1},
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
      })
        .then(() => {
          // Account deletion successful
          // Perform any additional actions, such as logging out the user or redirecting
          // to a different page
          console.log('Account deleted successfully')
        //   this.$store.dispatch('logOut')
          this.$router.push({name: 'ProfileView'})
        })
        .catch((error) => {
          // Account deletion failed
          // Handle the error accordingly
          console.log('gjgjgj')
          console.error('Account deletion failed:', error)
          this.check = true
        })

    },

    }
}
</script>

<style>
label{
  margin-right: 10px;
}

.change-pw-container{
  text-align: center;
}
.change-pw-form {
  display: inline-block;
  padding: 20px;
  width: 300px;
  height: 320px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>