<template>
  <div class="container">
    <div class="row">
      <div class="col-9">
        <h1>예적금 상세 정보</h1>
        <div class="container align-items-center">
          <div class="container">
            <div class="row">
              <div class="col-12">
                이름
              </div>
              <div class="col-12">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">First</th>
                      <th scope="col">Last</th>
                      <th scope="col">Handle</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Mark</td>
                      <td>Otto</td>
                      <td>@mdo</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>Jacob</td>
                      <td>Thornton</td>
                      <td>@fat</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td colspan="2">Larry the Bird</td>
                      <td>@twitter</td>
                    </tr>
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
import axios from 'axios'

export default {
name: 'DepositDetail',
components: {
    Login
},
methods: {
    async getDepositData() {
    const response = await axios.get(`'http://127.0.0.1:8000/deposits/detail/${this.$route.params.bank_info}'`)
    console.log(response)
    // this.$store.commit('GET_DEPOSIT_DATA', response.data)
    },
},
created(){
    // this.getDepositData()
},
}
</script>

<style>

</style>