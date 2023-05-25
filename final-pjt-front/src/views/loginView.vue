<template>
  <div class="login-container">
    <!-- <div v-if="isLogin">로그인된 상태
      <div>
        여기에 프로필이 들어가면 좋겠죠
        <div>
          왜안뜨지
          {{ userInfo.username }}
        </div>
        <button @click="logOut">로그아웃</button>
      </div>
    </div> -->
    <h1>Log In</h1>
    <div class="login-form">
      <div >
        <form>
            <label for="username" class="form-label">아이디</label><br>
            <input type="text"  style="width: 200px;" id="username" v-model="username">
            <br><br>
            <label for="exampleInputPassword1" class="form-label">비밀번호</label><br>
            <input type="password" style="width: 200px;" id="exampleInputPassword1" v-model="password">
            <br><br>
          <button type="button" @click="login" style="width: 200px; background-color: #601986; color:white;" class="btn">로그인</button>

        </form>
          

      </div>
      <div>
        <br>
      <span style="color:red" v-if='check'>아이디와 비밀번호를 확인해주세요</span>
        
        <br>
        
        <span>아직 회원이 아니신가요? </span>
        <router-link to="/signup">회원가입</router-link>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'loginView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userInfo() {
      return this.$store.state.userInfo
    }
  },
  data() {
    return {
      username: '',
      password: '',
      check: false
    }
  },
  methods: {
    login() {
      const username = this.username;
      const password = this.password;

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
      .then(()=>{
        //로그인이 정상적으로 되었을때 getUserInfo()메서드를 실행시켜서 userInfo를 가져오
        this.$store.dispatch('getUserInfo')
        this.$router.push({name: 'home'})
      })
      .catch((err)=>{
        console.error('로그인이실패',err)
        this.check=true
      })
    },
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .body {
    background-image: url('@/photo/base_img/onlypig.jpg');
  }

  /* .login {
    margin: 10px 10px;
    width: 15rem;
    height: 25rem;
    padding: 10px 10px;
  } */
  .login-container {
    text-align: center;
  }
  .login-form {
  display: inline-block;
  padding: 20px;
  width: 300px;
  height: 250px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
</style>