<template>
  <div class="back-ground">
    <br>
    <br>
    <br>
    <div class="info-container">
      <img class="odd-info main_image" ref="firstInfo" src='@/photo/base_img/first_info.jpg' alt="first_img" style="max-width:100%; height:auto;">
      <img class="odd-info main_image" ref="thirdInfo" src='@/photo/base_img/third_info.jpg' alt="third_img" style="max-width:100%; height:auto;" @click="goToRecommend">
      <img class="even-info main_image" ref="forthInfo" src='@/photo/base_img/forth_info.jpg' alt="forth_img" style="max-width:100%; height:auto;">
      <Footer/>
    </div>
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'

export default {
  name: 'MainPage',
  components: {
    Footer,
  },
  mounted() {
    this.createIntersectionObserver();
  },
    data(){
    return {
    articles:this.$store.state.articles
    }
  },
  methods: {
    goToRecommend() {
      return this.$router.push({ path: '/recommend' })
    },
    createIntersectionObserver() {
      const options = {
        root: null, // 스크롤 기준 요소 (기본값은 viewport)
        threshold: 0.5 // 트리거 되는 요소가 얼마나 보여야하는지 설정 (0.5는 절반 이상 보일 때 트리거)
      };

      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
          } else {
            entry.target.classList.remove('fade-in');
          }
        });
      }, options);

      const infoElements = this.$refs;
      Object.keys(infoElements).forEach(key => {
        observer.observe(infoElements[key]);
      });
    },
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  }
};
</script>

<style>
.main_image{
  width: 100vw;
  height: auto;
}

.back-ground {
  max-width: 100%;
  height: auto;
  background: linear-gradient( #601986, white, #601986);
}

.info-container {
  padding: 0;
  height: auto; /* 스크롤을 위한 임시 높이 */
  /* display: flex; */
  flex-direction: column;
  align-items: center;
  justify-content: center;
  
}

.odd-info {
  opacity: 0;
  transition: opacity 0.5s;
  max-width: 100%;
  height: 1000px;
  /* padding: 20px; */
  /* margin: 5px 5px 5px 5px; */
  /* background-color: white; */
  /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); */
}

.even-info {
  opacity: 0;
  transition: opacity 0.5s;
  margin: 0px;
  height: 1000px;
  /* padding: 20px; */
  /* background-color: black; */
  /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); */
}

.fade-in {
  opacity: 1;
}
</style>
