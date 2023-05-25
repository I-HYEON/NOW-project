<template>
  <div class="DepositCard" :class="{ 'hovered': isHovered }" @click="navigateToDetail">
    <img :src="getBankImage(deposit.kor_co_nm)" class="card-img-top" :alt="`Image not found: ${deposit.kor_co_nm}`">
    <div class="card-body">
      <h5 class="card-title">{{ deposit.fin_prdt_nm }}</h5>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item explain">{{ deposit.kor_co_nm }}</li>
      <li class="list-group-item explain">현재 가입자 수: {{ deposit.user_count }}</li>
      <li class="list-group-item explain">최대 금리 {{ deposit.max_intr }}%</li>
    </ul>
    <div class="card-body"></div>
  </div>
</template>

<script>
import dummycat from "@/photo/dummycat.jpg"

export default {
  name: 'DepositCard',
  props: {
    deposit: Object
  },
  data() {
    return {
      isHovered: false
    }
  },
  methods: {
    getBankImage(korCoNm) {
      try {
        return require(`@/bank_photo/${korCoNm}.png`);
      } catch (error) {
        console.error(error);
        return dummycat;
      }
    },
    navigateToDetail() {
      this.$router.push({
        name: 'deposit_detail',
        params: {
          bank_info: this.deposit.fin_prdt_cd
        }
      });
    }
  }
}
</script>

<style scoped>
.DepositCard {
  font-size: 0.5rem;
  /* background-color: white; */
  color:black;
  width: calc(20% - 40px);
  height: calc(12% - 20px);
  height:fit-content;
  margin: 20px;
  padding: 20px;
  /* border: 1px solid #000; */
  border-radius: 10px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.DepositCard:hover {
  transform: translateY(-10px);
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
}

</style>
