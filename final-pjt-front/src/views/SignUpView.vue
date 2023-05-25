<template>
  <div>
    <div class="signup-container">
      <h1>Sign Up</h1>
      <br>
      <div class="signup-form ">
        <form >
            <label for="username">아이디</label><br>
            <input type="text" id="username" v-model="username"><br>
            <br>
            <label for="password1">비밀번호</label><br>
            <input type="password" id="password1"  v-model="password1" ><br>
            <br>
            <label for="password2">비밀번호확인</label><br>
            <input type="password" id="password2" v-model="password2"><br>
            <br>
            <label for="age">나이</label><br>
            <input type="text" id="" v-model="age"><br>
            <br>
            <label for="gender">성별</label><br>
            <input type="radio" name="gender" v-model="gender" value="1">남자
            <input type="radio" name="gender" v-model="gender" value="2">여자<br>
            <br>
            <label for="salary">연봉 (만원)</label><br>
            <input type="text" id="salary" v-model="salary"><br>
            <br>
            <label for="wealth">자산 (만원)</label><br>
            <input type="text" id="wealth" v-model="wealth"><br>
            <br>
            <label for="tendency">저축성향</label>
            <input type="radio" name="tendency" v-model="tendency" value="1">단기
            <input type="radio" name="tendency" v-model="tendency" value="2">중기
            <input type="radio" name="tendency" v-model="tendency" value="3">장기<br>
            <br>
            <!-- <label for="email">email:</label>
            <input type="text" v-model="email">
            <br> -->
            <button type="button" @click="signUp" style="width: 200px; background-color: #601986; color:white;" class="btn">확인</button>
        </form>
      </div>
    </div>
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
        console.log('SignUpView까지는 잘가고있음')
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
        console.log(payload)
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
    },
    maskText(text) {
      const maskedText = '*'.repeat(text.length);
      return maskedText;
}
}
}
</script>

<style>
label{
  margin-right: 10px;
}

.signup-container{
  text-align: center;
}
.signup-form {
  display: inline-block;
  padding: 20px;
  width: 300px;
  height: 670px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>