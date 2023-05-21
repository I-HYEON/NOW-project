<template>
  <div class="container">
    <div class="row">
      <div class="col-9">
        <h1>예적금 조회</h1>
        <div class="container align-items-center">
          <div class="container">
            <div v-if=show class="row">
              <DepositCard
              v-for="deposit in $store.state.depositData"
              :deposit="deposit"
              :key="deposit.id"
              />
            </div>
            <div v-else>
              <img src="@/photo/loading.gif" alt="로딩중...">
            </div>
          </div>
        </div>
      </div>
      <div class="col-3">
        <div class="container align-items-center">
          <div>
            <Login/>
          </div>
          <div class="container">
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
            <div class="col">바로가기1</div>
          </div>
        </div>
      </div>
    </div>
    <div>
      로고+번호+제작자
    </div>
  </div>
</template>



<script>
import Login from '@/components/Login.vue'
import DepositCard from '@/components/DepositCard.vue'
import axios from 'axios'

export default {
  name: 'DepositProducts',
  data() {
    return {
      show:false,
    }
  },
  components: {
    Login,
    DepositCard
  },
  methods: {
    async getDepositData() {
      const response = await axios.get('http://127.0.0.1:8000/deposits/save/')
      this.$store.commit('GET_DEPOSIT_DATA', response.data)
      this.show = true
    },
  },
  created(){
    // console.log('제발')
    this.getDepositData()
  },
}
</script>

<style>

</style>