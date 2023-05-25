<template class="template">

  <div class="appvue-container">
    <div class="d-flex justify-content-center">
      <img src='@/photo/png/mainlogo.png' alt="main_img" style="max-width:120px; height:auto; margin:20px 0px 0px 20px; cursor:pointer;" @click="goToHome">
    </div>
    
    
    <nav class="main_nav navbar navbar-expand-lg">
      <div class="container-fluid">
        
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/" class="link">Home</router-link>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/depositproducts" class="link">예적금상품조회</router-link>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/recommend" class="link">맞춤상품추천</router-link>
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/article" class="link">커뮤니티</router-link>
                </a>
              </li>
              
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                HELP
                </a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" @click="goToMapView">근처 은행 검색</a></li>
                    <li><a class="dropdown-item" @click="goToWordSearch">금융 용어 검색</a></li>
                    <li><a class="dropdown-item" @click="goToMoneyChange">환율 환전 정보</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li @click="goToFooter"><a class="dropdown-item" href="#">문의사항</a></li>
                </ul>
              </li>

              <li v-if="isLogin" class="nav-item">
                <div class="nav-link">
                {{userInfo.username}}님
                </div>
              </li>

              <li v-if="isLogin" class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/profile" class="link">마이페이지</router-link>
                </a>
              </li>

              <li v-if="!isLogin" class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/signup" class="link">회원가입</router-link>
                </a>
              </li>
              <li v-if="!isLogin" class="nav-item">
                <a class="nav-link" href="#">
                  <router-link to="/login" class="link">로그인</router-link>
                </a>
              </li>
              <li v-if="isLogin" class="nav-item">
                <a class="nav-link" href="#">
                  <span class="link" @click="logOut">로그아웃</span>
                </a>
              </li>
              
            </ul>

        </div>
      </div>
    </nav>
    
    <div class="main_page">
      <transition name="slide" mode="out-in">
        <router-view/>
      </transition>
    </div>
    <QuickBar/>
  </div>
</template>

<script>
import QuickBar from '@/components/QuickBar.vue'

export default {
    name : 'APP',
    components: {
      QuickBar
    },
    methods : {
      logOut() {
      this.$store.dispatch('logOut')
    },
    goToHome() {
      if (this.$route.path !== '/') {
        this.$router.push({ path: '/' });
      }
    },
    goToMapView() {
      if (this.$route.path !== '/mapview') {
        this.$router.push({ path: '/mapview' });
      }
    },
    goToWordSearch() {
      if (this.$route.path !== '/wordsearch') {
        this.$router.push({ path: '/wordsearch' });
      }
    },
    goToMoneyChange() {
      if (this.$route.path !== '/moneychange') {
      this.$router.push({ path: '/moneychange' });}
    },
    goToFooter() {
      window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: 'smooth'
      })
    },
    },
    computed: {
    isLogin() {
        return this.$store.getters.isLogin
    },
    userInfo() {
        return this.$store.state.userInfo
    }
},
}
</script>

<style scope>

  .dropdown-item{
    cursor: pointer;
  }
  
  .container-fluid{
    display: flex;
    flex-direction: column;
  }
  .main_nav {
    margin: 20px 0px 20px 60px;
  };

  .a {
    text-decoration: none;
    color: inherit;
  }

  .link {
    text-decoration: none;
    color: inherit;
  }

  .navbar-collapse {
    margin: 0px auto;
  }

  #navbarSupportedContent {
    color: white;
  }

  .fade-enter-active,
  .fade-leave-active {
     transition: opacity 0.5s;
  }

  .fade-enter,
  .fade-leave-to {
     opacity: 0;
  }

  .slide-enter-active,
  .slide-leave-active {
  transition: transform 0.5s;
}

  .slide-enter,
  .slide-leave-to {
  transform: translateX(100%);
}

</style>
