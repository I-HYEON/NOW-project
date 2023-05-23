<template>
  <div class="container-fluid">
    <div class="main">
      <firstMain/>
    </div>

    <div class="info-container">
        <secondMain/>
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src
import firstMain from '@/components/firstMain.vue'
import secondMain from '@/components/secondMain.vue'
import Carousel from '@/components/Carousel.vue'
// import login from '@/components/Login.vue'
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
    firstMain,
    secondMain,
    Carousel,
    // Login,
    QuickBar,
  }
}
</script>

<style>
    .container-fluid {
      display: flex;
      flex-direction: column;
    }
    .info-container {
      /* border: 1px solid black; */
    }

    .purple {
      color:  #601986
    }
</style>
