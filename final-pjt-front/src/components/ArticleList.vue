<template>
  <div class="article-list">
    
    <h3>글목록</h3>
    
    <br>
    


    <br>
    <div class="table-container">
    <table class="table table-hover">
      <thead>
        <tr>
          <!-- <th scope="col">#</th> -->
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일</th>
        </tr>
      </thead>
      <tbody>
        <tr class="clickable" v-for="article in articles" :key="article.id" @click="check(article)">
          <th scope="row">{{ article.title }}</th>
          <td>{{article.username}}</td>
          <td>{{article.created_at.substring(0, 10)}}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <button type="button" @click='createArticle' class="btn btn-outline-success my-3">글쓰기</button>
  
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleList',
  data() {
    return {
      articles: null,
      alert: false,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    getArticles() {
      const API_URL = 'http://127.0.0.1:8000'
      const token = this.$store.state.token
      axios
        .get(`${API_URL}/articles/`, {
          // headers:{
         //Authorization: `Token ${this.$store.state.token}`
        // },
        })
        .then((response) => {
          this.articles = response.data
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    check(article){
      this.$router.push({
        name: 'ArticleDetailView',
        params: { id: article.id }
      });
    },
    createArticle(){
      if (this.isLogin) {this.$router.push({name: 'CreateView'})}
      else { alert('로그인을 해주세요') }
    }
  },
  created() {
    this.getArticles()
  },
}
</script>

<style >
.article-list {
  text-align: center;
}
.table-container {
  width: 80%; /* Adjust the width as needed */
  margin: 0 auto; /* Center the table horizontally */
}
.article-list table {
  width: 70%; /* 원하는 너비로 설정 */
  margin: 0 auto; /* 가운데 정렬을 위해 margin을 auto로 설정 */
}

.article-list table td {
  max-width: 200px; /* content의 최대 너비를 설정 */
  overflow: hidden; /* 너비를 초과하는 내용은 숨김 처리 */
  text-overflow: ellipsis; /* 너비를 초과하는 경우 말줄임표(...)로 표시 */
  white-space: nowrap; /* 줄바꿈 없이 한 줄로 표시 */
}
.toright{
  margin-left: 50%;
}
.clickable {
      cursor: pointer;
    }
</style>