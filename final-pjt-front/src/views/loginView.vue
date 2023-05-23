<template>
  <div class="login">
    <div v-if="isLogin">로그인된 상태
      <div>
        여기에 프로필이 들어가면 좋겠죠
        <div>
          왜안뜨지
          {{ userInfo.username }}
        </div>
        <button @click="logOut">로그아웃</button>
      </div>
    </div>
    <div v-else>you 로그인안된 상태
      <div>
        <form @submit.prevent="login">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" v-model="username">
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <div>
        <router-link to="/signup"><button type="button" class="btn btn-primary">SignUp</button></router-link>
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
      password: ''
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
      })
      .catch((err)=>{
        console.error('로그인이실패',err)
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

  .login {
    /* background-color: #ff7743; */
    margin: 10px 10px;
    width: 15rem;
    height: 25rem;
    padding: 10px 10px;
  }
</style>