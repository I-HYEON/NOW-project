<template>
  <div class="container">
    <div class="row">
      <div class="col-9">
        <h1>예적금 조회</h1>
        <div class="container align-items-center">
          <div class="container">
            <div v-if=show class="row justify-content">
              <DepositCard
              class = "mx-auto my-1 col-12 col-md-6 col-lg-4 col-xl-3"
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
          <div>
            <QuickBar/>
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
import QuickBar from '@/components/QuickBar.vue'
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
    DepositCard,
    QuickBar,
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