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
          <div>
            <QuickBar/>
        </div>
      </div>
    </div>
    <div>
      로고+번호+제작자
    </div>
    <router-link to='/recommend'>추천</router-link>
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Carousel from '@/components/Carousel.vue'
import Login from '@/components/Login.vue'
import QuickBar from '@/components/QuickBar.vue'

export default {
  name: 'HomeView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userInfo() {
      return this.$store.state.userInfo
    },
  },
  
  components: {
    HelloWorld,
    Carousel,
    Login,
    QuickBar,
  }
}
</script>
