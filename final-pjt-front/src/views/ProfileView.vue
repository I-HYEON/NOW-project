<template>
    <div>
      <div class="profile-container">
        <h1>{{userInfo.username}}님의 프로필</h1>
      </div>
        <div class="container">
            <div class="row">
                <div class="col-9">
                    
                    <br>
                        <p>
                            나이 :
                            {{userInfo.age}}</p>

                        <p v-if="userInfo.gender === 1">성별 : 남자</p>
                        <p v-else>성별 : 여자</p>

                        <p>
                            연봉 :
                            {{userInfo.salary}}만원</p>


<p v-if="userInfo.tendency === 1">투자성향 : 단기형</p>
<p v-else-if="userInfo.tendency === 2">투자성향 : 중기형</p>
<p v-else-if="userInfo.tendency === 3">투자성향 : 장기형</p>

<p> 재산 : {{userInfo.wealth}}만원</p>

<!-- {{deposits}} -->
<div class="d-flex">
<div class="card" v-for="(deposit,idx) in deposits" :key='idx' style="width: 14rem;" v-if="userInfo.deposit.includes(idx+1)">
    <img :src="getBankImage(deposit.kor_co_nm)" class="card-img-top" :alt="`Image not found: ${deposit.kor_co_nm}`">
    <div class="card-body">
      <h5 class="card-title"></h5>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item explain">{{ deposit.fin_prdt_nm }}</li>
      <li class="list-group-item explain">{{ idx }}</li>
      <li class="list-group-item explain">{{ deposit.kor_co_nm }}</li>
      <li class="list-group-item explain">현재 가입자 수 : {{ deposit.user_count }}</li>
      <li class="list-group-item explain">
        <router-link
        class="link"
        :to="{
          name: 'deposit_detail',
          params: {
            bank_info : deposit.fin_prdt_cd
          }
        }">상세 보기</router-link>
      </li>
    </ul>
    <div class="card-body">
    </div>
  </div>
  </div>

<router-link to="/withdrawl">회원탈퇴</router-link>
<br>
<router-link to="/changepassword">비번변경</router-link>
<br>
<router-link to="/profileupdate">프로필변경</router-link>

                        <p>가입 상품 목록</p>
                        <div class="d-flex">
                            <div
                                class="card"
                                v-for="(deposit,idx) in deposits"
                                :key='idx'
                                style="width: 14rem;"
                                v-if="userInfo.deposit.includes(idx+1)">
                                <img
                                    :src="getBankImage(deposit.kor_co_nm)"
                                    class="card-img-top"
                                    :alt="`Image not found: ${deposit.kor_co_nm}`">
                                    <div class="card-body">
                                        <h5 class="card-title"></h5>
                                    </div>
                                    <ul class="list-group list-group-flush">
                                        <li class="list-group-item explain">{{ deposit.fin_prdt_nm }}</li>
                                        <li class="list-group-item explain">{{ deposit.kor_co_nm }}</li>
                                        <li class="list-group-item explain">현재 가입자 수 :
                                            {{ deposit.user_count }}</li>
                                        <li class="list-group-item explain">
                                            <router-link
                                                class="link"
                                                :to="{
                                                name: 'deposit_detail',
                                                params: {
                                                  bank_info : deposit.fin_prdt_cd
                                                }
                                              }">상세 보기</router-link>
                                        </li>
                                    </ul>
                                    <div class="card-body"></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-3">
                            <br>
                            <p><button type="button" @click="changePassword" class="btn btn-outline-info">비밀번호 변경</button></p>
                            <p><button type="button" @click="changeProfile" class="btn btn-outline-info">프로필 변경</button></p>
                            <p><button type="button" @click="withdrawl" class="btn btn-outline-info">회원탈퇴</button></p>

                                
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </template>
<script>

import axios from 'axios'
export default {
    name : 'ProfileView',
    data(){
        return{
            deposits:null
        }
    },

    computed: {
    isLogin() {
        return this.$store.getters.isLogin
    },
    userInfo() {
        console.log(this.$store.state.userInfo)
        return this.$store.state.userInfo
    }
},
      methods: {
    async getDepositData() {
      const response = await axios.get('http://127.0.0.1:8000/deposits/save/')
      this.$store.commit('GET_DEPOSIT_DATA', response.data)
      this.deposits = response.data
      // console.log(response.data)
      console.log(this.deposits)
    },

  
      getArticles() {
        this.$store.dispatch('getArticles')
      },
      getBankImage(korCoNm) {
      try {
        return require(`@/bank_photo/${korCoNm}.png`);
      } catch (error) {
        console.error(error);
        return dummycat;
      }
      }, 
      changePassword(){
        this.$router.push({name: 'ChangePassword'})
      },
      changeProfile(){
        this.$router.push({name: 'ProfileUpdateView'})
      },
      withdrawl(){
        this.$router.push({name: 'Withdrawl'})
      },

},
    created(){
    
    this.getArticles()
    this.getDepositData()
    }
}
</script>

<style>

.profile-container {
  text-align:center;

}

</style>