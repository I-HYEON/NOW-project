<template>
  <div>
    
    <div class="profile-change-container">
      <h1>프로필 변경</h1>
      <div class="profile-change-form">
        <form>
            <label for="username">아이디</label><br>
            <input type="text" id="username" v-model="updatedFormData.username" disabled><br>
            <br>
            <label for="age">나이</label><br>
            <input type="text" id="" v-model="updatedFormData.age"><br>
            <br>
            <label for="gender">성별</label><br>
            <input type="radio" name="gender" v-model="updatedFormData.gender" value="1">남자
            <input type="radio" name="gender" v-model="updatedFormData.gender" value="2">여자<br>
            <br>
            <label for="salary">연봉 (만원)</label><br>
            <input type="text" id="salary" v-model="updatedFormData.salary"><br>
            <br>
            <label for="wealth">자산 (만원)</label><br>
            <input type="text" id="wealth" v-model="updatedFormData.wealth"><br>
            <br>
            <label for="tendency">저축성향</label>
            <input type="radio" name="tendency" v-model="updatedFormData.tendency" value="1">단기
            <input type="radio" name="tendency" v-model="updatedFormData.tendency" value="2">중기
            <input type="radio" name="tendency" v-model="updatedFormData.tendency" value="3">장기<br>
            <br>
            <!-- <label for="email">email:</label>
            <input type="text" v-model="email">
            <br> -->
            <button type="button" @click="updateProfile" style="width: 200px;" class="btn btn-success">확인</button>
        </form>
      </div>
    </div>
    <!-- {{updatedFormData}} -->
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileUpdateView',
  data() {
    return {
      updatedFormData: this.$store.state.userInfo,
    };
  },
  computed: {
  },
  methods: {
    updateProfile() {
      const username = this.updatedFormData.username
      const age = this.updatedFormData.age
      const gender = this.updatedFormData.gender
      const salary = this.updatedFormData.salary
      const wealth = this.updatedFormData.wealth
      const tendency = this.updatedFormData.tendency
      console.log(this.$store.state.token)
      axios({
        method: 'patch',
        url: `${API_URL}/accounts/user/`,
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          age, gender, salary, wealth, tendency
        },
      })
      .then((res)=>{
        console.log(res)
        this.$store.dispatch('getUserInfo')
        this.$router.push({name: 'ProfileView'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
};
</script>
<style>
label{
  margin-right: 10px;
}

.profile-change-container{
  text-align: center;
}
.profile-change-form {
  display: inline-block;
  padding: 20px;
  width: 300px;
  height: 520px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>