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
      console.log(this.$store.state.userInfo)
      return this.$store.state.userInfo
    },
  },
  
  components: {
    MainPage,
    Carousel,
    QuickBar,
  },
  created(){
    console.log(this.$store.state.userInfo)
  }
}
</script>

<style>

    .container-fluid {
      padding: 0;
      display: flex;
      flex-direction: column;
      margin-right: 0;
      margin-left: 0;
    }

    .purple {
      color:  #601986
    }
</style>
