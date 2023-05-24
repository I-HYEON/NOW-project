<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <div class="d-flex justify-content-between"><div>
          <h1>예적금 상세 정보</h1></div>
          <div class="d-flex" v-if="isLogin">
            <button v-if=show type="button" class="btn btn-danger" @click="signDeposit">가입 취소</button>
            <button v-else type="button" class="btn btn-primary" @click="signDeposit">가입 신청</button>
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
    </div>
    <div>
    <hr>
    </div>
    <br>
    <DepositComments :deposit_detail="deposit_detail" />
  </div>
</template>
  
  

<script>
import Table from '@/components/Table.vue'
import QuickBar from '@/components/QuickBar.vue'
import DepositComments from '@/components/DepositComments.vue'
import axios from 'axios'

export default {
name: 'DepositDetail',
computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userInfo() {
      return this.$store.state.userInfo
    }
},
data(){
  return{
    deposit_detail:null,
    deposit_detail_options:null,
    show:null
  }
},
components: {
    Table,
    QuickBar,
    DepositComments,
},
methods: {
    async getDepositData() {
      const response = await axios.get(`http://127.0.0.1:8000/deposits/detail/${this.$route.params.bank_info}`)
      this.$store.commit('GET_CURRENT_DETAIL', response.data)
      console.log(this.$store.state.currentDetail)
      this.set_info()
      this.check()
    },
    set_info() {
      this.deposit_detail = this.$store.state.currentDetail.deposit_detail
      this.deposit_detail_options = this.$store.state.currentDetail.deposit_detail_options
    },
    async signDeposit() {
      const response = await axios.post(`http://127.0.0.1:8000/deposits/detail/${this.$route.params.bank_info}/${this.userInfo.pk}/`)
      console.log(response)
      this.$store.commit('USERINFO',response.data)
      this.check()
    },
      check() {
        if(this.isLogin){
          if (this.userInfo.deposit.includes(this.deposit_detail.id)){
        this.show = true
          }else{
            this.show = false
          }
        }
      
    }
},
created(){
    this.getDepositData()
},
}
</script>

<style>

</style>