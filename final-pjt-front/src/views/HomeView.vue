<template>
  <div class="container-fluid">
    <img src='@/photo/base_img/withdog.jpg' alt="main_img" style="max-width:100%; height:auto;">

    <div class="info-container">
        <MainPage/>
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src
// import firstMain from '@/components/firstMain.vue'
import MainPage from '@/components/MainPage.vue'
import Carousel from '@/components/Carousel.vue'
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
    // firstMain,
    MainPage,
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
      margin-right: 0;
      margin-left: 0;
    }

    .purple {
      color:  #601986
    }
</style>
