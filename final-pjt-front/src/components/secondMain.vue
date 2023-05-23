<template>
  <div class="main-second">
    <br>
    <br>
    <br>
    <div class="info-container">
      <div class="odd-info" ref="firstInfo">First Info</div>
      <div class="even-info" ref="secondInfo">Second Info</div>
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
