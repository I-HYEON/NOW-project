<template>
  <div class="container">
    <div class="row">
      <div class="col-9">
        <div class="d-flex justify-content-between"><div>
          <h1>예적금 상세 정보</h1></div>
          <div class="d-flex">
            <button type="button" class="btn btn-primary" @click="">가입 신청</button>
            <button type="button" class="btn btn-danger" @click="">가입 취소</button>
          </div>
        </div>
        <div class="container align-items-center">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <div>{{ this.deposit_detail.fin_prdt_nm }}</div>
                <div>{{ this.deposit_detail.kor_co_nm }}</div>
                <div>{{ this.deposit_detail.mtrt_int }}</div>
                <div>{{ this.deposit_detail.etc_note }}</div>
                <div>{{ this.deposit_detail.spcl_cnd }}</div>
                <div>{{ this.deposit_detail.join_deny }}</div>
                <div>{{ this.deposit_detail.join_member }}</div>
                <div>{{ this.deposit_detail.join_way }}</div>                                            
              </div>
              <div class="col-12">
                <table class="table">
                  <tbody>
                    <Table
                    v-for="table in this.deposit_detail_options"
                    :table="table"
                    :key="table.id"
                    />
                  </tbody>
                </table>
              </div>
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
import Table from '@/components/Table.vue'
import axios from 'axios'

export default {
name: 'DepositDetail',
data(){
  return{
    deposit_detail:null,
    deposit_detail_options:null
  }
},
components: {
    Login,
    Table,
},
methods: {
    async getDepositData() {
      const response = await axios.get(`http://127.0.0.1:8000/deposits/detail/${this.$route.params.bank_info}`)
      this.$store.commit('GET_CURRENT_DETAIL', response.data)
      console.log(this.$store.state.currentDetail)
      this.set_info()
    },
    set_info() {
      this.deposit_detail = this.$store.state.currentDetail.deposit_detail
      this.deposit_detail_options = this.$store.state.currentDetail.deposit_detail_options
    },
    signDeposit() {
      
    }
},
created(){
    this.getDepositData()
},
}
</script>

<style>

</style>