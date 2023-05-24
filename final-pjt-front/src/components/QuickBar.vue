<template>
    <div class="quick-bar" :class="{ show: isQuickBarVisible }">
        <div class="row">
            <router-link class="col-12 link" to="mapview/"><div class="quick-bar-item">근처은행</div></router-link><br>
            <router-link class="col-12 link" to="wordsearch/"><div class="quick-bar-item">백과사전</div></router-link><br>
            <router-link class="col-12 link" to="mapview/"><div class="quick-bar-item">무언가더</div></router-link><br>
            <router-link class="col-12 link" to="mapview/"><div class="quick-bar-item">추가하면</div></router-link><br>
            <router-link class="col-12 link" to="mapview/"><div class="quick-bar-item">좋겠지만</div></router-link><br>
            <router-link class="col-12 link" to="mapview/"><div class="quick-bar-item">음...음</div></router-link><br>
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
    },
  };
  </script>
  
  <style scoped>


  .quick-bar {
    text-align: center;
    width: 8rem;
    position: fixed;
    right: 20px;
    bottom: 30%;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 15px;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: opacity 0.3s ease-in-out;
    opacity: 0;
  }
  
  .quick-bar.show {
    opacity: 1;
  }

  @media (max-width: 600px) {
  .quick-bar {
    display: none; /* 화면 너비가 600px 이하일 때 퀵바 숨김 */
  }
}
.quick-bar-item {
  margin-bottom: 10px; /* 아이템 사이의 행간을 조절하는 부분 */
}
  </style>
