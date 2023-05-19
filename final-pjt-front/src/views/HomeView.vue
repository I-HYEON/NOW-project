<template>
  <div class="container">
    <div class="row">
      <div class="col-9">
        <div class="container align-items-center">
          <div>
            <Carousel/>
          </div>
          <div>
            <p>게시판</p>
          </div>
        </div>
      </div>
      <div class="col-3">
        <div class="container align-items-center">
          <div>
            <Login/>
          </div>
          <div class="container">
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
          </div>
        </div>
      </div>
    </div>
    <div>
      로고+번호+제작자
    </div>
    <router-link to='/recommend'>추천</router-link>
    
    <div v-if="isLogin">현재 사용자는 {{tempToken}}</div>
    
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Carousel from '@/components/Carousel.vue'
import Login from '@/components/Login.vue'

export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    tempToken() {
      return this.$store.state.token
    }
  },
  components: {
    HelloWorld,
    Carousel,
    Login
  }
}
</script>
