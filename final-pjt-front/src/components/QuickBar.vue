<template>
  <div class="quick-bar" :class="{ show: isQuickBarVisible }" @mouseover="showQuickBar" @mouseleave="hideQuickBar">
    <div class="row">
      <div class="col-12 link icon" @click="goToHome"><span class="material-symbols-outlined">home</span></div>
      <div class="col-12 link desc" @click="goToHome">홈</div>
      <div class="col-12 link icon" @click="goToDepositProducts"><span class="material-symbols-outlined">money</span></div>
      <div class="col-12 link desc" @click="goToDepositProducts">상품조회</div>
      <div class="col-12 link icon" @click="goToRecommend"><span class="material-symbols-outlined">recommend</span></div>
      <div class="col-12 link desc" @click="goToRecommend">상품추천</div>
      <div class="col-12 link icon" @click="goToMapView"><span class="material-symbols-outlined">map</span></div>
      <div class="col-12 link desc" @click="goToMapView">근처은행</div>
      <div class="col-12 link icon" @click="goToWordSearch"><span class="material-symbols-outlined">search</span></div>
      <div class="col-12 link desc" @click="goToWordSearch">단어검색</div>
      <div v-if="isLogin">
        <div class="col-12 link icon" @click="goToProfile"><span class="material-symbols-outlined">person</span></div>
        <div class="col-12 link desc" @click="goToProfile">마이페이지</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuickBar',
  data() {
    return {
      isQuickBarVisible: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    window.addEventListener('resize', this.handleResize);
    this.handleResize();
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    handleScroll() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      this.isQuickBarVisible = scrollTop > 0;
    },
    handleResize() {
      const screenWidth = window.innerWidth;
      this.isQuickBarVisible = screenWidth >= 600; // 화면 너비가 600px 이상일 때만 퀵바 표시
    },
    showQuickBar() {
      this.isQuickBarVisible = true;
    },
    hideQuickBar() {
      this.isQuickBarVisible = false;
    },
    goToHome() {
      if (this.$route.path !== '/') {
        this.$router.push({ path: '/' });
      } else {
        this.scrollToTop();
      }
    },
    goToDepositProducts() {
      if (this.$route.path !== '/depositproducts') {
      this.$router.push({ path: '/depositproducts' });}
    },
    goToRecommend() {
      if (this.$route.path !== '/recommend') {
      this.$router.push({ path: '/recommend' });}
    },
    goToMapView() {
      if (this.$route.path !== '/mapview') {
        this.$router.push({ path: '/mapview' });
      }
    },
    goToWordSearch() {
      if (this.$route.path !== '/wordsearch') {
      this.$router.push({ path: '/wordsearch' });}
    },
    goToProfile() {
      if (this.$route.path !== '/profile') {
      this.$router.push({ path: '/profile' });}
    },
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  }
};
</script>

<style scoped>
.quick-bar {
  text-align: center;
  width: 6rem;
  position: fixed;
  right: -5rem;
  bottom: 30%;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 15px;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: right 0.3s ease-in-out;
}

.quick-bar.show {
  right: 20px;
}

@media (max-width: 600px) {
  .quick-bar {
    display: none;
  }
}
  .desc{
    font-size: 13px;
  }

  .icon {
    cursor: pointer;
  }
.quick-bar-item {
  margin-bottom: 10px;
}
</style>