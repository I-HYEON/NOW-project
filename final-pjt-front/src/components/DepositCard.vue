<template>
  <div class="card" style="width: 18rem;">
    <img :src="getBankImage(deposit.kor_co_nm)" class="card-img-top" :alt="`Image not found: ${deposit.kor_co_nm}`">
    <div class="card-body">
      <h5 class="card-title"></h5>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item">{{ deposit.fin_prdt_nm }}</li>
      <li class="list-group-item">{{ deposit.kor_co_nm }}</li>
      <li class="list-group-item">현재 가입자 수 : {{ deposit.user_count }}</li>
    </ul>
    <div class="card-body">
      <router-link
      :to="{
        name: 'deposit_detail',
        params: {
          bank_info : deposit.fin_prdt_cd
        }
      }"><p>상세 보기</p></router-link>
    </div>
  </div>
</template>

<script>
import dummycat from "@/photo/dummycat.jpg"

export default {
  name: 'DepositCard',
  props: {
    deposit: Object
  },
  methods: {
    getBankImage(korCoNm) {
      try {
        return require(`@/bank_photo/${korCoNm}.png`);
      } catch (error) {
        console.error(error);
        return dummycat;
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
