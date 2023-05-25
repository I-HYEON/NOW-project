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
                            {{userInfo.age}}세</p>

                        <p v-if="userInfo.gender === 1">성별 : 남자</p>
                        <p v-else>성별 : 여자</p>

                        <p>
                            연봉 :
                            {{userInfo.salary}}만원</p>


<p v-if="userInfo.tendency === 1">투자성향 : 단기형</p>
<p v-else-if="userInfo.tendency === 2">투자성향 : 중기형</p>
<p v-else-if="userInfo.tendency === 3">투자성향 : 장기형</p>

<p> 재산 : {{userInfo.wealth}}만원</p>
<br>
<hr>
<p><h5>내가 쓴 게시글</h5></p>
<div>
  <div v-if="$store.state.articles.some(article => article.username===userInfo.username)">
    <div class="table-container">
      <table class="table table-hover">
        <thead>
          <tr>
            <!-- <th scope="col">#</th> -->
            <th scope="col">제목</th>
            <th scope="col">내용</th>
            <th scope="col">작성일</th>
          </tr>
        </thead>
        <tbody>
          <tr class="clickable" v-for="article in $store.state.articles" v-if='article.username===userInfo.username' :key="article.id" @click="check(article)">
            <th scope="row">{{ article.title }}</th>
            <th scope="row">{{ article.content }}</th>
            <th scope="row">{{article.created_at.substring(0, 10)}}</th>
    
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-else style="color:red;">
    쓴 글이 없습니다.
  </div>
</div>
<br>
<br>
<hr>
<p><h5>내가 좋아요한 게시글</h5></p>
<div>
  <div v-if="$store.state.articles.some(article => article.like_users.includes(userInfo.pk))">
    <div class="table-container">
      <table class="table table-hover">
        <thead>
          <tr>
            <!-- <th scope="col">#</th> -->
            <th scope="col">제목</th>
            <th scope="col">내용</th>
            <th scope="col">작성일</th>
          </tr>
        </thead>
        <tbody>
          <tr class="clickable" v-for="article in $store.state.articles" v-if='article.like_users.includes(userInfo.pk)' :key="article.id" @click="check(article)">
            <th scope="row">{{ article.title }}</th>
            <th scope="row">{{ article.content }}</th>
            <th scope="row">{{article.created_at.substring(0, 10)}}</th>
    
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-else style="color:red;">
    좋아요한 게시글이 없습니다.
  </div>
</div>

<br>
<br>
<hr>
<p><h5>가입 상품 목록</h5></p>
  <div v-if="userInfo.deposit.length === 0" style="color: red;">
    가입한 상품이 없습니다.
  </div>
  <div v-else class="d-flex justify-content-center flex-wrap">
    <div class="DepositCard" :class="{ 'hovered': isHovered }" @click="navigateToDetail(deposit)" v-for="(deposit,idx) in deposits" :key='idx' style="width: 14rem;" v-if="userInfo.deposit.includes(idx+1)">
      <img :src="getBankImage(deposit.kor_co_nm)" class="card-img-top" :alt="`Image not found: ${deposit.kor_co_nm}`">
      <div class="card-body">
        <h5 class="card-title">{{ deposit.fin_prdt_nm }}</h5>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item explain">{{ deposit.kor_co_nm }}</li>
        <li class="list-group-item explain">현재 가입자 수: {{ deposit.user_count }}</li>
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
            deposits:null,
            isHovered: false
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
    },

  
      getArticles() {
        this.$store.dispatch('getArticles')
        console.log(this.$store.state.articles)
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
      getBankImage(korCoNm) {
      try {
        return require(`@/bank_photo/${korCoNm}.png`);
      } catch (error) {
        console.error(error);
        return dummycat;
      }
    },
    navigateToDetail(deposit) {
      this.$router.push({
        name: 'deposit_detail',
        params: {
          bank_info: deposit.fin_prdt_cd
        }
      });
    },
    check(article){
      this.$router.push({
        name: 'ArticleDetailView',
        params: { id: article.id }
      });
    },
    

},
    created(){
    
    this.getArticles()
    this.getDepositData()
    }
}
</script>

<style scoped>

.profile-container {
  text-align:center;

}
.clickable {
      cursor: pointer;
    }
.DepositCard {
  background-color: white;
  color:black;
  width: calc(20% - 40px);
  height: calc(12% - 20px);
  /* margin: 20px; */
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