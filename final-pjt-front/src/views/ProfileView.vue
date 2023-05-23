<template>
<div>
<h1> 프로필 페이지 입니다.</h1>
<!-- <p> 이름 : {{userInfo.username}}</p> -->
<p> 나이 : {{userInfo.age}}</p>


<p v-if="userInfo.gender === 1">성별 : 남자</p>
<p v-else>성별 : 여자</p>

<p> 연봉 : {{userInfo.salary}}만원</p>

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

<!-- {{deposits}} -->
<div class="card" v-for="(deposit,idx) in deposits" :key='idx' style="width: 14rem;">
    <img :src="getBankImage(deposit.kor_co_nm)" class="card-img-top" :alt="`Image not found: ${deposit.kor_co_nm}`">
    <div class="card-body">
      <h5 class="card-title"></h5>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item explain">{{ deposit.fin_prdt_nm }}</li>
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

<router-link to="/withdrawl">회원탈퇴</router-link>

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
        // console.log(this.$store.state.userInfo)
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
},
    created(){
    
    this.getArticles()
    this.getDepositData()
    }
}
</script>

<style>

</style>