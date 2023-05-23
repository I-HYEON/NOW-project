<template>
  <div>
    <h1>Edit User Information</h1>
    <!-- <h2>{{userInfo}}</h2> -->
    <form @submit.prevent="updateProfile">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="updatedFormData.username">
      </div>
      <div>
        <label for="age">Age:</label>
        <input type="number" id="age" v-model="updatedFormData.age">
      </div>
      <div>
        <label for="gender">Gender:</label>
        <input type="text" id="gender" v-model="updatedFormData.gender">
      </div>
      <div>
        <label for="salary">Salary:</label>
        <input type="number" id="salary" v-model="updatedFormData.salary">
      </div>
      <div>
        <label for="wealth">Wealth:</label>
        <input type="number" id="wealth" v-model="updatedFormData.wealth">
      </div>
      <div>
        <label for="tendency">Tendency:</label>
        <input type="number" id="tendency" v-model="updatedFormData.tendency">
      </div>
      <button type="submit">Save</button>
    </form>
    {{updatedFormData}}
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
        this.$router.push({name: 'ProfileView'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
};
</script>
