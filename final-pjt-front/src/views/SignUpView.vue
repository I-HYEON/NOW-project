<template>
  <div>
    <form @submit.prevent="signUp">
        <label for="username">ID:</label>
        <input type="text" id="username" v-model="username">
        <br>

        <label for="password1">password:</label>
        <input type="text" id="password1" v-model="password1">
        <br>

        <label for="password2">password confirmation:</label>
        <input type="text" id="password2" v-model="password2">
        <br>

        <label for="age">나이:</label>
        <input type="text" id="" v-model="age">
        <br>

        <label for="gender">성별:</label>
        <input type="radio" name="gender" v-model="gender" value="1">남자
        <input type="radio" name="gender" v-model="gender" value="2">여자
        <br>

        <label for="salary">연봉:</label>
        <input type="text" id="salary" v-model="salary">
        <br>

        <label for="wealth">자산:</label>
        <input type="text" id="wealth" v-model="wealth">
        <br>

        <label for="tendency">저축성향:</label>
        <input type="radio" name="tendency" v-model="tendency" value="1">단기
        <input type="radio" name="tendency" v-model="tendency" value="2">중기
        <input type="radio" name="tendency" v-model="tendency" value="3">장기
        <br>

        <!-- <label for="email">email:</label>
        <input type="text" v-model="email">
        <br> -->

        <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
        username: '',
        password1: '',
        password2: '',
        age: '',
        gender: '',
        salary: '',
        wealth: '',
        tendency: '',
    }
  },
  methods: {
    signUp() {
        // console.log('SignUpView까지는 잘가고있음')
        const username = this.username;
        const password1 = this.password1;
        const password2 = this.password2;
        const age = this.age;
        const gender = this.gender;
        const salary = this.salary;
        const wealth = this.wealth;
        const tendency = this.tendency;

        const payload = {
            username, password1, password2, age, gender, salary, wealth, tendency
        }

        this.$store.dispatch('signUp', payload)
        .then(() => {
          //성공적으로 회원가입이 완료된 경우
          console.log('메인으로')
          this.$store.dispatch('getUserInfo')
          this.$router.push('/')
        })
        .catch((error)=>{
          console.log('메인으로못감')
          console.error(error)
        })
        // console.log(this.gender)
    }
}
}
</script>

<style>

</style>