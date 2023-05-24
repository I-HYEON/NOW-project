<template>
  <div class="quick-bar" :class="{ show: isQuickBarVisible }" @mouseover="showQuickBar" @mouseleave="hideQuickBar">
    <div class="row">
      <div class="col-12 link" @click="goToHome">홈으로</div>
      <div class="col-12 link" @click="goToDepositProducts">상품조회</div>
      <div class="col-12 link" @click="goToRecommend">추천받기</div>
      <div class="col-12 link" @click="goToMapView">근처은행찾기</div>
      <div class="col-12 link" @click="goToWordSearch">백과사전</div>
      <div class="col-12 link" @click="goToProfile">마이페이지</div>
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
      }
    },
    goToDepositProducts() {
      this.$router.push({ path: '/depositproducts' });
    },
    goToRecommend() {
      this.$router.push({ path: '/recommend' });
    },
    goToMapView() {
      this.$router.push({ path: '/mapview' });
    },
    goToWordSearch() {
      this.$router.push({ path: '/wordsearch' });
    },
    goToProfile() {
      this.$router.push({ path: '/profile' });
    },
  },
};
</script>

<style scoped>
.quick-bar {
  text-align: center;
  width: 8rem;
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

.quick-bar-item {
  margin-bottom: 10px;
}
</style>
