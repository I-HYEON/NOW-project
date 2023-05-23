<template>
  <div class="main-second">
    <br>
    <br>
    <br>
    <div class="info-container">
      <div class="odd-info" ref="firstInfo">
        
      </div>
      <div class="even-info" ref="secondInfo">
        <div class="container">
    <div class="col-12">
      <div class="row">
        <div class="col-4">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">Articles</h5>
              <div v-for="(article, index) in articles" :key="index">
                <h6>{{ article.title }} 작성자 :{{ article.username }} </h6>
              </div>
            </div>
          </div>
        </div>
        <div class="col-4">
          <div class="card h-100">
            <div class="card-body">
              이게 무슨내용

              <!-- Customize the content for the second and third cards here -->
              <!-- You can add any HTML elements or Vue directives -->
            </div>
          </div>
        </div>
        <div class="col-4">
          <div class="card h-100">
            <div class="card-body">
              여기에 내용을 추가해

              <!-- Customize the content for the second and third cards here -->
              <!-- You can add any HTML elements or Vue directives -->
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
      </div>
      <div class="odd-info" ref="thirdInfo">Third Info</div>
      <div class="even-info" ref="forthInfo">forth Info</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'secondMain',
  mounted() {
    this.createIntersectionObserver();
  },
    data(){
    return {
    articles:this.$store.state.articles
    }
  },
  methods: {
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
.main-second {
  max-width: 100%;
  height: auto;
  background: linear-gradient(#f19319, white, #f19319);
}

.info-container {
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
  height: 800px;
  padding: 20px;
  /* margin: 5px 5px 5px 5px; */
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.even-info {
  opacity: 0;
  transition: opacity 0.5s;
  margin: 0px;
  height: 800px;
  padding: 20px;
  background-color: black;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.fade-in {
  opacity: 1;
}
</style>
