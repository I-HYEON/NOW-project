<template class="template">

  <div class="appvue-container">
    
    <nav class="main_nav navbar navbar-expand-lg">
      <div class="container-fluid">
        
        <spans class="navbar-brand">
          <router-link to="/" class="link">
            ●●●
          </router-link>
        </spans>
        
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
                  <router-link to="/article" class="link">커뮤니티</router-link>
                </a>
              </li>
              <li class="nav-item">
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
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
                </a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Action</a></li>
                    <li><a class="dropdown-item" href="#">Another action</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
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
  </div>
</template>

<script>


export default {
    name : 'APP',
    methods : {
      logOut() {
      this.$store.dispatch('logOut')
    }
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
<style>
    
  .appvue-cotainer {
    background-color: #ffd788;
    display: flex;
    flex-direction: column;
  }

  .main_nav {
    height: 50px;
        /* background-color: rgb(255, 144, 144); */
    color: #601986; /*왜적용안되는지모르겠음*/
    margin: 20px 0px 20px 60px;
  };

  .link {
    text-decoration: none;
    color: inherit;
  }

  #navbarSupportedContent {
    color: white
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
