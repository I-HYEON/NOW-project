<template>
  <div>

    <div>
    <label for="old_password">전 비밀번호 : </label>
    <input type="text" id="old_password" v-model="old_password" >
    </div>
    <div>
    <label for="new_password1">새 비밀번호 : </label>
    <input type="text" id="new_password1" v-model="new_password1" >
    </div>
    <div>
    <label for="new_password2">새 비밀번호 확인 : </label>
    <input type="text" id="new_password2" v-model="new_password2" >
    </div>
    <button type='submit' @click='changePassword'>진짜로 할거야?</button>
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
        }
    },
    methods:{
    changePassword() {
      const old_password = this.old_password  
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
    //   console.log((new_password1 && new_password2 && old_password))
      if (new_password1===new_password2 && old_password!==new_password1 && (new_password1 && new_password2 && old_password)){
      
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
          console.error('Account deletion failed:', error)
        })}
    else if(!(new_password1 && new_password2 && old_password)){
        alert('빈칸은 안되요')
      }  
      else if(new_password1!==new_password2){
        alert('비밀번호가 일치하지 않습니다')
      }

      else{
        alert('전과 다른 비밀번호로 변경해주세요')
      }

    },
    check(){
        console.log(this.old_password,this.new_password1,this.new_password2,)
    }
    }
}
</script>

<style>

</style>